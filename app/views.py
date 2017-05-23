#!/usr/bin/env python
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from app.fetch import *
from datetime import datetime
import time
from app.models import tweets
import operator
from django.db.models import Count, Avg

since = 7 # In Days

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def home(request):
    if request.user.is_authenticated():
        return redirect('app_view')
    return TemplateResponse(request, 'default/home.html',)

@login_required(login_url="/")
def processLogout(request):
    logout(request)
    return redirect('home_view')
    
@login_required(login_url="/")
def app(request):
    alltweets = tweets.objects.filter(username=request.user.username)
    allpopularusers = tweets.objects.filter(username=request.user.username).values('author').annotate(the_count=Count('author')).order_by('-the_count')
    allpopulardomains = tweets.objects.filter(username=request.user.username).values('domain').annotate(the_count=Count('domain')).order_by('-the_count')
    return TemplateResponse(request, 'default/app.html', {
        'alltweets': alltweets, 
        'allpopularusers': allpopularusers, 
        'allpopulardomains': allpopulardomains})
        
@login_required(login_url="/")
def fetchTweets(request):
    statuses = getTweets(request.user.username)
    for status in statuses:
        tt = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(status['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
        ct = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if(days_between(tt[:10], ct[:10]) <= since):
            try:
                r = tweets(
                    timestamp=status['created_at'],
                    tweet=status['text'].encode('utf-8'),
                    username=request.user.username,
                    author=status['user']['screen_name'],
                    domain=status['entities']['urls'][0]['expanded_url'])
                r.save()
            except:
                pass
    alltweets = tweets.objects.filter(username=request.user.username)
    allpopularusers = tweets.objects.filter(username=request.user.username).values('author').annotate(the_count=Count('author')).order_by('-the_count')
    allpopulardomains = tweets.objects.filter(username=request.user.username).values('domain').annotate(the_count=Count('domain')).order_by('-the_count')
    return TemplateResponse(request, 'default/app.html', {
        'alltweets': alltweets, 
        'allpopularusers': allpopularusers, 
        'allpopulardomains': allpopulardomains})