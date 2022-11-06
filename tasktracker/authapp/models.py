from django.db import models
from django.contrib.auth.models import AbstractUser


class TaskUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст', null=True, blank=True)
