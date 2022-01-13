import tweepy
import os
from dotenv import load_dotenv, find_dotenv
import time

load_dotenv(find_dotenv())

client = tweepy.Client(consumer_key=os.getenv("API_KEY"),
                       consumer_secret=os.getenv("API_KEY_SECRET"),
                       access_token=os.getenv("ACCESS_TOKEN"),
                       access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
                       bearer_token=os.getenv("BEARER_TOKEN"))

query = '#localhackday -is:retweet'

response = client.search_recent_tweets(query=query, max_results=50)

for tweet in response.data:
    retweet = client.retweet(tweet_id=f'{tweet.id}')
    print("Retweeted")
    like = client.like(tweet_id=f'{tweet.id}')
    print("Liked")
    time.sleep(1)

