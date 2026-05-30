from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect_by_role(request.user)

    if request.method == 'POST':
        identifier = request.POST.get('identifier', '').strip()
        password   = request.POST.get('password', '')

        user = None

        # Try by email
        try:
            user_obj = User.objects.get(email=identifier)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            pass

        # Try by matricule
        if user is None:
            try:
                user_obj = User.objects.get(matricule=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass

        # Try by username directly
        if user is None:
            user = authenticate(request, username=identifier, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect_by_role(user)
        else:
            messages.error(request, 'Incorrect identifier or password.')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def redirect_by_role(user):
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'teacher':
        return redirect('teacher_dashboard')
    else:
        return redirect('student_dashboard')


@login_required
def admin_dashboard(request):
    if not request.user.is_admin():
        messages.error(request, 'Unauthorized access.')
        return redirect_by_role(request.user)

    total_teachers = User.objects.filter(role='teacher').count()
    total_students = User.objects.filter(role='student').count()

    return render(request, 'accounts/admin_dashboard.html', {
        'total_teachers': total_teachers,
        'total_students': total_students,
    })

@login_required
def teacher_dashboard(request):
    if not request.user.is_teacher():
        messages.error(request, 'Unauthorized access.')
        return redirect_by_role(request.user)
    return render(request, 'accounts/teacher_dashboard.html')


@login_required
def student_dashboard(request):
    if not request.user.is_student():
        messages.error(request, 'Unauthorized access.')
        return redirect_by_role(request.user)
    return render(request, 'accounts/student_dashboard.html')

# ── User Management ───────────────────────────────────────────────────────────

@login_required
def teachers_list(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    teachers = User.objects.filter(role='teacher').order_by('-date_joined')
    return render(request, 'accounts/teachers/index.html', {'teachers': teachers})


@login_required
def teacher_create(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    if request.method == 'POST':
        name       = request.POST.get('name', '').strip()
        email      = request.POST.get('email', '').strip()
        password   = request.POST.get('password', '')
        first_name = name.split(' ')[0]
        last_name  = ' '.join(name.split(' ')[1:])
        if User.objects.filter(email=email).exists():
            messages.error(request, 'A user with this email already exists.')
            return render(request, 'accounts/teachers/create.html')
        user = User.objects.create_user(
            username   = email,
            email      = email,
            password   = password,
            first_name = first_name,
            last_name  = last_name,
            role       = 'teacher',
        )
        messages.success(request, 'Teacher account created successfully.')
        return redirect('teachers_list')
    return render(request, 'accounts/teachers/create.html')


@login_required
def teacher_edit(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    teacher = User.objects.filter(pk=pk, role='teacher').first()
    if not teacher:
        messages.error(request, 'Teacher not found.')
        return redirect('teachers_list')
    if request.method == 'POST':
        name     = request.POST.get('name', '').strip()
        email    = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        teacher.first_name = name.split(' ')[0]
        teacher.last_name  = ' '.join(name.split(' ')[1:])
        teacher.email      = email
        teacher.username   = email
        if password:
            teacher.set_password(password)
        teacher.save()
        messages.success(request, 'Teacher updated successfully.')
        return redirect('teachers_list')
    return render(request, 'accounts/teachers/edit.html', {'teacher': teacher})


@login_required
def teacher_toggle(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    teacher = User.objects.filter(pk=pk, role='teacher').first()
    if not teacher:
        messages.error(request, 'Teacher not found.')
        return redirect('teachers_list')
    teacher.is_active = not teacher.is_active
    teacher.save()
    status = 'activated' if teacher.is_active else 'deactivated'
    messages.success(request, f'Teacher {status} successfully.')
    return redirect('teachers_list')


@login_required
def teacher_delete(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    teacher = User.objects.filter(pk=pk, role='teacher').first()
    if not teacher:
        messages.error(request, 'Teacher not found.')
        return redirect('teachers_list')
    teacher.delete()
    messages.success(request, 'Teacher deleted successfully.')
    return redirect('teachers_list')


@login_required
def students_list(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    students = User.objects.filter(role='student').order_by('-date_joined')
    return render(request, 'accounts/students/index.html', {'students': students})


@login_required
def student_create(request):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    if request.method == 'POST':
        name       = request.POST.get('name', '').strip()
        email      = request.POST.get('email', '').strip()
        matricule  = request.POST.get('matricule', '').strip()
        password   = request.POST.get('password', '')
        first_name = name.split(' ')[0]
        last_name  = ' '.join(name.split(' ')[1:])
        if User.objects.filter(email=email).exists():
            messages.error(request, 'A user with this email already exists.')
            return render(request, 'accounts/students/create.html')
        if User.objects.filter(matricule=matricule).exists():
            messages.error(request, 'A user with this matricule already exists.')
            return render(request, 'accounts/students/create.html')
        User.objects.create_user(
            username   = email,
            email      = email,
            password   = password,
            first_name = first_name,
            last_name  = last_name,
            role       = 'student',
            matricule  = matricule,
        )
        messages.success(request, 'Student account created successfully.')
        return redirect('students_list')
    return render(request, 'accounts/students/create.html')


@login_required
def student_edit(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    student = User.objects.filter(pk=pk, role='student').first()
    if not student:
        messages.error(request, 'Student not found.')
        return redirect('students_list')
    if request.method == 'POST':
        name      = request.POST.get('name', '').strip()
        email     = request.POST.get('email', '').strip()
        matricule = request.POST.get('matricule', '').strip()
        password  = request.POST.get('password', '')
        student.first_name = name.split(' ')[0]
        student.last_name  = ' '.join(name.split(' ')[1:])
        student.email      = email
        student.username   = email
        student.matricule  = matricule
        if password:
            student.set_password(password)
        student.save()
        messages.success(request, 'Student updated successfully.')
        return redirect('students_list')
    return render(request, 'accounts/students/edit.html', {'student': student})


@login_required
def student_toggle(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    student = User.objects.filter(pk=pk, role='student').first()
    if not student:
        messages.error(request, 'Student not found.')
        return redirect('students_list')
    student.is_active = not student.is_active
    student.save()
    status = 'activated' if student.is_active else 'deactivated'
    messages.success(request, f'Student {status} successfully.')
    return redirect('students_list')


@login_required
def student_delete(request, pk):
    if not request.user.is_admin():
        return redirect_by_role(request.user)
    student = User.objects.filter(pk=pk, role='student').first()
    if not student:
        messages.error(request, 'Student not found.')
        return redirect('students_list')
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('students_list')