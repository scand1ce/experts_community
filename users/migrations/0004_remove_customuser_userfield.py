# Generated by Django 3.1 on 2020-08-23 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200821_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='userfield',
        ),
    ]
