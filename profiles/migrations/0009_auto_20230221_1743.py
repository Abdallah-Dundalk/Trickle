# Generated by Django 3.2.16 on 2023-02-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_userprofile_subscription_expiration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='subscription_expiration_date',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]