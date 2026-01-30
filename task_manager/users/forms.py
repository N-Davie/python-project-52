from django.contrib.auth.forms import UserCreationForm
from .models import AppUser


class UserForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = [
            'first_name',
            'last_name',
            'username',
        ]
