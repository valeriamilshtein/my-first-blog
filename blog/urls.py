from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    # url(r'^deletePost/(?P<slug>[w-]+)/$', views.post_remove, name='post_remove_by_slug'),
    # url(r'^deletePost/(?P<id>[0-9]+)/$', views.post_remove, name='post_remove_by_id'),
]
