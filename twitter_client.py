import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    
    try:
        consumer_key="RC2Kl8eVrzz1wEd7vIJLKbPWX"
        consumer_secret="9TC1hx6wdJLvfss5AW8NF8I6TmIuchHS9rXmt2752iaStKSHeH"
        access_token="956451552633397248-Xc3E5KMwUOBe7I2fHisHLYUnnDmiFuS"
        access_secret="7o7xZmNobDfeNWq0x8PSlIOwvyWpRQJSsZtAzZKAO99Hl"
    except KeyError:
        print("error in twitter key's ...")
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth


def get_twitter_client():
    
    auth=get_twitter_auth()
    client=API(auth)
    return client