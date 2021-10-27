# build api function
import tweepy
import os

def build_api():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(os.getenv("MUSE_AI_CONSUMER_KEY"), os.getenv("MUSE_AI_CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("MUSE_AI_ACCESS_TOKEN"), os.getenv("MUSE_AI_ACCESS_TOKEN_SECRET"))

    # Create API object
    api = tweepy.API(auth)
    return api

def main():
    pass

if __name__ == "__main__":
    main()
