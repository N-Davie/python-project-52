from django import forms
from .models import Status, Task, Label
from django.contrib.auth.models import User


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }