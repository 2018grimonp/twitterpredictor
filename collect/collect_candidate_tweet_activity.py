def twitter_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """

    try:
        #on ouvre le fichier file_path et on créé une liste contenant des chaines de caractères correspondant à chaque keyword ou hashtag
        lignes=[]
        with open('file_path') as inf:
            for line in inf:
                num = line.strip()  #on prend chaque ligne une par une et on la rajoute à l
                lignes.append('num')     #on créé une liste dont chaque élément (string) est une ligne
        connexion = twitter_setup()
        queries=[]
        for i in range(len(lignes)):
            queries.append (connexion.search("l[i]"))   #on rajoute chaque requète à la liste queries
        return queries

    except IOError:
        print'Assemblage des requètes impossible'

def test_queries(num_candidate, file_path):
    queries = get_candidate_queries(num_candidate, file_path)
    for querie in queries:
        assert querie != None



