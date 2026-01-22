from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Status
from .forms import StatusForm
from .forms import TaskForm
from .models import Task


# ========================
# Status Views
# ========================

class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'task_manager_app/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'task_manager_app/status_form.html'
    success_url = reverse_lazy('status-list')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно создан.')
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'task_manager_app/status_form.html'
    success_url = reverse_lazy('status-list')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно обновлен.')
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'task_manager_app/status_confirm_delete.html'
    success_url = reverse_lazy('status-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.exists():
            messages.error(request, 'Невозможно удалить статус, связанный с задачами.')
            return redirect('status-list')
        messages.success(request, 'Статус успешно удален.')
        return super().delete(request, *args, **kwargs)


# ========================
# Home / Index
# ========================

def home(request):
    return render(request, 'task_manager_app/index.html')


# ========================
# User Views
# ========================

class UserListView(ListView):
    model = User
    template_name = 'task_manager_app/user_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password']
    template_name = 'task_manager_app/user_form.html'
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request, 'Пользователь успешно создан.')
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'password']
    template_name = 'task_manager_app/user_form.html'
    success_url = reverse_lazy('user-list')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object() != request.user:
            messages.error(request, 'Вы можете редактировать только свой профиль.')
            return redirect('user-list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data['password']:
            user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request, 'Пользователь успешно обновлен.')
        return super().form_valid(form)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'task_manager_app/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.exists():  # если связь с задачами будет
            messages.error(request, 'Невозможно удалить пользователя, связанного с задачами.')
            return redirect('user-list')
        messages.success(request, 'Пользователь успешно удален.')
        return super().delete(request, *args, **kwargs)

# ========================
# User Task
# ========================

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_manager_app/task_form.html'  # создадим этот шаблон
    success_url = reverse_lazy('task-list')  # потом добавим такой url

    def form_valid(self, form):
        # автоматически ставим автора задачи
        form.instance.author = self.request.user
        messages.success(self.request, 'Задача успешно создана.')
        return super().form_valid(form)
    
    # ========================
# Task Views
# ========================

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_manager_app/task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_manager_app/task_detail.html'
    context_object_name = 'task'

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
        self.object = self.get_object()
        # Проверка: удалять может только автор
        if self.object.author != request.user:
            messages.error(request, 'Удалять задачу может только её автор.')
            return redirect('task-list')
        messages.success(request, 'Задача успешно удалена.')
        return super().delete(request, *args, **kwargs)
