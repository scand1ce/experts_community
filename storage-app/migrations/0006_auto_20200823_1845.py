# Generated by Django 3.1 on 2020-08-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage-app', '0005_auto_20200823_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.FileField(upload_to='media/files/%Y/%m/%d/', verbose_name='Файлы'),
        ),
    ]
