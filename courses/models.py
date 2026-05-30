from django.db import models
from django.conf import settings


class Course(models.Model):
    name        = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class TeacherCourse(models.Model):
    teacher    = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='teacher_courses',
        limit_choices_to={'role': 'teacher'}
    )
    course     = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teacher_courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('teacher', 'course')

    def __str__(self):
        return f"{self.teacher} — {self.course}"
