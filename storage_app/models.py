from django.db import models
from users.models import CustomUser


class UploadFilesModel(models.Model):
    number = models.IntegerField(blank=True, default=0, verbose_name='Номер дела')
    title = models.CharField(max_length=50, blank=False, verbose_name='Тема вопроса')
    comment = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Описание')
    file = models.FileField(upload_to='media/files/%Y/%m/%d/', blank=False, verbose_name='Файлы')
    sum = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0.00, verbose_name='Объявленная цена')
    uploader = models.ForeignKey(CustomUser,
                                 on_delete=models.CASCADE,
                                 verbose_name='Пользователь загрузивший файл',
                                 blank=False,
                                 null=False
                                 )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-title']
