# Generated by Django 3.2.16 on 2023-02-23 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_song_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='playlist_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
