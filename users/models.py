from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='media/profile/%Y/%m/%d/', verbose_name='Аватар', blank=True)
    department = models.CharField(max_length=50, blank=False, verbose_name='Название отдела')
    first_name = models.CharField(max_length=50, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Фамилия')
    is_superuser = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=False, verbose_name='Активировать')
    body = models.TextField()

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('admin_page', args=[str(self.pk)])

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
