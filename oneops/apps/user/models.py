from django.db import models
from django.contrib.auth.models import AbstractUser


class Menu(models.Model):
    name = models.CharField(max_length=64)
    path = models.CharField(max_length=64)
    parent = models.ForeignKey(
        'self',
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )


class Role(models.Model):
    name = models.CharField(max_length=64)
    menus = models.ManyToManyField(Menu)


class User(AbstractUser):
    token_version = models.SmallIntegerField(default=1)
    retry_count = models.SmallIntegerField(default=5)
    roles = models.ManyToManyField(Role)
