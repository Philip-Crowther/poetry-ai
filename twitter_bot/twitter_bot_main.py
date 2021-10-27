# twitter bot 
import tweepy
import os
import time

# Authenticate to Twitterp
auth = tweepy.OAuthHandler(os.getenv("MUSE_AI_CONSUMER_KEY"), os.getenv("MUSE_AI_CONSUMER_SECRET"))
auth.set_access_token(os.getenv("MUSE_AI_ACCESS_TOKEN"), os.getenv("MUSE_AI_ACCESS_TOKEN_SECRET"))

# Create API object
api = tweepy.API(auth)

# follow all unfollowed followers
for follower in tweepy.Cursor(api.get_followers).items():
    if not follower.following:
        follower.follow()

