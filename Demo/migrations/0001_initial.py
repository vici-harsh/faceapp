# Generated by Django 2.2.5 on 2019-10-01 07:33

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(default='')),
                ('content_image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
                ('style_image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
                ('output_image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
            ],
        ),
    ]
