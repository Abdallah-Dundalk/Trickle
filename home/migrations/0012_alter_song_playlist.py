# Generated by Django 3.2.16 on 2023-02-23 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_playlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.playlist'),
        ),
    ]
