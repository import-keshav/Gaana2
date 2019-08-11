from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('song/<int:song_id>', views.song, name='song'),
	path('artist/<str:artist_name>', views.artist, name='artist'),
	path('add_song_in_queue', views.addSongInQueue, name='add_song_in_queue')
]