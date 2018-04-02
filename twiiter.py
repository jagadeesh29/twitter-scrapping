"""
@author: jac
"""

import tweepy
import textblob
# you can add your own key information.
consumer_key = "xxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token = "9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#get my timeline mes by using home_timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
    
# get the tweets of a twitter_id or user_name
name = "ikamalhaasan"
tweetcount = 20
result = api.user_timeline(id= name,count = tweetcount)
#for getting all tweets
for tweet in result:
    print(tweet.text)

query = "#NammavarAgainstSterlite"
language = "en"
# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# for getting all tweets
for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.user.screen_name,"Tweeted:",tweet.text)
