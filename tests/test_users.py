import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from task_manager_app.tests.utils import login


pytestmark = pytest.mark.django_db 
# ========================
# User Tests
# ========================

def test_user_list_requires_login(client):
    url = reverse('user-list')
    response = client.get(url)
    assert response.status_code == 302
    assert '/login/' in response.url

def test_create_user(client):
    url = reverse('user-create')
    response = client.post(url, {'username': 'newuser', 'password': 'pass123'})
    assert response.status_code == 302
    assert User.objects.filter(username='newuser').exists()

def test_update_user(client):
    user = login(client)
    url = reverse('user-update', args=[user.id])
    response = client.post(url, {'username': 'updateduser', 'password': ''})
    user.refresh_from_db()
    assert user.username == 'updateduser'

def test_delete_user(client):
    user = login(client)
    url = reverse('user-delete', args=[user.id])
    response = client.post(url)
    assert not User.objects.filter(id=user.id).exists()
