from django.db import models

# Create your models here.

class MusicsOfArtist(models.Model):
	music_id = models.IntegerField()
	artist_name = models.CharField(max_length=100)


class Music(models.Model):
	title = models.CharField(max_length=100)
	audio = models.FileField(upload_to='musics')
	lyrics = models.TextField()
	lyricst = models.CharField(max_length=100)
	image = models.ImageField(upload_to='pics')
	release_date = models.DateField()
	music_company = models.CharField(max_length=300)
	language = models.CharField(max_length=20)
	genre = models.CharField(max_length=50)
