import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from task_manager_app.models import Label, Status, Task
from task_manager_app.tests.utils import create_user, login

pytestmark = pytest.mark.django_db

# ========================
# Status Tests
# ========================

def test_status_list_requires_login(client):
    url = reverse('status-list')
    response = client.get(url)
    assert response.status_code == 302
    assert '/login/' in response.url

def test_create_status(client):
    login(client)
    url = reverse('status-create')
    response = client.post(url, {'name': 'Новый'})
    assert response.status_code == 302
    assert Status.objects.filter(name='Новый').exists()

def test_update_status(client):
    login(client)
    status = Status.objects.create(name='Старый')
    url = reverse('status-update', args=[status.id])
    response = client.post(url, {'name': 'Обновлённый'})
    status.refresh_from_db()
    assert status.name == 'Обновлённый'

def test_delete_status(client):
    login(client)
    status = Status.objects.create(name='Удалить')
    url = reverse('status-delete', args=[status.id])
    response = client.post(url)
    assert not Status.objects.filter(id=status.id).exists()
