from django.db import models


class Category(models.Model):
    name        = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering   = ['name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Question(models.Model):
    TYPE_CHOICES = [
        ('scored', 'Scored (1–5)'),
        ('open',   'Open (text)'),
    ]

    text       = models.TextField()
    type       = models.CharField(max_length=10, choices=TYPE_CHOICES, default='scored')
    category   = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='questions'
    )
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category__name', 'id']

    def __str__(self):
        return self.text[:80]
