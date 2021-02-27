from django.db import models

# cria model Artist
class Artist(models.Model):
    name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# cria model Song
class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.BigIntegerField()
    spotify_published = models.BooleanField()
    youtube_published = models.BooleanField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=0, related_name='Artist', null=True)


    def __str__(self):
        return f'{self.title} - {self.artist}'
