import tweepy
# We import our access keys:
from twitter_collect.credentials import *

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    #Tweet pour s'assurer que ça marche
    api = tweepy.API(auth)
    status="testing"
    api.update_status(status=status)
    return api

def testt ():
    assert None != twitter_setup()
