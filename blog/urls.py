from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
  	url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
=======
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
>>>>>>> b5faffc96a8204c4b541e943a7a6052b4cfb40a0
]