from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from rep.models import Song, Program, Composer

def index(request):
	all_songs = Song.objects.all()
	context = {'all_songs': all_songs}
	return render(request, 'rep/index.html', context)

def detail(request, song_id):
	song_composer = get_object_or_404(Song, pk=composer_id)
	return render(request, 'rep/detail.html', {'composer' : composer}) 
	