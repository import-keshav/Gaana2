from .models import Music, MusicsOfArtist
from . import services
from . import constants

from django.shortcuts import render
from django.http import JsonResponse


def home(request):
	musics_in_dict = {}
	data_to_send = {}
	user_dict = {}
	musics = Music.objects.all()
	for music in musics:
		music_dict = services.convert_music_object_to_dict(music)
		musics_in_dict[music.id] = music_dict

	data_to_send['musics'] = musics_in_dict
	data_to_send['languages'] = constants.languages_of_song

	if 'username' in request.session:
		data_to_send['user_logged_in'] = True

	return render(request, 'home.html', data_to_send)


def song(request, song_id):
	music = Music.objects.get(id=song_id)
	music_dict = services.convert_music_object_to_dict(music)

	return render(request, 'song/song.html', {'music_info': music_dict})
	# return JsonResponse({'music_info': music_dict})


def artist(request, artist_name):
	musics = []
	musics_of_artist = MusicsOfArtist.objects.filter(artist_name=artist_name)
	for music in musics_of_artist:
		music_dict = services.get_music_from_music_id(music.music_id)
		musics.append(music_dict)

	return JsonResponse({'musics': musics})