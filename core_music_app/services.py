from .models import Music, MusicsOfArtist


def get_artist_of_music(music_id):
	artists_list = []
	artists = MusicsOfArtist.objects.filter(music_id=music_id)
	for artist in artists:
		artists_list.append(artist.artist_name)

	return artists_list


def convert_music_object_to_dict(music_object):
	music_dict = {}
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


def get_music_from_music_id(music_id):
	music = Music.objects.get(id=music_id)
	music_dict = convert_music_object_to_dict(music)

	return music_dict