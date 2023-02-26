"""trickle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('index', views.index, name='home'),
    path('play_song/<song_id>/', views.get_play_song_page,
         name='get_play_song_page'),
    path('add/', views.add_music, name='add_music'),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('bag/', include('bag.urls')),
    path('membership_options/', include('membership_options.urls')),
    path('playlists/', views.playlists, name='playlists'),
    path('playlist_songs/<int:playlist_id>/', views.playlist_songs, name='playlist_songs'),
    path('edit_playlist/<int:playlist_id>/', views.edit_playlist, name='edit_playlist'),
    path('delete_playlist/<int:playlist_id>/', views.delete_playlist, name='delete_playlist'),
    path('add_playlist/', views.add_playlist, name='add_playlist'),
    path('add_song_to_playlist/<int:song_id>/', views.add_song_to_playlist, name='add_song_to_playlist'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
