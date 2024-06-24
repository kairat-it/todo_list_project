from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'status', 'due_date']
        labels = {
            'description': 'Описание',
            'status': 'Статус',
            'due_date': 'Дата выполнения',
        }
