from django.db import models
from django.contrib.auth.models import User

# твоя модель Status
class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# модель Task
class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='tasks'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='created_tasks'
    )

    executor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
