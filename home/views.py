from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from . models import Song
from profiles.models import UserProfile
from . forms import AddSongForm
from django.contrib import messages
from datetime import datetime, timedelta
from django.contrib.auth.models import Group
from django.db.models import Q

# def index(request):
#     """ A view to return the index page"""
#     paginator = Paginator(Song.objects.all(), 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {"page_obj": page_obj}
#     return render(request, 'home/index.html', context)


def index(request):
    """A view to return all songs on index page"""
    songs = Song.objects.all()
    query = None

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)    
        if profile.subscription_expiration_date is None:
            group = Group.objects.get(name='subscribed')
            user = request.user
            user.groups.remove(group)
        elif profile.subscription_expiration_date < datetime.now().date():
            group = Group.objects.get(name='subscribed')
            user = request.user
            user.groups.remove(group)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search term...")
                return (redirect('home'))
            queries = Q(title__icontains=query) | Q(artist__icontains=query)
            songs = songs.filter(queries)

    context = {
        'songs': songs,
        'search_term': query,
    }

    return render(request, 'home/index.html', context)


def get_play_song_page(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    context = {
        "song": song
    }

    return render(request, 'home/play_song.html', context)


def add_music(request):
    if request.method == 'POST':
        form = AddSongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("form saved")
            messages.success(request, 'Music successfully added')
            return redirect('add_music')
        else:
            messages.error(request, 'Failed to add song. Please ensure the form is valid before submitting')
            print('failed')
    else:
        form = AddSongForm()

    context = {
        'form': form
    }

    return render(request, 'home/add_music.html', context)
