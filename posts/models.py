from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименования')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Публикация')
    photo = models.ImageField(upload_to='media/photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Состояние')

    def __str__(self):
        return self.title
