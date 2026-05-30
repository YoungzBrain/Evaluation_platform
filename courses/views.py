from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, TeacherCourse
from accounts.models import User


def redirect_by_role(user):
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'teacher':
        return redirect('teacher_dashboard')
    return redirect('student_dashboard')


# ── Course List ───────────────────────────────────────────────────────────────

@login_required
def courses_list(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    courses = Course.objects.prefetch_related('teacher_courses__teacher').all()
    return render(request, 'courses/index.html', {'courses': courses})


# ── Create Course ─────────────────────────────────────────────────────────────

@login_required
def course_create(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    teachers = User.objects.filter(role='teacher', is_active=True).order_by('first_name')

    if request.method == 'POST':
        name        = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        teacher_ids = request.POST.getlist('teacher_ids')

        if not name:
            messages.error(request, 'Course name is required.')
            return render(request, 'courses/create.html', {'teachers': teachers})

        if Course.objects.filter(name__iexact=name).exists():
            messages.error(request, 'A course with this name already exists.')
            return render(request, 'courses/create.html', {'teachers': teachers})

        course = Course.objects.create(name=name, description=description)

        for tid in teacher_ids:
            try:
                teacher = User.objects.get(pk=tid, role='teacher')
                TeacherCourse.objects.get_or_create(teacher=teacher, course=course)
            except User.DoesNotExist:
                pass

        messages.success(request, 'Course created successfully.')
        return redirect('courses_list')

    return render(request, 'courses/create.html', {'teachers': teachers})


# ── Edit Course ───────────────────────────────────────────────────────────────

@login_required
def course_edit(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    course   = get_object_or_404(Course, pk=pk)
    teachers = User.objects.filter(role='teacher', is_active=True).order_by('first_name')
    assigned_ids = list(course.teacher_courses.values_list('teacher_id', flat=True))

    if request.method == 'POST':
        name        = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        teacher_ids = request.POST.getlist('teacher_ids')

        if not name:
            messages.error(request, 'Course name is required.')
            return render(request, 'courses/edit.html', {
                'course': course, 'teachers': teachers, 'assigned_ids': assigned_ids
            })

        if Course.objects.filter(name__iexact=name).exclude(pk=pk).exists():
            messages.error(request, 'A course with this name already exists.')
            return render(request, 'courses/edit.html', {
                'course': course, 'teachers': teachers, 'assigned_ids': assigned_ids
            })

        course.name        = name
        course.description = description
        course.save()

        # Sync teacher assignments
        new_ids = set(int(tid) for tid in teacher_ids if tid.isdigit())
        old_ids = set(assigned_ids)

        # Remove unselected
        course.teacher_courses.filter(teacher_id__in=old_ids - new_ids).delete()

        # Add new ones
        for tid in new_ids - old_ids:
            try:
                teacher = User.objects.get(pk=tid, role='teacher')
                TeacherCourse.objects.get_or_create(teacher=teacher, course=course)
            except User.DoesNotExist:
                pass

        messages.success(request, 'Course updated successfully.')
        return redirect('courses_list')

    return render(request, 'courses/edit.html', {
        'course': course,
        'teachers': teachers,
        'assigned_ids': assigned_ids,
    })


# ── Toggle Active ─────────────────────────────────────────────────────────────

@login_required
def course_toggle(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    course = get_object_or_404(Course, pk=pk)
    course.is_active = not course.is_active
    course.save()
    status = 'activated' if course.is_active else 'deactivated'
    messages.success(request, f'Course {status} successfully.')
    return redirect('courses_list')


# ── Delete Course ─────────────────────────────────────────────────────────────

@login_required
def course_delete(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    course = get_object_or_404(Course, pk=pk)
    course.delete()
    messages.success(request, 'Course deleted successfully.')
    return redirect('courses_list')


# ── Assign Teachers (standalone page) ────────────────────────────────────────

@login_required
def course_assign(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)

    course   = get_object_or_404(Course, pk=pk)
    teachers = User.objects.filter(role='teacher', is_active=True).order_by('first_name')
    assigned_ids = list(course.teacher_courses.values_list('teacher_id', flat=True))

    if request.method == 'POST':
        teacher_ids = request.POST.getlist('teacher_ids')
        new_ids = set(int(tid) for tid in teacher_ids if tid.isdigit())
        old_ids = set(assigned_ids)

        course.teacher_courses.filter(teacher_id__in=old_ids - new_ids).delete()
        for tid in new_ids - old_ids:
            try:
                teacher = User.objects.get(pk=tid, role='teacher')
                TeacherCourse.objects.get_or_create(teacher=teacher, course=course)
            except User.DoesNotExist:
                pass

        messages.success(request, 'Teacher assignments updated.')
        return redirect('courses_list')

    return render(request, 'courses/assign.html', {
        'course': course,
        'teachers': teachers,
        'assigned_ids': assigned_ids,
    })
