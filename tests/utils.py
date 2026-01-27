import pytest
from django.contrib.auth.models import User


pytestmark = pytest.mark.django_db

def create_user(username='testuser', password='12345'):
    return User.objects.create_user(username=username, password=password)

def login(client, username='testuser', password='12345'):
    user = create_user(username=username, password=password)
    client.login(username=username, password=password)
    return user