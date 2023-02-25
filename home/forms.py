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
    # def __init__(self, user=None, *args, **kwargs):  # note the additional user param
    #     self.playlists = Playlist.objects.filter(user=user)
    #     super(AddSongToPlayListForm, self).__init__(*args, **kwargs)
    #     self.fields['playlist'].queryset = self.playlists
    #     if user:
    #         print('wooooooooo')
    #         self.fields['playlist'].queryset = Playlist.objects.filter(user=self.request.user)
    #     else:
    #         print(user)

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
