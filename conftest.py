# conftest.py
import pytest
from django.core.management import call_command

@pytest.fixture(scope="session", autouse=True)
def apply_migrations(django_db_setup, django_db_blocker):
    """Принудительно мигрируем тестовую БД перед тестами"""
    with django_db_blocker.unblock():
        print(">>> Applying migrations for tests")
        call_command("migrate")
