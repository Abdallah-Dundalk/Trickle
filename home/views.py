from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.core.paginator import Paginator
from . models import Song
from . forms import AddSongForm

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

    context = {
        'songs': songs,
    }

    return render(request, 'home/index.html', context)


def get_play_song_page(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    context = {
        "song": song
    }

    return render(request, 'home/play_song.html', context)


def add_music_page(request):
    if request.method == 'POST':
        form = AddSongForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            message.success(request, 'Mussic successfully added')

    form = AddSongForm()
    context = {
        'form': form
    }

    return render(request, 'home/add_music.html', context)
