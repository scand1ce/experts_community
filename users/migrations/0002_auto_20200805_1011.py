# Generated by Django 3.0.8 on 2020-08-05 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='my_admin status'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='user status'),
        ),
    ]
