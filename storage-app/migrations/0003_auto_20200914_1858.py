# Generated by Django 3.1.1 on 2020-09-14 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage-app', '0002_auto_20200903_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadfilesmodel',
            options={'ordering': ['-title'], 'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AddField(
            model_name='uploadfilesmodel',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.customuser', verbose_name='Пользователь загрузивший файл'),
            preserve_default=False,
        ),
    ]
