import pytest
from django.urls import reverse
from task_manager_app.models import Label, Task, Status
from task_manager_app.tests.utils import create_user, login


pytestmark = pytest.mark.django_db 
# ========================
# Label Tests
# ========================

def test_label_list_requires_login(client):
    url = reverse('label-list')
    response = client.get(url)
    assert response.status_code == 302
    assert '/login/' in response.url

def test_create_label(client):
    login(client)
    url = reverse('label-create')
    response = client.post(url, {'name': 'Баг'})
    assert response.status_code == 302
    assert Label.objects.filter(name='Баг').exists()

def test_update_label(client):
    login(client)
    label = Label.objects.create(name='Старая')
    url = reverse('label-update', args=[label.id])
    response = client.post(url, {'name': 'Новая'})
    label.refresh_from_db()
    assert label.name == 'Новая'

def test_delete_label(client):
    login(client)
    label = Label.objects.create(name='Удалить')
    url = reverse('label-delete', args=[label.id])
    response = client.post(url)
    assert not Label.objects.filter(id=label.id).exists()
