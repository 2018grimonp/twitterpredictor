from twitter_connection_setup import twitter_setup

import pandas as pd

import numpy as np

connexion = twitter_setup()

"""Objectif: La majorite des retweets sont fait par les followers. 
On divise donc le nombre de retweets de deux candidats par le nombre de followers pour savoir quelle est
la communaute la plus active. On remultiplie par 10 000 pour pouvoir visualiser.
Rend plus ou moins bien en fonction de la periode de temps sur laquelle on se place"""

def collect_to_pandas_dataframe(username): # ex: @EmmanuelMacron
    tweets = connexion.search("username",language="fr",rpp=1000)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data


follower_count1 = connexion.get_user('JLMelenchon').followers_count
follower_count2 = connexion.get_user('EmmanuelMacron').followers_count
data1=collect_to_pandas_dataframe("@JLMelenchon")
data2=collect_to_pandas_dataframe("@EmmanuelMacron")

import matplotlib.pyplot as plt

tret1 = pd.Series(data=data1['RTs'].values*10000/follower_count1, index=data1['Date'])
tret2 = pd.Series(data=data2['RTs'].values*10000/follower_count2, index=data2['Date'])

# Likes vs retweets visualization:
tret1.plot(figsize=(16,4), label="Retweets JLM", legend=True)
tret2.plot(figsize=(16,4), label="Retweets EM", legend=True)

plt.show()



