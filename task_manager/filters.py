# task_manager/filters.py
import django_filters
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    executor = django_filters.ModelChoiceFilter(queryset=User.objects.none())
    labels = django_filters.ModelMultipleChoiceFilter(
        queryset=Label.objects.all(),
        conjoined=False,
    )
    my_tasks = django_filters.BooleanFilter(
        method='filter_my_tasks',
        label='Только мои задачи',
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'my_tasks']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['executor'].queryset = User.objects.all()

    def filter_my_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
