from django.conf.urls import url, include
from django.contrib import admin
from config import *

urlpatterns = [
    url(r'', include('app.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
