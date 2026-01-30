from django.test import TestCase, Client
from django.urls import reverse


from task_manager.users.models import AppUser


class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.first_name = 'First_name'
        self.last_name = 'Last_name'
        self.username = 'test_user'
        self.password = 'password',

    def test_signup_page_url(self):
        response = self.client.get("/users/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='form.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='form.html')

    def test_signup_form(self):
        response = self.client.post(reverse('signup'),
                                    data={
                                          'first_name': self.first_name,
                                          'last_name': self.last_name,
                                          'username': self.username,
                                          'password1': self.password,
                                          'password2': self.password,
                                          })
        self.assertEqual(response.status_code, 302)


class TestLoginLogout(TestCase):
    def setUp(self):
        self.client = Client()
        self.data = {
                     'first_name': 'First_name',
                     'last_name': 'Last_name',
                     'username': 'test_username',
                     'password': 'password',
                    }
        self.test_user = AppUser.objects.create_user(**self.data)

    def test_login_user(self):
        response = self.client.post(reverse('signin'),
                                    data={
                                          'username': self.data['username'],
                                          'password': self.data['password'],
                                         })
        self.assertEqual(response.status_code, 302)


class TestUpdateDeleteUser(TestCase):
    def setUp(self):
        self.data = {
                     'first_name': 'First_name',
                     'last_name': 'Last_name',
                     'username': 'test_username',
                     'password': 'password',
                     }
        self.user = AppUser.objects.create_user(**self.data)
        self.client.force_login(self.user)

    def test_update_form(self):
        response = self.client.post(reverse('update_user',
                                            args=[self.user.pk]), data={
            'first_name': 'Another_first_name',
            'last_name': 'Another_last_name',
            'username': 'another_username',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_user(self):
        response = self.client.post(reverse('delete_user',
                                            args=[self.user.pk]))
        self.assertEqual(response.status_code, 302)
