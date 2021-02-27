from django.contrib import admin
from .models import Song
from .models import Artist

#registra Songs e Artists através do Admin
admin.site.register(Song)
admin.site.register(Artist)


