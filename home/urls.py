from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='home'),
    path('playlists/', views.playlists, name='playlists'),
    path('playlist_songs/<int:playlist_id>/', views.playlist_songs, name='playlist_songs'),
    path('edit_playlist/<int:playlist_id>/', views.edit_playlist, name='edit_playlist'),
    path('add_playlist/', views.add_playlist, name='add_playlist'),
    path('add_song_to_playlist/<int:song_id>/', views.add_song_to_playlist, name='add_song_to_playlist'),
]
