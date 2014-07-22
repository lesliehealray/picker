from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^$', 'rep.views.index', name='index'),
	url(r'^songs/$', 'rep.views.list_songs', name='list_songs'),
    url(r'^songs/(?P<slug>[^\.]+)/$', 
        'rep.views.song_detail',
        name='song_detail'),
    url(r'^program/$', 'rep.views.list_programs', name='list_programs'),
    url(r'^program/(?P<slug>[^\.]+)/$',
    	'rep.views.program_detail',
    	name='program_detail'),
 )
