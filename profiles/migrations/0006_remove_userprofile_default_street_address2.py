# Generated by Django 3.2.16 on 2023-02-21 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_street_address2',
        ),
    ]
