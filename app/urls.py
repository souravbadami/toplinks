#!usr/bin/env python
from django.conf.urls import url, include
from app import views

urlpatterns = [
    url(r'^$', views.home, name='home_view'),
    url(r'^logout/$', views.processLogout, name='logout'),
    url(r'^app/$', views.app, name='app_view'),
    url(r'^fetch/$', views.fetchTweets, name='fetch_tweets'),
]