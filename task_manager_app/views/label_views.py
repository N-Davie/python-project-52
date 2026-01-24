from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from task_manager_app.models import Label
from task_manager_app.forms import LabelForm

class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'task_manager_app/label_list.html'
    context_object_name = 'labels'

class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'task_manager_app/label_form.html'
    success_url = reverse_lazy('label-list')

    def form_valid(self, form):
        messages.success(self.request, 'Метка успешно создана.')
        return super().form_valid(form)

class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'task_manager_app/label_form.html'
    success_url = reverse_lazy('label-list')

    def form_valid(self, form):
        messages.success(self.request, 'Метка успешно обновлена.')
        return super().form_valid(form)

class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'task_manager_app/label_confirm_delete.html'
    success_url = reverse_lazy('label-list')

    def delete(self, request, *args, **kwargs):
        label = self.get_object()
        if label.task_set.exists():
            messages.error(request, 'Невозможно удалить метку, связанную с задачами.')
            return redirect('label-list')
        messages.success(request, 'Метка успешно удалена.')
        return super().delete(request, *args, **kwargs)
