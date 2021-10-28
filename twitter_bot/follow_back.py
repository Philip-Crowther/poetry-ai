#!/usr/bin/env python
# follow back all followers not previously followed
import tweepy
import build_api
import time

def follow(api):
    """follow unfollowed followers"""
    for follower in tweepy.Cursor(api.get_followers).items():
        if not follower.following:
            follower.follow()

def main():
    """build api and follow followers"""
    api = build_api.build_api()
    while True:
        follow(api)
        time.sleep(60)

if __name__ == "__main__":
    main()
