from django.db import models
from django.conf import settings
from courses.models import Course
from questions.models import Question


class Evaluation(models.Model):

    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('submitted', 'Submitted'),
    ]

    student    = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='evaluations_as_student',
        limit_choices_to={'role': 'student'}
    )
    teacher    = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='evaluations_as_teacher',
        limit_choices_to={'role': 'teacher'}
    )
    course     = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='evaluations'
    )
    status     = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # One student can only evaluate one teacher per course once
        unique_together = ('student', 'teacher', 'course')
        ordering        = ['-created_at']

    def __str__(self):
        return f"{self.student} → {self.teacher} ({self.course})"


class Answer(models.Model):
    evaluation  = models.ForeignKey(
        Evaluation,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    question    = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    score       = models.PositiveSmallIntegerField(null=True, blank=True)
    text_answer = models.TextField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('evaluation', 'question')

    def __str__(self):
        return f"Answer to {self.question} in {self.evaluation}"