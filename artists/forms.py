#https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/

from django.forms import ModelForm
from .models import Song

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'spotify_published', 'youtube_published', 'artist']


form = SongForm()