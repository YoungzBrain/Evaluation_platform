from django.urls import path
from . import views

urlpatterns = [
    # ── Categories ────────────────────────────────────────────────────────────
    path('admin/categories/',                   views.categories_list,  name='categories_list'),
    path('admin/categories/create/',            views.category_create,  name='category_create'),
    path('admin/categories/<int:pk>/edit/',     views.category_edit,    name='category_edit'),
    path('admin/categories/<int:pk>/delete/',   views.category_delete,  name='category_delete'),

    # ── Questions ─────────────────────────────────────────────────────────────
    path('admin/questions/',                    views.questions_list,   name='questions_list'),
    path('admin/questions/create/',             views.question_create,  name='question_create'),
    path('admin/questions/<int:pk>/edit/',      views.question_edit,    name='question_edit'),
    path('admin/questions/<int:pk>/toggle/',    views.question_toggle,  name='question_toggle'),
    path('admin/questions/<int:pk>/delete/',    views.question_delete,  name='question_delete'),
]
