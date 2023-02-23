from django import forms
from .models import Song, Playlist


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
            'paginate_by': 'Paginate by',
            'playlist': 'Playlist',
        }


class AddSongToPlayListForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['playlist']

        labels = {
            'playlist': 'Playlist',
        }


class AddPlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['playlist_name']

        labels = {
            'playlist_name': 'Playlist Name',
            'user': 'User',
        }