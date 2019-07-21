#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:01:37 2019

@author: lavanyasingh
"""

# our first script: exploring the API search capabilities 

from twitter import *
from credentials import consumer_key, consumer_secret, access_token_key, access_token_secret

# a function to search for tweets containing the keyword "trump"
def search():
    t = Twitter(auth=OAuth(access_token_key, access_token_secret, 
                           consumer_key, consumer_secret))
    search_results = t.search.tweets(q = "trump")
    return search_results

# iterating over keys is a quick and easy way to investigate what information 
# a dictionary contains
s = search()
for key in s:
    print(key)
statuses = s['statuses']
print(statuses[0])
for key in statuses[0]:
    print(key)
print(statuses[0]['text'])