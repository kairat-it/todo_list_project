from django.db import models

class Task(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('new', 'Новая задача'),
        ('in_progress', 'Выполняется'),
        ('done', 'Сделано'),
    ]

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    due_date = models.DateField(null=True, blank=True)
    detail_views = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description
