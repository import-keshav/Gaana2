from django.contrib import admin
from .models import Music, MusicsOfArtist, Queue

# Registering models for admin panel
admin.site.register(Music)
admin.site.register(MusicsOfArtist)
admin.site.register(Queue)
