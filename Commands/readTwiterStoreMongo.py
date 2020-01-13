import tweepy
from tweepy import OAuthHandler

import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from pymongo import MongoClient


consumer_key=""
consumer_secret=""
access_token=""
access_secret=""

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)
 
class MyListener(StreamListener):
    
    def on_data(self, data):
        try:
            Client = MongoClient()
            db = Client.HappySad
            db.sad.insert(json.loads(data))
            with open('SadData.csv', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['sad'])
