#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:32:56 2019

@author: lavanyasingh
"""

from twitter import *
from credentials import consumer_key, consumer_secret, access_token_key, access_token_secret

def search(keyword):
    t = Twitter(auth=OAuth(access_token_key, access_token_secret, 
                           consumer_key, consumer_secret))
    search_results = t.search.tweets(q = keyword)
    text = [tweet['text'] for tweet in search_results['statuses']]
    return text

# rewriting our search function to search for a certain number of tweets
def search_while(keyword, c):
    t = Twitter(auth=OAuth(access_token_key, access_token_secret, 
                consumer_key, consumer_secret))
    search_results = t.search.tweets(q = keyword, count = 100)
    text = [tweet['text'] for tweet in search_results['statuses']]
    since_id = search_results['search_metadata']['since_id']
    while len(text) < c:
        # the max_id keyword ensures that we move backwards without overlap, 
        # pulling the most recent tweets first but not retrieving any duplicates
        search_results = t.search.tweets(q = keyword, count = 100, max_id = since_id)
        text += [tweet['text'] for tweet in search_results['statuses']]
        since_id = search_results['search_metadata']['since_id']
    return text[:150]


results = search_while("trump", 150)