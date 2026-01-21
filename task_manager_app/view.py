from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

# Вашу функцию home оставить как есть
def home(request):
    return render(request, 'task_manager_app/index.html')

# Далее — классы для управления пользователями

class UserListView(ListView):
    model = User
    template_name = 'task_manager_app/user_list.html'
    context_object_name = 'users'
    # Можно добавить или убрать, зависит от доступа

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password', 'email', 'first_name', 'last_name']
    template_name = 'task_manager_app/user_form.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'task_manager_app/user_form.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        return self.request.user == self.get_object()

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'task_manager_app/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        return self.request.user == self.get_object() or self.request.user.is_superuser
