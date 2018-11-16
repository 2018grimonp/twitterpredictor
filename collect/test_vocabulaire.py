from textblob import TextBlob
from textblob import Word
import nltk

from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))


def voc(mots):  #chaine de caracteres
    l=TextBlob(mots)
    w=l.tags                #on obtient une liste de chaine de caractères
    L=[]
    for i in w:
        a=i[0].lemmatize()
        if a not in L and (a not in stop_words):
            L.append(a)
    return (L)


def testvoc ():
    l=voc("I am almost finished and so I am happy!")
    assert type(l) == list          #on vérifie que l'on obtient bien une liste
    for i in l:
        assert type(i) == str       #on verifie que chaque element est un string
    L=""
    for i in l:
        L=L+i                       #on verifie que l'on obtient bien le meme resultat quand on a reapplique la fonction a la chaine de caractère reconstitue.
    assert l==voc(L)







