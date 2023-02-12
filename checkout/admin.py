from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['date', 'order_number', 'order_total']

    fields = ('order_number','date', 'full_name', 'email', 'phone_number',
              'country', 'street_address1', 'street_address2',
              'order_total',)

    list_display = ('order_number', 'full_name', 'email',
                    'order_total', 'date')

    ordering = ('-date',)



