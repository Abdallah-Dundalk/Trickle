# Register your models here.
from django.contrib import admin
from . models import Song, Playlist


admin.site.register(Song)
admin.site.register(Playlist)
