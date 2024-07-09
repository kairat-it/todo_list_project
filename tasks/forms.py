from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'status', 'due_date', 'detail_views']
        labels = {
            'description': 'Описание',
            'status': 'Статус',
            'due_date': 'Дата выполнения',
            'detail_views': 'Подробнее'
        }
        widgets = {
            'due_date': forms.TextInput(attrs={'type': 'date'}),
        }
