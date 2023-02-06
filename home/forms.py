from django import forms
from .models import Song


class Add_song(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

        labels = {
            'title': 'Title',
            'artist': 'Artist',
            'image': 'Image',
            'duration': 'Duration',
        }