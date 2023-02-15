from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from membership_options.models import MembershipOptions


def bag_contents(request):

    bag_items = []
    order_total = 0
    bag = request.session.get('bag', {})

    context = {
        'bag_items': bag_items,
        'order_total': order_total,
    }

    return context