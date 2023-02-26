from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=50, blank=False,
                                     null=False, default='')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             blank=True, null=True)

    def __str__(self):
        return self.playlist_name


""" The below model is modified code by 
Onojakpor Ochuko and can be found here 
https://www.section.io/engineering-education/how-to-build-a-music-player-using-django/"""

class Song(models.Model):
    title = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    image = CloudinaryField('image', default='placeholder')
    audio_file = CloudinaryField(resource_type='')
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    paginate_by = 2
    playlist = models.ForeignKey(Playlist, null=True,
                                 blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title + " performed by " + self.artist
