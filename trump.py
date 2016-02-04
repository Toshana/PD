# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:54:31 2016

@author: centraltendency
"""

# Web Scraping with BeautifulSoup
from bs4 import BeautifulSoup
import urllib
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd
from string import punctuation
import csv


r = urllib.request.urlopen("https://www.washingtonpost.com/news/post-politics/wp/2015/06/16/full-text-donald-trump-announces-a-presidential-bid/").read()
soup = BeautifulSoup(r, 'lxml')
#print(type(soup))
#print(soup.prettify()[0:1000])
#paragraphs = soup.find_all("p", class_= False)
paragraphs = soup.find_all("p", {"class" : False, "id" : False})

listOfText = []
for paragraph in paragraphs:
    listOfText.append(paragraph.get_text())

#print(paragraphs[200])
listofwords =[]
d = "APPLAUSE"
c = "AUDIENCE MEMBER"
for item in listOfText:
    if c not in item:
        listofwords.append(item)
listwithoutapplause = []
for item in listofwords:
    if d not in item:
        listwithoutapplause.append(item)
a = "AUDIENCE"
listwithoutaudience = []
for item in listwithoutapplause:
    if a not in item:
        listwithoutaudience.append(item)
b = "LAUGHTER"
listwithoutlaughter = []
for item in listwithoutaudience:
    if b not in item:
        listwithoutlaughter.append(item)

# relevant text is in 2:196
trump_words = listwithoutlaughter[2:191]

split_words = []
for string in trump_words:
    split_words.append(string.split()) 

trump_list = []
for sublist in split_words:
    for val in sublist:
        trump_list.append(val)

#remove TRUMP: 
def remove_val_from_list(the_list, val):
    while val in the_list:
        the_list.remove(val)
        
remove_val_from_list(trump_list, "TRUMP:")

# Remove punctuation
trump_list_no_rpunc = [w.rstrip(punctuation) for w in trump_list]
trump_list_no_lpunc = [w.lstrip(punctuation) for w in trump_list_no_rpunc]


# Dimensionality Reduction
lower_list = []
for word in trump_list_no_lpunc:
   lower_list.append(word.lower()) 
   
# Stemmer
stemmer = PorterStemmer()
stemmed_trump = [stemmer.stem(item) for item in lower_list]
# Lemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_trump = [lemmatizer.lemmatize(item, pos ='v') for item in lower_list]


trump_1 = []
for word in lemmatized_trump:
    if word not in stopwords.words('english'):
        trump_1.append(word)

# count frequency of words
# get unique values
trumpdict1 = {} # dictionary
for word in trump_1:
    if word in trumpdict1:
        trumpdict1[word] +=1
    else:
        trumpdict1[word] = 1

word_list = []
for word in set(trump_1):
    word_list.append(word)
    
# remove empty strings
word_list = [x for x in word_list if x != '']

counts = []
for word in word_list:
    counts.append(trump_1.count(word))
    

word_df = pd.DataFrame(word_list, index = range(0, 891), columns = ["word"])
count_df = pd.DataFrame(counts, index = range(0, 891), columns = ["count"])
trump_df = word_df
trump_df["count"] = count_df # dataframe

# sort dataframe by descending 

trump_descending = trump_df.sort("count", ascending = False)

# trump_df.to_csv("trump_speech_one_", sep = ',')

# Further exploration of the dataset


one = trump_df [trump_df["count"] == 1] # 423 words appear once in the speech
two = trump_df [trump_df["count"] == 2] # 168 words appear twice
three = trump_df [trump_df["count"] == 3] # 85
four = trump_df [trump_df["count"] == 4] # 57
five = trump_df [trump_df["count"] == 5] # 37
six = trump_df [trump_df["count"] == 6] # 22



        

    
        
        
        
        
        
        
        
        
        






