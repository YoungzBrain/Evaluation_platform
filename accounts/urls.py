from django.urls import path
from . import views

urlpatterns = [
    # ── Auth ──────────────────────────────────────────────────────────────────
    path('login/',              views.login_view,        name='login'),
    path('logout/',             views.logout_view,       name='logout'),

    # ── Dashboards ────────────────────────────────────────────────────────────
    path('admin/dashboard/',    views.admin_dashboard,   name='admin_dashboard'),
    path('teacher/dashboard/',  views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/',  views.student_dashboard, name='student_dashboard'),

    # ── Teachers ──────────────────────────────────────────────────────────────
    path('admin/teachers/',                views.teachers_list,  name='teachers_list'),
    path('admin/teachers/create/',         views.teacher_create, name='teacher_create'),
    path('admin/teachers/<int:pk>/edit/',  views.teacher_edit,   name='teacher_edit'),
    path('admin/teachers/<int:pk>/toggle/',views.teacher_toggle, name='teacher_toggle'),
    path('admin/teachers/<int:pk>/delete/',views.teacher_delete, name='teacher_delete'),

    # ── Students ──────────────────────────────────────────────────────────────
    path('admin/students/',                views.students_list,  name='students_list'),
    path('admin/students/create/',         views.student_create, name='student_create'),
    path('admin/students/<int:pk>/edit/',  views.student_edit,   name='student_edit'),
    path('admin/students/<int:pk>/toggle/',views.student_toggle, name='student_toggle'),
    path('admin/students/<int:pk>/delete/',views.student_delete, name='student_delete'),
]