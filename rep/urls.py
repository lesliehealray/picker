from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^$', 'rep.views.index', name='index'),
	url(r'^songs/$', 'rep.views.list_songs', name='list_songs'),
    url(r'^songs/(?P<slug>[^\.]+)/$', 
        'rep.views.song_detail',
        name='song_detail'),
 )
