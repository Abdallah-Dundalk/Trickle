from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='home'),
    path('add_music', views.add_music_page, name='add_music_page'),
    path('play_song/<song_id>/', views.get_play_song_page, name='get_play_song_page'),

]
