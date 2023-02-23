from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='home'),
    path('playlists', views.playlists, name='playlists'),
    path('playlist_songs/<int:playlist_id>', views.playlist_songs, name='playlist_songs')
]
