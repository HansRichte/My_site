# Generated by Django 4.2.7 on 2023-11-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles',
            name='trailer',
            field=models.FileField(upload_to='videos/', verbose_name='Трейлер'),
        ),
    ]
