# !/usr/bin/env python3

'''
Sentiment analysis using the twitter api.
DEFINITION:
Sentiment Analysis - Understanding and extracting
feelings from data.

GOAL 1: Collect tweets containing a certain keyword.
GOAL 2: Perform sentime analysis on the tweets.
GOAL 3: Return the tweets, and their sentiment to the users terminal.
'''

__author__ = "Michael Ketiku"
__project__ = "Sentiment Analysis"

from textblob import TextBlob
import tweepy


# Register to access twitter api

# Create an API at app.twitter.com and then fill in the values below. 

CONSUMER_KEY = 'XXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXX'

ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXX'

AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Variable to do twitter api magic

API = tweepy.API(AUTH)


def search_twitter(keyword: 'Hello' ):
    '''Search twitter using a given keyword '''
    public_tweets = API.search(keyword)  # Retrieves tweets matching keyword
    for tweet in public_tweets:
        print(tweet.text)  # Print the tweets text AttributeError
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)

search_twitter(input("Search Keyword: "))
