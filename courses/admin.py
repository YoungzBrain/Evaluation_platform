from django.contrib import admin
from .models import Course, TeacherCourse


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display  = ('name', 'is_active', 'created_at')
    list_filter   = ('is_active',)
    search_fields = ('name',)


@admin.register(TeacherCourse)
class TeacherCourseAdmin(admin.ModelAdmin):
    list_display  = ('teacher', 'course', 'created_at')
    list_filter   = ('course',)
    search_fields = ('teacher__email', 'course__name')
