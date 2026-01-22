import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from task_manager_app.models import Label, Status, Task

pytestmark = pytest.mark.django_db

# ========================
# Helpers
# ========================

def create_user(username='testuser', password='12345'):
    return User.objects.create_user(username=username, password=password)

def login(client, username='testuser', password='12345'):
    user = create_user(username=username, password=password)
    client.login(username=username, password=password)
    return user

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

# ========================
# Task Tests
# ========================

def test_task_create_assigns_author(client):
    user = login(client)
    status = Status.objects.create(name='New Status')
    url = reverse('task-create')
    response = client.post(url, {
        'name': 'Task 1',
        'description': 'Описание',
        'status': status.id,
    })
    task = Task.objects.get(name='Task 1')
    assert task.author == user
    assert task.status == status

def test_task_create_with_labels(client):
    user = login(client)
    status = Status.objects.create(name='Статус')
    label1 = Label.objects.create(name='Баг')
    label2 = Label.objects.create(name='Фича')

    url = reverse('task-create')
    response = client.post(url, {
        'name': 'Задача с метками',
        'description': 'Описание',
        'status': status.id,
        'labels': [label1.id, label2.id],
    })
    task = Task.objects.get(name='Задача с метками')
    assert task.labels.count() == 2
    assert label1 in task.labels.all()
    assert label2 in task.labels.all()

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

def test_delete_label_with_task(client):
    user = login(client)
    status = Status.objects.create(name='Новый')
    label = Label.objects.create(name='Связанная')
    task = Task.objects.create(
        name='Задача с меткой',
        status=status,
        author=user
    )
    task.labels.add(label)
    url = reverse('label-delete', args=[label.id])
    response = client.post(url)
    # метка не удалена, так как связана с задачей
    assert Label.objects.filter(id=label.id).exists()
