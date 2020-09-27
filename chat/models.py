from django.db import models

from users.models import CustomUser


class Chat(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField(max_length=600, blank=True, verbose_name='Сообщение')
    time_sent = models.DateTimeField(auto_now_add=True)
