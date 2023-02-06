from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    audio_file = CloudinaryField(resource_type='')
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    paginate_by = 2

    def __str__(self):
        return self.title
