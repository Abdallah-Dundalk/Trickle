# Generated by Django 3.2.16 on 2023-02-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20230206_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='playlists',
            field=models.ManyToManyField(to='home.Playlist'),
        ),
    ]
