from django.contrib import admin
from .models import Category, Question


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'description', 'created_at')
    search_fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display  = ('text', 'type', 'category', 'is_active', 'created_at')
    list_filter   = ('type', 'is_active', 'category')
    search_fields = ('text',)
