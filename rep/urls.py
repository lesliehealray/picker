from django.conf.urls import patterns, include, url

from rep.views import index, detail

urlpatterns = patterns('',
	url(r'^$', 'rep.views.index', name='index'),
)