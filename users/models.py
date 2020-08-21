from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, blank=False, verbose_name='Название отдела')
    first_name = models.CharField(max_length=50, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Фамилия')
    is_superuser = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=False, verbose_name='Активировать')
    userfield = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        null=True,
    )
    body = models.TextField()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('admin_page', args=[str(self.id)])

