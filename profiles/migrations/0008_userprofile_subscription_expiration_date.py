# Generated by Django 3.2.16 on 2023-02-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_remove_userprofile_subscription_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subscription_expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
