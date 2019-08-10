from django.contrib import admin
from .models import Music, MusicsOfArtist

# Register your models here.

admin.site.register(Music)
admin.site.register(MusicsOfArtist)