import twitter
import json
from datetime import datetime
import time
from config import *

def oauth_login():
    CONSUMER_KEY = SOCIAL_AUTH_TWITTER_KEY
    CONSUMER_SECRET = SOCIAL_AUTH_TWITTER_SECRET
    OAUTH_TOKEN = SOCIAL_OAUTH_TWITTER_TOKEN
    OAUTH_TOKEN_SECRET = SOCIAL_OAUTH_TWITTER_TOKEN_SECRET
    auth = twitter.oauth.OAuth( OAUTH_TOKEN,
                                OAUTH_TOKEN_SECRET,
                                CONSUMER_KEY,
                                CONSUMER_SECRET )
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def getTweets(username):
    twitter_api = oauth_login()
    statuses = twitter_api.statuses.home_timeline(screen_name=username, count=1000)
    return statuses
