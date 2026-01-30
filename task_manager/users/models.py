from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.get_full_name()
