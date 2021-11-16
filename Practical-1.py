import tweepy
import pandas as pd
import numpy as np
import twitter_credentials

hash_tag = ''
num_tweets = 100

def getHashtag():
    global hash_tag
    hash_tag = input('Enter hashtag to search : ')

def authenticateTwitterAPI():
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    return auth

def fetchTweets(api):
    t = []
    tweets = api.search_tweets(q=hash_tag, count=100)
    for tweet in tweets:
        if 'RT' not in tweet.text:
            t.append(tweet)
    return t

def tweets_to_data_frame(tweets):
    df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        
    df['date'] = np.array([tweet.created_at for tweet in tweets])
    df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
    
    print(df)

def getTweets():
    auth = authenticateTwitterAPI()
    api = tweepy.API(auth, wait_on_rate_limit=True)
    t = fetchTweets(api)
    tweets_to_data_frame(t)

def execute():
    getHashtag()
    getTweets()

if __name__ == "__main__":
    execute()