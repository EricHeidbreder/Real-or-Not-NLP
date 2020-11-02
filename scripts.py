from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from collections import Counter
from nltk.corpus import stopwords

def find_hashtags(text):
    '''
    Split the text, then find a hashtag and return the word minus the hashtag
    This will let us look at just the hashtags, if we'd like.
    '''
    return ' '.join([word[1:] for word in text.split() if word.startswith('#')])

def remove_links(text):
    '''
    This code removes links and html artifacts and is great for 
    dirty data scraped from the internet.
    '''
    
    # Getting rid of links
    text = [word for word in text.lower().split() if not 'http' in word]
    text = ' '.join(text)
    
    return text