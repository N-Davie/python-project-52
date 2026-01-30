from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import AppUser
from .models import Label


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

        response = self.client.post(reverse('label_create'),
                                    data={
                                          'name': 'Test_label',
                                          })
        self.assertEqual(response.status_code, 302)

    def test_update_status_form(self):
        Label.objects.create(name='test_label')
        id = Label.objects.get(name='test_label').pk
        response = self.client.post(reverse('label_update', args=[id]),
                                    data={
                                          'name': 'Updated_test_label',
                                          })
        self.assertEqual(response.status_code, 302)

    def test_delete_status_user(self):
        Label.objects.create(name='test_label')
        id = Label.objects.get(name='test_label').pk
        response = self.client.post(reverse('label_delete', args=[id]))
        self.assertEqual(response.status_code, 302)
