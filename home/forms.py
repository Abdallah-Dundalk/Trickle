from django import forms
from .models import Song


class AddSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

        labels = {
            'title': 'Title',
            'artist': 'Artist',
            'image': 'Image',
            'duration': 'Duration',
            'audio_file': 'Audio File',
            'audio_link': 'Audio Link',
        }
