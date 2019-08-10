from django.shortcuts import render
from .models import Music, MusicsOfArtist
from . import services
from . import constants

def home(request):
	musics_in_dict = {}
	data_to_send = {}
	musics = Music.objects.all()
	for music in musics:
		music_dict = services.convert_music_object_to_dict(music)
		musics_in_dict[music.id] = music_dict

	data_to_send['musics'] = musics_in_dict
	data_to_send['languages'] = constants.languages_of_song

	return render(request, 'home.html', data_to_send)