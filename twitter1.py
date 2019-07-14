#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:01:37 2019

@author: lavanyasingh
"""

from twitter import *
from credentials import consumer_key, consumer_secret, access_token_key, access_token_secret

def search():
    t = Twitter(auth=OAuth(access_token_key, access_token_secret, 
                           consumer_key, consumer_secret))
    search_results = t.search.tweets(q = "trump")
    return search_results

s = search()
for key in s:
    print(key)
statuses = s['statuses']
print(statuses[0])
for key in statuses[0]:
    print(key)
print(statuses[0]['text'])