import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    
    try:
        consumer_key="XXXXX"
        consumer_secret="XXXXX"
        access_token="XXXXX"
        access_secret="XXXXXX"
    except KeyError:
        print("error in twitter key's ...")
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth


def get_twitter_client():
    
    auth=get_twitter_auth()
    client=API(auth)
    return client
