from django.shortcuts import render

def browse_songs_home(request):
	return render(request, 'browse/browse_songs_home.html')