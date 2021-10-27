# build api function
import os
import tweepy

def build_api():
    """reusable function to build api object"""
    # Authenticate to Twitter
    print("authenticating")
    auth = tweepy.OAuthHandler(os.getenv("MUSE_AI_CONSUMER_KEY"), \
        os.getenv("MUSE_AI_CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("MUSE_AI_ACCESS_TOKEN"), \
        os.getenv("MUSE_AI_ACCESS_TOKEN_SECRET"))

    # Create API object
    api = tweepy.API(auth)
    print("api created")
    return api

def main():
    """main function"""
    pass

if __name__ == "__main__":
    main()
