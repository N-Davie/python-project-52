from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import AppUser
from .models import Status


class TestCreateUpdateDeleteStatus(TestCase):
    def setUp(self):
        self.data = {
                     'first_name': 'First_name',
                     'last_name': 'Last_name',
                     'username': 'test_username',
                     'password': 'password',
                    }
        self.user = AppUser.objects.create_user(**self.data)
        self.client.force_login(self.user)

    def test_create_status(self):
        response = self.client.post(reverse('status_create'),
                                    data={
                                          'name': 'Test_status',
                                          })
        self.assertEqual(response.status_code, 302)

    def test_update_status_form(self):
        Status.objects.create(name='Test_status')
        id = Status.objects.get(name='Test_status').pk
        response = self.client.post(reverse('status_update', args=[id]),
                                    data={
                                          'name': 'Updated_test_status',
                                          })
        self.assertEqual(response.status_code, 302)

    def test_delete_status_user(self):
        Status.objects.create(name='Test_status')
        id = Status.objects.get(name='Test_status').pk
        response = self.client.post(reverse('status_delete', args=[id]))
        self.assertEqual(response.status_code, 302)
