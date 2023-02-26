from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from membership_options.models import MembershipOptions


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    order_total = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            membership_option = get_object_or_404(MembershipOptions,
                                                  pk=item_id)
            total += item_data * membership_option.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'membership_option': membership_option,
            })

    order_total = total

    context = {
        'bag_items': bag_items,
        'order_total': order_total,
        'product_count': product_count,
    }

    return context
