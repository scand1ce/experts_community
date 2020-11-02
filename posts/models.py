from django.db import models
from users.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименования')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Публикация')
    photo = models.ImageField(upload_to='media/photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Состояние')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор поста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at', '-title']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', blank=False, null=False,
                             related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=False,
                               null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Публикация')
    comment_text = models.TextField(max_length=600, blank=True, verbose_name='Текст комментария')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-author', '-created_at']
