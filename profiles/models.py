from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    default_full_name = models.CharField(max_length=50, null=True,
                                         blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_country = CountryField(blank_label='Country *',
                                   blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    subscription_expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def subscription_check(self):
        if self.subscription_expiration_date < datetime.now().date():
            group = Group.objects.get(name='subscribed')
            user = request.user
            user.groups.remove(group)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # If user already exists, save the profile
    instance.user_profile.save()
