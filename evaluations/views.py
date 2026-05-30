from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError

from accounts.models import User
from courses.models import Course, TeacherCourse
from questions.models import Question
from .models import Evaluation, Answer


@login_required
def teachers_list(request):
    if not request.user.is_student():
        messages.error(request, 'Unauthorized access.')
        return redirect('student_dashboard')

    # Get all teachers who have at least one active course assigned
    teacher_ids = TeacherCourse.objects.values_list('teacher_id', flat=True).distinct()
    teachers    = User.objects.filter(pk__in=teacher_ids, role='teacher', is_active=True)

    return render(request, 'evaluations/teachers_list.html', {
        'teachers': teachers
    })


@login_required
def courses_list(request, teacher_pk):
    if not request.user.is_student():
        messages.error(request, 'Unauthorized access.')
        return redirect('student_dashboard')

    teacher = get_object_or_404(User, pk=teacher_pk, role='teacher', is_active=True)

    # Get courses assigned to this teacher
    course_ids = TeacherCourse.objects.filter(teacher=teacher).values_list('course_id', flat=True)
    courses    = Course.objects.filter(pk__in=course_ids, is_active=True)

    # Mark courses already evaluated by this student for this teacher
    evaluated_course_ids = Evaluation.objects.filter(
        student=request.user,
        teacher=teacher,
        status='submitted'
    ).values_list('course_id', flat=True)

    return render(request, 'evaluations/courses_list.html', {
        'teacher':             teacher,
        'courses':             courses,
        'evaluated_course_ids': list(evaluated_course_ids),
    })


@login_required
def evaluate(request, teacher_pk, course_pk):
    if not request.user.is_student():
        messages.error(request, 'Unauthorized access.')
        return redirect('student_dashboard')

    teacher = get_object_or_404(User,   pk=teacher_pk, role='teacher', is_active=True)
    course  = get_object_or_404(Course, pk=course_pk,  is_active=True)

    # Block if already evaluated
    already_evaluated = Evaluation.objects.filter(
        student=request.user,
        teacher=teacher,
        course=course,
        status='submitted'
    ).exists()

    if already_evaluated:
        messages.error(request, 'You have already evaluated this teacher for this course.')
        return redirect('courses_list', teacher_pk=teacher_pk)

    # Get all active questions
    questions = Question.objects.filter(is_active=True).select_related('category')

    if request.method == 'POST':
        # Create evaluation
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

        # Save answers
        for question in questions:
            if question.type == 'scored':
                score = request.POST.get(f'question_{question.pk}')
                if score:
                    Answer.objects.create(
                        evaluation=evaluation,
                        question=question,
                        score=int(score),
                    )
            else:
                text = request.POST.get(f'question_{question.pk}', '').strip()
                if text:
                    Answer.objects.create(
                        evaluation=evaluation,
                        question=question,
                        text_answer=text,
                    )

        messages.success(request, 'Evaluation submitted successfully.')
        return redirect('evaluation_success')

    return render(request, 'evaluations/evaluate.html', {
        'teacher':   teacher,
        'course':    course,
        'questions': questions,
    })


@login_required
def evaluation_success(request):
    if not request.user.is_student():
        return redirect('student_dashboard')
    return render(request, 'evaluations/success.html')