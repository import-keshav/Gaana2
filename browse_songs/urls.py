from django.urls import path
from . import views

urlpatterns = [
	path('', views.browse_songs_home, name='browse_songs_home'),
]
