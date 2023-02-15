from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Theres nothing in your bag at present")
        return redirect(reverse('membership_options'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MXpnoIu94X7WsTedWBojclRuMerlwKpdOouNeaLcSf4YSQczJxcgHyYgDAy0lmydVgBTNP2OdvZSHexjAN6rxgh00bGhJsv0e',
        'client_secret_key': 'test client secret',
    }

    return render(request, template, context)