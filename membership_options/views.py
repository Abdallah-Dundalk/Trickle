from django.shortcuts import render, get_object_or_404
from . models import MembershipOptions

# Create your views here.


def membership_options(request):
    membership_options = MembershipOptions.objects.all().order_by('pk').values()

    template = 'membership_options/membership_options.html'

    context = {
        'membership_options': membership_options,
    }

    return render(request, template, context)
