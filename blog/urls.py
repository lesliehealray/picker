from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', 'blog.views.blog_index', name='blog_index'),
    url(r'^(?P<slug>[^\.]+)/$', 
         'blog.views.view_post',
         name='blog_post'),
)

# url(
#     r'^blog/category/(?P<slug>[^\.]+).html', 
#     'djangorocks.blog.views.view_category', 
#     name='view_blog_category'),