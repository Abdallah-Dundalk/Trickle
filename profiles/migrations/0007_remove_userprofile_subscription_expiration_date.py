# Generated by Django 3.2.16 on 2023-02-21 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_remove_userprofile_default_street_address2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='subscription_expiration_date',
        ),
    ]