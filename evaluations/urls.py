from django.urls import path
from . import views

urlpatterns = [
    # ── Module 5 — Student flow ───────────────────────────────────────────────
    path('student/teachers/',
         views.teachers_list,    name='teachers_list'),
    path('student/teachers/<int:teacher_pk>/courses/',
         views.courses_list,     name='courses_list'),
    path('student/evaluate/<int:teacher_pk>/<int:course_pk>/',
         views.evaluate,         name='evaluate'),
    path('student/evaluation/success/',
         views.evaluation_success, name='evaluation_success'),

    # ── Module 6 — Teacher results ────────────────────────────────────────────
    path('teacher/results/',
         views.teacher_results,      name='teacher_results'),
    path('teacher/results/download/',
         views.teacher_download_pdf, name='teacher_download_pdf'),

    # ── Module 6 — Admin evaluations ─────────────────────────────────────────
    path('admin/evaluations/',
         views.admin_evaluations,       name='admin_evaluations'),
    path('admin/evaluations/<int:pk>/',
         views.admin_evaluation_detail, name='admin_evaluation_detail'),
    path('admin/evaluations/<int:pk>/pdf/',
         views.admin_download_pdf,      name='admin_download_pdf'),
]
