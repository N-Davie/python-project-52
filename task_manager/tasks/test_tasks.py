import pytest
from django.urls import reverse
from task_manager_app.models import Task, Status, Label
from task_manager_app.tests.utils import create_user, login

pytestmark = pytest.mark.django_db  # Позволяет работать с базой данных в тестах

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
# Task Filter Tests
# ========================

def test_task_filter_by_status(client):
    user = login(client)
    status1 = Status.objects.create(name='Статус1')
    status2 = Status.objects.create(name='Статус2')

    Task.objects.create(name='Task1', status=status1, author=user)
    Task.objects.create(name='Task2', status=status2, author=user)

    url = reverse('task-list') + f'?status={status1.id}'
    response = client.get(url)
    content = response.content.decode()
    assert response.status_code == 200
    assert 'Task1' in content
    assert 'Task2' not in content


def test_task_filter_by_executor(client):
    user = login(client)
    executor = create_user(username='executor')
    status = Status.objects.create(name='Статус')

    Task.objects.create(name='Task1', status=status, author=user, executor=executor)
    Task.objects.create(name='Task2', status=status, author=user)

    url = reverse('task-list') + f'?executor={executor.id}'
    response = client.get(url)
    content = response.content.decode()
    assert response.status_code == 200
    assert 'Task1' in content
    assert 'Task2' not in content


def test_task_filter_by_label(client):
    user = login(client)
    status = Status.objects.create(name='Статус')
    label1 = Label.objects.create(name='Баг')
    label2 = Label.objects.create(name='Фича')

    task1 = Task.objects.create(name='Task1', status=status, author=user)
    task1.labels.add(label1)
    task2 = Task.objects.create(name='Task2', status=status, author=user)
    task2.labels.add(label2)

    url = reverse('task-list') + f'?labels={label1.id}'
    response = client.get(url)
    content = response.content.decode()
    assert 'Task1' in content
    assert 'Task2' not in content


def test_task_filter_only_mine(client):
    user1 = login(client)
    user2 = create_user(username='other')
    status = Status.objects.create(name='Статус')

    Task.objects.create(name='MyTask', status=status, author=user1)
    Task.objects.create(name='OtherTask', status=status, author=user2)

    url = reverse('task-list') + '?only_mine=on'
    response = client.get(url)
    content = response.content.decode()
    assert 'MyTask' in content
    assert 'OtherTask' not in content  # тут все верно
