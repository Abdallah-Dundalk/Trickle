from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from . models import Song, Playlist
from profiles.models import UserProfile
from membership_options.models import MembershipOptions
from . forms import AddSongForm, AddPlaylistForm, AddSongToPlayListForm
from django.contrib import messages
from datetime import datetime, timedelta
from django.contrib.auth.models import Group
from django.db.models import Q
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required


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
    membership_options = MembershipOptions.objects.all().order_by('pk').values()

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
        'membership_options': membership_options,
    }

    return render(request, 'home/index.html', context)

@login_required
def get_play_song_page(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    context = {
        "song": song
    }

    return render(request, 'home/play_song.html', context)

@login_required
def add_music(request):
    if request.method == 'POST':
        form = AddSongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("form saved")
            messages.success(request, 'Music successfully added')
            return redirect('add_music')
        else:
            messages.error(request, 'Failed to add song. Please ensure the \
                           form is valid before submitting')
            print('failed')
    else:
        form = AddSongForm()

    context = {
        'form': form
    }

    return render(request, 'home/add_music.html', context)


@login_required
def playlists(request):
    playlists = Playlist.objects.all().filter(user=request.user)
    template = 'home/playlists.html'
    context = {
        "playlists": playlists
    }

    return render(request, template, context)

@login_required
def playlist_songs(request, playlist_id):
    playlist_songs = Song.objects.all().filter(playlist=playlist_id)
    template = 'home/playlist_songs.html'
    context = {
        "playlist_songs": playlist_songs
    }

    return render(request, template, context)

@login_required
def edit_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    template = 'home/edit_playlist.html'
    if request.method == 'POST':
        form = AddPlaylistForm(request.POST, instance=playlist)
        print("start")
        if form.is_valid():
            form.save()
            print("saved")
            messages.success(request, 'Play list updated...')
            return redirect('playlists')
    form = AddPlaylistForm(instance=playlist)
    context = {
        'form': form,
        'playlist': playlist,
    }
    return render(request, template, context)

@login_required
def delete_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    if request.method == 'POST' and 'delete-btn' in request.POST:
        playlist.delete()
        print("deleted")
        messages.success(request, 'Playlist deleted.')
        return redirect('playlists')
    elif request.method == 'POST' and 'cancel-btn' in request.POST:
        print("cancelled")
        messages.success(request, 'Playlist not deleted.')
        return redirect('playlists')
    form = AddPlaylistForm(instance=playlist)
    context = {
        'playlist': playlist
    }
    return render(request, 'home/delete_playlist.html', context)

@login_required
def add_playlist(request):

    template = 'home/add_playlist.html'
    if request.method == 'POST':
        form = AddPlaylistForm(request.POST)
        print("start")
        if form.is_valid():
            new_form = form.save(commit=False)
            # Attach the user's profile to the order
            new_form.user = request.user
            print(new_form.user)
            new_form.save()
            print("saved")
            messages.success(request, 'Play list created...')
            return redirect('/playlists')
    form = AddPlaylistForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required
def add_song_to_playlist(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    template = 'home/add_song_to_playlist.html'
    if request.method == 'POST':
        form = AddSongToPlayListForm(request.POST, instance=song)
        print("start")
        if form.is_valid():
            form.save()
            print("saved")
            messages.success(request,  "Song added to playlist...")
            return redirect('home')
    form = AddSongToPlayListForm(instance=song)
    context = {
        'form': form,
        'song': song,
    }
    return render(request, template, context)
