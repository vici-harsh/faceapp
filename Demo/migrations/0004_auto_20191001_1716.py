# Generated by Django 2.2.6 on 2019-10-01 11:46

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0003_auto_20191001_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='content_image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='images',
            name='output_image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='images',
            name='style_image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
    ]
