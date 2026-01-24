from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

class UserListView(LoginRequiredMixin, ListView):
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
    fields = ['username', 'first_name', 'last_name']
    template_name = 'task_manager_app/user_form.html'
    success_url = reverse_lazy('user-list')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object() != request.user:
            messages.error(request, 'Вы можете редактировать только свой профиль.')
            return redirect('user-list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Пользователь успешно обновлен.')
        return super().form_valid(form)

class UserDeleteView(DeleteView):
    model = User
    template_name = 'task_manager_app/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.exists():
            messages.error(request, 'Невозможно удалить пользователя, связанного с задачами.')
            return redirect('user-list')
        messages.success(request, 'Пользователь успешно удален.')
        return super().delete(request, *args, **kwargs)
