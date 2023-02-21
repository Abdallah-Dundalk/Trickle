from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
# from checkout.models import Order

# Create your views here.


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    # pk = request.user.id
    # order = get_object_or_404(Order, pk=1)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        # 'order': order
    }

    return render(request, template, context)