from django.conf.urls import url
from django.contrib import admin
from .views import (
	post_list,
	post_detail,
	post_create,
	post_update,
	post_delete,)

urlpatterns = [
	url(r'^$', post_list, name = "list"),
	#whats in url, view to return, name(optional), the name is essential tied to viewname.. detail = post_detail now
    url(r'^create$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name= "detail"),
    url(r'^(?P<id>\d+)/edit/$', post_update, name = "update"),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
    #url(r'nameinadressbarw/regex,'<appname>.views.functionname')
]
#after i did from .views import () i deleted the relative path and used the function directly as path
	#url(r'^$', 'posts.views.post_list'), 
    #url(r'^create$', 'posts.views.post_create'),
    #url(r'^detail$', 'posts.views.post_detail'),
    #url(r'^update$', 'posts.views.post_update'),
    #url(r'^delete$', 'posts.views.post_delete'),