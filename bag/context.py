def bag_contents(request):

    bag_items = []
    order_total = 0

    context = {
        'bag_items': bag_items,
        'order_total': order_total,
    }

    return context