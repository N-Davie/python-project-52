from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import AppUser
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from .models import Task


class TestCreateUpdateDeleteTask(TestCase):
    def setUp(self):

        self.data1 = {
                      'first_name': 'First_name1',
                      'last_name': 'Last_name1',
                      'username': 'test_username1',
                      'password': 'password1',
                     }
        self.data2 = {
                      'first_name': 'First_name2',
                      'last_name': 'Last_name2',
                      'username': 'test_username2',
                      'password': 'password2',
                      }

        self.user = AppUser.objects.create_user(**self.data1)
        AppUser.objects.create_user(**self.data2)
        Label.objects.create(name='Test_label1')
        Label.objects.create(name='Test_label2')
        Status.objects.create(name='Test_status1')
        Status.objects.create(name='Test_status2')
        self.client.force_login(self.user)
        self.status = Status.objects.get(name='Test_status1')
        self.executor = AppUser.objects.get(username='test_username1')

        self.task_data = {
                     'name': 'Test_task',
                     'description': 'test_description',
                     'status': self.status,
                     'executor': self.executor,
                     'author': self.user,
                     }

    def test_create_task(self):

        response = self.client.post(reverse('task_create'),
                                    data={
                                          'name': 'Test_task',
                                          'description': 'test_description',
                                          'status': 1,
                                          'executor': 1,
                                          })
        self.assertEqual(response.status_code, 302)

    def test_update_task_form(self):

        Task.objects.create(**self.task_data)
        id = Task.objects.get(name='Test_task').pk
        response = self.client.post(reverse('task_update', args=[id]),
                                    data={
                                          'name': 'Updated_test_task',
                                          'description': 'test_description',
                                          'status': 2,
                                          'executor': 2,
                                          })
        self.assertEqual(response.status_code, 302)

    def test_delete_task_user(self):

        Task.objects.create(**self.task_data)
        id = Task.objects.get(name='Test_task').pk
        response = self.client.post(reverse('task_delete', args=[id]))
        self.assertEqual(response.status_code, 302)
