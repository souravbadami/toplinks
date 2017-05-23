#!usr/bin/env python
from __future__ import unicode_literals
from django.db import models

class tweets(models.Model):
    timestamp = models.CharField(max_length=100)
    tweet = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)