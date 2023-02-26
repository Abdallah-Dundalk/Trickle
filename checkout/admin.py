from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('date', 'order_number', 'order_total', 'original_bag',
                       'stripe_pid', 'user_profile',)

    fields = ('order_number', 'date', 'full_name', 'user_profile',
              'email', 'phone_number', 'country', 'town_or_city',
              'street_address1', 'street_address2', 'order_total',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'full_name', 'email',
                    'order_total', 'date')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
