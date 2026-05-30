from django.urls import path
from . import views

urlpatterns = [
    path('student/teachers/',                          views.teachers_list,    name='teachers_list'),
    path('student/teachers/<int:teacher_pk>/courses/', views.courses_list,     name='courses_list'),
    path('student/evaluate/<int:teacher_pk>/<int:course_pk>/', views.evaluate, name='evaluate'),
    path('student/evaluation/success/',                views.evaluation_success, name='evaluation_success'),
]