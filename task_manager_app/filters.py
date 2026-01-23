# task_manager_app/filters.py
import django_filters
from .models import Task, Status, User, Label

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    executor = django_filters.ModelChoiceFilter(queryset=User.objects.all())
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

    def filter_my_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
