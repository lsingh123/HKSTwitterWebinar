#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:26:10 2019

@author: lavanyasingh
"""

from twitter import *
from credentials import consumer_key, consumer_secret, access_token_key, access_token_secret

def search(keyword):
    text = []
    t = Twitter(auth=OAuth(access_token_key, access_token_secret, 
                           consumer_key, consumer_secret))
    search_results = t.search.tweets(q = keyword)
    tweets = search_results['statuses']
    for tweet in tweets:
        text.append(tweet['text'])
    return text

#result = search("trump")
#print(result)

def search2(keyword):
    t = Twitter(auth=OAuth(access_token_key, access_token_secret, 
                           consumer_key, consumer_secret))
    search_results = t.search.tweets(q = keyword)
    text = [tweet['text'] for tweet in search_results['statuses']]
    return text

result = search2("trump")
print(result)