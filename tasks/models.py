from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Task(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('new', 'Новая задача'),
        ('in_progress', 'Выполняется'),
        ('done', 'Сделано'),
    ]
    TYPE_CHOICES = [
        ('bug', 'Bug'),
        ('feature', 'Feature'),
        ('task', 'Task'),
    ]
    def validate_due_date(value):
        if value < timezone.now().date():
            raise ValidationError('Дата не может быть в прошлом')

    def validate_des_length(value):
        if len(value) < 10:
            raise ValidationError('Длина описания должна составлять не менее 10 символов')

    description = models.CharField(max_length=255,validators=[validate_des_length])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    task_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='task')
    due_date = models.DateField(null=True, blank=True, validators=[validate_due_date])
    detail_views = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


