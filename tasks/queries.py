from django.utils import timezone
from django.db.models import Q
from .models import Task
import datetime

one_month_ago = timezone.now() - datetime.timedelta(days=30)
closed_tasks_last_month = Task.objects.filter(status='done', updated_at__gte=one_month_ago)

status_choices = ['in_progress', 'done']
type_choices = ['feature', 'bug']
tasks_with_status_and_type = Task.objects.filter(status__in=status_choices, task_type__in=type_choices)

not_closed_tasks_with_bug = Task.objects.filter(
    Q(status__in=['new', 'in_progress']) & (Q(description__icontains='bug') | Q(task_type='bug'))
)

print("Закрытые задачи в прошлом месяце:", closed_tasks_last_month)
print("Задачи с заданным статусом и типом:", tasks_with_status_and_type)
print("Незакрытые задачи с 'bug' в описании или типе 'Bug':", not_closed_tasks_with_bug)
