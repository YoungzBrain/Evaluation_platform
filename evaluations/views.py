import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Avg
from django.http import FileResponse, Http404

from django.conf import settings
from accounts.models import User
from courses.models import Course, TeacherCourse
from questions.models import Question
from .models import Evaluation, Answer, EvaluationPdf
from .utils import generate_evaluation_pdf, generate_teacher_report_pdf, PDF_DIR


# ════════════════════════════════════════════════════════════════════════════
#  MODULE 5 — Student evaluation flow (unchanged from your camarade's code)
# ════════════════════════════════════════════════════════════════════════════

@login_required
def teachers_list(request):
    if not request.user.is_student():
        messages.error(request, 'Unauthorized access.')
        return redirect('student_dashboard')

    teacher_ids = TeacherCourse.objects.values_list('teacher_id', flat=True).distinct()
    teachers    = User.objects.filter(pk__in=teacher_ids, role='teacher', is_active=True)

    return render(request, 'evaluations/teachers_list.html', {'teachers': teachers})


@login_required
def courses_list(request, teacher_pk):
    if not request.user.is_student():
        messages.error(request, 'Unauthorized access.')
        return redirect('student_dashboard')

    teacher    = get_object_or_404(User, pk=teacher_pk, role='teacher', is_active=True)
    course_ids = TeacherCourse.objects.filter(teacher=teacher).values_list('course_id', flat=True)
    courses    = Course.objects.filter(pk__in=course_ids, is_active=True)

    evaluated_course_ids = Evaluation.objects.filter(
        student=request.user, teacher=teacher, status='submitted'
    ).values_list('course_id', flat=True)

    return render(request, 'evaluations/courses_list.html', {
        'teacher':              teacher,
        'courses':              courses,
        'evaluated_course_ids': list(evaluated_course_ids),
    })


@login_required
def evaluate(request, teacher_pk, course_pk):
    if not request.user.is_student():
        messages.error(request, 'Unauthorized access.')
        return redirect('student_dashboard')

    teacher = get_object_or_404(User,   pk=teacher_pk, role='teacher', is_active=True)
    course  = get_object_or_404(Course, pk=course_pk,  is_active=True)

    already_evaluated = Evaluation.objects.filter(
        student=request.user, teacher=teacher, course=course, status='submitted'
    ).exists()

    if already_evaluated:
        messages.error(request, 'You have already evaluated this teacher for this course.')
        return redirect('courses_list', teacher_pk=teacher_pk)

    questions = Question.objects.filter(is_active=True).select_related('category')

    if request.method == 'POST':
        try:
            evaluation = Evaluation.objects.create(
                student=request.user,
                teacher=teacher,
                course=course,
                status='submitted'
            )
        except IntegrityError:
            messages.error(request, 'You have already submitted this evaluation.')
            return redirect('courses_list', teacher_pk=teacher_pk)

        for question in questions:
            if question.type == 'scored':
                score = request.POST.get(f'question_{question.pk}')
                if score:
                    Answer.objects.create(evaluation=evaluation, question=question, score=int(score))
            else:
                text = request.POST.get(f'question_{question.pk}', '').strip()
                if text:
                    Answer.objects.create(evaluation=evaluation, question=question, text_answer=text)

        # ── Module 6: auto-generate PDF after submission ───────────────────
        try:
            generate_evaluation_pdf(evaluation)
        except Exception:
            pass  # PDF generation failure must not block submission

        messages.success(request, 'Evaluation submitted successfully.')
        return redirect('evaluation_success')

    return render(request, 'evaluations/evaluate.html', {
        'teacher': teacher, 'course': course, 'questions': questions,
    })


@login_required
def evaluation_success(request):
    if not request.user.is_student():
        return redirect('student_dashboard')
    return render(request, 'evaluations/success.html')


# ════════════════════════════════════════════════════════════════════════════
#  MODULE 6 — Teacher results + Admin overview + PDF download
# ════════════════════════════════════════════════════════════════════════════

# ── Teacher: view own results ─────────────────────────────────────────────────

@login_required
def teacher_results(request):
    if not request.user.is_teacher():
        messages.error(request, 'Unauthorized access.')
        return redirect('teacher_dashboard')

    evaluations = Evaluation.objects.filter(
        teacher=request.user, status='submitted'
    ).select_related('course', 'student')

    course_ids = evaluations.values_list('course_id', flat=True).distinct()
    courses    = Course.objects.filter(pk__in=course_ids)

    course_results = []
    for course in courses:
        course_evals = evaluations.filter(course=course)
        eval_count   = course_evals.count()

        # Scored question averages
        question_stats = []
        q_ids = Answer.objects.filter(
            evaluation__in=course_evals, question__type='scored'
        ).values_list('question_id', flat=True).distinct()
        scored_questions = Question.objects.filter(pk__in=q_ids)

        for q in scored_questions:
            avg = Answer.objects.filter(
                evaluation__in=course_evals, question=q, score__isnull=False
            ).aggregate(avg=Avg('score'))['avg']
            question_stats.append({
                'question': q,
                'avg':      round(avg, 1) if avg else None,
            })

        # Open answers
        open_answers = Answer.objects.filter(
            evaluation__in=course_evals,
            question__type='open',
            text_answer__isnull=False,
        ).exclude(text_answer='').select_related('question')

        # Global average for this course
        all_scores = Answer.objects.filter(
            evaluation__in=course_evals,
            question__type='scored',
            score__isnull=False,
        ).aggregate(avg=Avg('score'))['avg']

        course_results.append({
            'course':         course,
            'eval_count':     eval_count,
            'question_stats': question_stats,
            'open_answers':   open_answers,
            'global_avg':     round(all_scores, 1) if all_scores else None,
        })

    return render(request, 'evaluations/teacher/results.html', {
        'course_results': course_results,
        'total_evals':    evaluations.count(),
    })


# ── Teacher: download own full report PDF ─────────────────────────────────────

@login_required
def teacher_download_pdf(request):
    if not request.user.is_teacher():
        return redirect('teacher_dashboard')

    evaluations = Evaluation.objects.filter(teacher=request.user, status='submitted')
    course_ids  = evaluations.values_list('course_id', flat=True).distinct()
    courses     = Course.objects.filter(pk__in=course_ids)

    course_results = []
    for course in courses:
        course_evals = evaluations.filter(course=course)
        q_ids = Answer.objects.filter(
            evaluation__in=course_evals, question__type='scored'
        ).values_list('question_id', flat=True).distinct()
        scored_questions = Question.objects.filter(pk__in=q_ids)

        question_stats = []
        for q in scored_questions:
            avg = Answer.objects.filter(
                evaluation__in=course_evals, question=q, score__isnull=False
            ).aggregate(avg=Avg('score'))['avg']
            question_stats.append({'question': q, 'avg': round(avg, 1) if avg else None})

        open_answers = Answer.objects.filter(
            evaluation__in=course_evals, question__type='open',
            text_answer__isnull=False,
        ).exclude(text_answer='').select_related('question')

        course_results.append({
            'course':         course,
            'eval_count':     course_evals.count(),
            'question_stats': question_stats,
            'open_answers':   open_answers,
        })

    filename = generate_teacher_report_pdf(request.user, course_results)
    filepath = os.path.join(PDF_DIR, filename)

    if not os.path.exists(filepath):
        raise Http404("PDF could not be generated.")

    return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=filename)


# ── Admin: list all evaluations ───────────────────────────────────────────────

@login_required
def admin_evaluations(request):
    if not request.user.is_admin():
        messages.error(request, 'Unauthorized access.')
        return redirect('admin_dashboard')

    teacher_id = request.GET.get('teacher')
    course_id  = request.GET.get('course')

    evaluations = Evaluation.objects.filter(status='submitted') \
        .select_related('student', 'teacher', 'course') \
        .order_by('-created_at')

    if teacher_id:
        evaluations = evaluations.filter(teacher_id=teacher_id)
    if course_id:
        evaluations = evaluations.filter(course_id=course_id)

    teachers = User.objects.filter(role='teacher', is_active=True).order_by('first_name')
    courses  = Course.objects.filter(is_active=True).order_by('name')

    return render(request, 'evaluations/admin/list.html', {
        'evaluations':      evaluations,
        'teachers':         teachers,
        'courses':          courses,
        'selected_teacher': teacher_id,
        'selected_course':  course_id,
        'total':            evaluations.count(),
    })


# ── Admin: evaluation detail + PDF download ───────────────────────────────────

@login_required
def admin_evaluation_detail(request, pk):
    if not request.user.is_admin():
        messages.error(request, 'Unauthorized access.')
        return redirect('admin_dashboard')

    evaluation = get_object_or_404(
        Evaluation.objects.select_related('student', 'teacher', 'course'), pk=pk
    )
    answers = evaluation.answers.select_related('question', 'question__category').order_by('question__id')

    # Check if PDF exists
    has_pdf = EvaluationPdf.objects.filter(evaluation=evaluation).exists()

    return render(request, 'evaluations/admin/detail.html', {
        'evaluation': evaluation,
        'answers':    answers,
        'has_pdf':    has_pdf,
    })


# ── Download a single evaluation PDF (admin) ──────────────────────────────────

@login_required
def admin_download_pdf(request, pk):
    if not request.user.is_admin():
        return redirect('admin_dashboard')

    evaluation = get_object_or_404(Evaluation, pk=pk, status='submitted')

    # Generate if not already done
    pdf_record = EvaluationPdf.objects.filter(evaluation=evaluation).first()
    if not pdf_record:
        pdf_record = generate_evaluation_pdf(evaluation)

    filepath = os.path.join(PDF_DIR, pdf_record.file_path)
    if not os.path.exists(filepath):
        # Regenerate
        pdf_record = generate_evaluation_pdf(evaluation)
        filepath   = os.path.join(PDF_DIR, pdf_record.file_path)

    return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=pdf_record.file_path)
