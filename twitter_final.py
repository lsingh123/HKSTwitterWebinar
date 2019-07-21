#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:42:19 2019

@author: lavanyasingh
"""

# performing some simple sentiment analysis on tweets as an example of the 
# work that can be done using the Twitter API

from twitter import *
from credentials import consumer_key, consumer_secret, access_token_key, access_token_secret
import nltk
nltk.download('vader_lexicon')
from matplotlib import pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def search_while(keyword, c):
    t = Twitter(auth=OAuth(access_token_key, access_token_secret, 
                consumer_key, consumer_secret))
    search_results = t.search.tweets(q = keyword, count = 100)
    text = [tweet['text'] for tweet in search_results['statuses']]
    since_id = search_results['search_metadata']['since_id']
    while len(text) < c:
        search_results = t.search.tweets(q = keyword, count = 100, max_id = since_id)
        text += [tweet['text'] for tweet in search_results['statuses']]
        since_id = search_results['search_metadata']['since_id']
    return text[:150]

# returns a numerical score for a particular sentence
# a positive score indicates positive sentiment, a score of 0 indicates
# neutrality, and a negative score indicates negative sentiment
def nltk_sentiment(sentence):
    nltk_sentiment = SentimentIntensityAnalyzer()
    score = nltk_sentiment.polarity_scores(sentence)
    return score

def analyse(keyword, c):
    tweets = search_while(keyword, c)
    results = [nltk_sentiment(tweet) for tweet in tweets]
    res = [item['compound'] for item in results]
    final = zip(tweets, results)
    plt.hist(res)
    plt.title("sentiment analysis Scores")

analyse("trump", 150)
    


    
        
