# Generated by Django 3.2.16 on 2023-02-04 23:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='video'),
        ),
    ]
