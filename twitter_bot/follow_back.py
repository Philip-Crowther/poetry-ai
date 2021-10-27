# follow back all followers not previously followed
import tweepy
import build_api

def follow(api):
    for follower in tweepy.Cursor(api.get_followers).items():
        if not follower.following:
            follower.follow()

def main():
    print("creating api")
    api = build_api.build_api()
    print("executing follow function")
    follow(api)
    print("finished")

if __name__ == "__main__":
    main()
