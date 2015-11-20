from django.conf.urls import include, url, patterns
from django.contrib import admin
from bab import views

urlpatterns = patterns('',
   url(r'^$', views.restaurant, name = 'restaurant'),
   url(r'^(?P<bab_id>\d+)/$', views.detail, name = 'detail'),
   url(r'^point/(?P<bab_id>\d+)/$', views.point, name = 'point'),
)