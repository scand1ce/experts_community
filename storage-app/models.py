from django.db import models
from django.urls import reverse


class UploadFileModel(models.Model):
    number = models.IntegerField(blank=True, default=0, verbose_name='Номер дела')
    title = models.CharField(max_length=50, blank=False, verbose_name='Тема вопроаса')
    comment = models.CharField(max_length=2000, blank=True, verbose_name='Описание')
    file = models.FileField(upload_to='media/files/%Y/%m/%d/', blank=False, verbose_name='Файлы')
    sum = models.IntegerField(blank=True, default=0, verbose_name='Объявленная цена')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': str(self.pk)})
