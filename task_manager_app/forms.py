from django import forms
from .models import Status
from .models import Task


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor']