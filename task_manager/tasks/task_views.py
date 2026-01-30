from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django_filters.views import FilterView
from task_manager_app.models import Task, Status, Label
from task_manager_app.forms import TaskForm
from task_manager_app.filters import TaskFilter

class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'task_manager_app/task_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('only_mine'):
            queryset = queryset.filter(author=self.request.user)
        return queryset

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_manager_app/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_manager_app/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Задача успешно создана.')
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_manager_app/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, 'Задача успешно обновлена.')
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_manager_app/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != request.user:
            messages.error(request, 'Удалять задачу может только её автор.')
            return redirect('task-list')
        messages.success(request, 'Задача успешно удалена.')
        return super().delete(request, *args, **kwargs)
