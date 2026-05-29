from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    # If already logged in, redirect to correct dashboard
    if request.user.is_authenticated:
        return redirect_by_role(request.user)

    if request.method == 'POST':
        identifier = request.POST.get('identifier', '').strip()
        password   = request.POST.get('password', '')

        # Try username first, then email, then matricule
        from .models import User
        user = None

        # By username or email
        try:
            user_obj = User.objects.get(email=identifier)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            pass

        # By matricule (students)
        if user is None:
            try:
                user_obj = User.objects.get(matricule=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass

        # By username directly
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
    return render(request, 'accounts/admin_dashboard.html')


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