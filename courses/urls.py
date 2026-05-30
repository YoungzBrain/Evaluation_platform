from django.urls import path
from . import views

urlpatterns = [
    # ── Courses ───────────────────────────────────────────────────────────────
    path('admin/courses/',                    views.courses_list,   name='courses_list'),
    path('admin/courses/create/',             views.course_create,  name='course_create'),
    path('admin/courses/<int:pk>/edit/',      views.course_edit,    name='course_edit'),
    path('admin/courses/<int:pk>/toggle/',    views.course_toggle,  name='course_toggle'),
    path('admin/courses/<int:pk>/delete/',    views.course_delete,  name='course_delete'),
    path('admin/courses/<int:pk>/assign/',    views.course_assign,  name='course_assign'),
]
