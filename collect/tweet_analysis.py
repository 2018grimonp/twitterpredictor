from twitter_connection_setup import twitter_setup

import pandas as pd

import numpy as np

def collect_to_pandas_dataframe():
    connexion = twitter_setup()
    tweets = connexion.search("@MLP_officiel",language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

data=collect_to_pandas_dataframe()

def retweet():
    column_rts=data['RTs']
    return (column_rts)

print(retweet())

def likes():
    column_like=data['Likes']
    return (column_like)


