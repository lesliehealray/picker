from django.shortcuts import render_to_response, render, get_object_or_404

from rep.models import Song, Program, Composer

def index(request):
	return render(request, 'rep/index.html')

def list_songs(request,):
	return render_to_response('rep/list_songs.html', {
		'songs' : Song.objects.all()
	})


def song_detail(request, slug):
	return render_to_response('rep/song_detail.html', {
		'song' : get_object_or_404(Song, slug=slug)
	})

def list_programs(request,):
	return render_to_response('rep/list_programs.html', {
		'programs' : Program.objects.all()
	})

def program_detail(request, slug):
	return render_to_response('rep/program_detail.html', {
		'program_detail' : get_object_or_404(Program, slug=slug)
	})


