# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

################ Stopwords ###################

"""

$$  The process of converting data to something a computer can understand is referred
    to as pre-processing. One of the major forms of pre-processing is to filter out useless data.
    In natural language processing, useless words (data), are referred to as stop words.
    
    Stop Words: A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a
    search engine has been programmed to ignore, both when indexing entries for searching and
    when retrieving them as the result of a search query.

    We would not want these words taking up space in our database, or taking up valuable
    processing time. For this, we can remove them easily, by storing a list of words that
    you consider to be stop words. NLTK(Natural Language Toolkit) in python has a list of
    stopwords stored in 16 different languages. You can find them in the nltk_data directory.

    So, the reason why we use stopwords or identify the stopwords is not that we are
    interested in stopwords, but we are interested in what left after filtering out stopwords.

"""

## import necessary package from nltk

from nltk.corpus import stopwords

eng_sw = stopwords.words('english')

test_paragraph = "Hi, how are you? what are you doing exactly right now? shall we hangout?"


from nltk.tokenize import word_tokenize

word_tokenize_array = word_tokenize(test_paragraph)

print(word_tokenize_array)

filtered_words = [word for word in word_tokenize_array if word not in eng_sw]

print(filtered_words)

""" 
$$  Note : In some cases, some words may appear in filtered_words because of case-sensitive
    it's better to keep both the stopwords and tokenized words in same case either
    upper case (or) lower case

"""

""" 
$$  You can see that there are still some punctuation marks in the filtered words,
    you can remove that by importing punctuation from string. 
    
    for easyness i have assigned both stopwords and punctuation to a set, since
    sets contains only unique values and it is more faster than lists. 

"""

from string import punctuation

waste_words = set(stopwords.words('english') + list(punctuation))

filtered_words_1 = [word for word in word_tokenize_array if word not in waste_words]

print(filtered_words_1)

"""
 The stopwords used above are the one's which are universally accepted, but it not mandatory
 that you should only use these, you can either add some other stopwords or remove some words
 it all depends upon your requirements.
 
 The stopwords are not only available in english, it is in over 40+ languages.  

"""

""" 
    That's the End of Stopwords concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""
    







