from django.shortcuts import render, redirect

# Create your views here.
from django.core.paginator import Paginator
from . models import Song

def index(request):
    """ A view to return the index page"""
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, 'home/index.html', context)
