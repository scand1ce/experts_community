from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage-app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFilesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='Номер дела')),
                ('title', models.CharField(max_length=50, verbose_name='Тема вопроса')),
                ('comment', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('file', models.FileField(upload_to='media/files/%Y/%m/%d/', verbose_name='Файлы')),
                ('sum', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, verbose_name='Объявленная цена')),
            ],
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]
