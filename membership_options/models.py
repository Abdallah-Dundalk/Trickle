from django.db import models

# Create your models here.


class MembershipOptions(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Membership Options'

    def __str__(self):
        return self.name
