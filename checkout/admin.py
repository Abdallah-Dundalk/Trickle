from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'order_total')

    fields = ('order_number', 'date', 'full_name', 'email',
              'phone_number', 'country',
              'town_or_city', 'street_address1', 'street_address2',
              'order_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
