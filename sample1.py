import urllib.request

import nltk

response =  urllib.request.urlopen('https://tr.wikipedia.org/wiki/Elma')
html = response.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)


tokens = [t for t in text.split()]

from nltk.corpus import stopwords

sr = stopwords.words('turkish')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('turkish'):
        clean_tokens.remove(token)

#freq = nltk.FreqDist(clean_tokens)
#for key, val in freq.items():
#    print(str(key) + ':' + str(val))
#freq.plot(20, cumulative=False)

"""
from snowballstemmer import TurkishStemmer
turkStem=TurkishStemmer()
turkStem.stemWord("ekmekler") #ekmek
turkStem.stemWord("olta") #ol
turkStem.stemWord("sonra") #sonra
"""

""""
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words_lemma = [lemmatizer.lemmatize(word) for word in clean_tokens]
print(words_lemma)
"""

import zeyrek
analyzer = zeyrek.MorphAnalyzer()
print(analyzer.lemmatize("gideceğim"))