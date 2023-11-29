# Generated by Django 4.2.7 on 2023-11-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название страницы')),
                ('name', models.CharField(max_length=20, verbose_name='Название (фильма / сериала)')),
                ('image_film', models.ImageField(upload_to='static/main/image', verbose_name='Изображение обложки фильма')),
                ('age', models.DateField(verbose_name='Дата выпуска')),
                ('genre', models.CharField(max_length=20, verbose_name='Жанр')),
                ('country', models.CharField(max_length=20, verbose_name='Страна')),
                ('director', models.CharField(max_length=20, verbose_name='Режисер')),
                ('cast', models.CharField(max_length=90, verbose_name='В ролях')),
                ('description', models.TextField(max_length=537, verbose_name='Описание')),
                ('trailer', models.FileField(upload_to='videos/', verbose_name='Видеофайл')),
                ('video_file', models.FileField(upload_to='videos/', verbose_name='Видеофайл')),
            ],
        ),
    ]