from .models import Music, MusicsOfArtist
from . import services
from . import constants

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User, auth

def home(request):
	data_to_send = {}
	data_to_send['user_logged_in'] = False
	data_to_send['queue'] = 'Null'

	data_to_send['musics'] = services.get_music_of('Home')
	data_to_send['languages'] = constants.languages_of_song

	if request.session.get('username'):
		data_to_send['user_logged_in'] = True
		user = User.objects.get(username=request.session['username'])
		data_to_send['queue'] = services.get_queue_list_of_user(user.id)

	return render(request, 'home.html', data_to_send)


def song(request, song_id):
	music = Music.objects.get(id=song_id)
	music_dict = services.convert_music_object_to_dict(music)

	user = User.objects.get(username=request.session['username'])	
	queue = services.get_queue_list_of_user(user.id)

	return render(request, 'song/song.html', {'music_info': music_dict, 'queue': queue})


def artist(request, artist_name):
	musics = []
	musics_of_artist = MusicsOfArtist.objects.filter(artist_name=artist_name)
	for music in musics_of_artist:
		music_dict = services.get_music_from_music_id(music.music_id)
		musics.append(music_dict)

	return JsonResponse({'musics': musics})

def addSongInQueue(request):
	if request.session['username']:
		song_id = request.POST['song_id']
		user_id = services.get_user_id_from_username(request.session['username'])
		if services.add_song_in_queue(song_id, user_id):
			music = services.get_music_from_music_id(song_id)
			return JsonResponse({'is_added': True, 'message': 'Song added suceesfully', 'music': music})
		return JsonResponse({'is_added': False, 'message': 'Song already in Queue'})

