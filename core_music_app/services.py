from .models import Music, MusicsOfArtist, Queue
from django.contrib.auth.models import User, auth


def get_artist_of_music(music_id):
	artists_list = []
	artists = MusicsOfArtist.objects.filter(music_id=music_id)
	for artist in artists:
		artists_list.append(artist.artist_name)

	return artists_list


def convert_music_object_to_dict(music_object):
	music_dict = {}
	music_dict['id'] = music_object.id
	music_dict['title'] = music_object.title
	music_dict['audio'] = music_object.audio.url   # Media files cant add in json, so we add url of media file in json
	music_dict['lyrics'] = music_object.lyrics
	music_dict['lyricst'] = music_object.lyricst
	music_dict['release_date'] = music_object.release_date
	music_dict['image'] = music_object.image.url
	music_dict['music_company'] = music_object.music_company
	music_dict['language'] = music_object.language
	music_dict['genre'] = music_object.genre
	music_dict['artists'] = get_artist_of_music(music_object.id)

	return music_dict


def get_music_of(category):
	musics_in_dict = {}
	if category == 'Home':
		musics = Music.objects.all()
		for music in musics:
			music_dict = convert_music_object_to_dict(music)
			musics_in_dict[music.id] = music_dict
		return musics_in_dict


def get_music_from_music_id(music_id):
	music = Music.objects.get(id=music_id)
	music_dict = convert_music_object_to_dict(music)

	return music_dict


def get_queue_list_of_user(user_id):
	music_queue = []
	musics_id = Queue.objects.filter(user_id=user_id)
	for music_id in musics_id:
		music = Music.objects.get(id=music_id.music_id)
		music_dict = convert_music_object_to_dict(music)
		music_dict['id'] = music.id
		music_queue.append(music_dict)

	return music_queue

def add_song_in_queue(song_id, user_id):
	music = Music.objects.get(id=song_id)
	if Queue.objects.filter(music_id=song_id).exists():
		return False
	next_song_in_queue = Queue(music_id=music.id, user_id=user_id)
	next_song_in_queue.save()

	return True

def get_user_id_from_username(username):
	user = User.objects.get(username=username)
	return user.id
