from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, blank=False, verbose_name='Название отдела')
