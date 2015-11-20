from django.conf.urls import include, url, patterns
from django.contrib import admin
from board import views

urlpatterns = patterns('',
	url(r'^$', views.board, name = 'board'),
	url(r'^write/$', views.write, name = 'write'),
	url(r'^(?P<board_id>\d+)/$', views.view, name = 'view'),
	url(r'^write_board/', views.write_board, name = 'write_board'),
)
