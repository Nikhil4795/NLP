# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

"""

$$  Processing the text : 
        To start doing anything, you first have to see how the data
        is actually there in the dataset, and then you need to 
        develop a logic using those basic visualization according 
        to your requirement.
        
    There are many datasets available for training purpose in the
    NLTK module. You can use any one of them.
    
    I have show the sample code to get the data from the two most
    popular datasources which i know, so make use of it.

"""

## Import text from Gutenberg source

import nltk
from nltk.text import Text
carroll_alice = Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))

# NLTK also provides other texts from Gutenberg. you can view those by 
# running the following command:
print(nltk.corpus.gutenberg.fileids())


## Import text from webtext source

from nltk.corpus import webtext
pirates = Text(nltk.corpus.webtext.words('pirates.txt'))

# NLTK also provides other texts from webtext. you can view those by 
# running the following command:
print(nltk.corpus.webtext.fileids())

### we will consider the Pirates dataset

# Word Count: How many words are contained in pirates :
# Note that this includes punctuation as well as traditional words.

print("Total word count : ",len(pirates))

# Unique Word Count: How many unique words are present in pirates : 

print("Unique word count : ",len(set(pirates)))

# Specific Word Count: How many times does a specific word occur in a text : 

print(pirates.count("Jack"))

# Concordance: Shows occurence of word in context of use.
# We can check where the term "Jack" appears in "pirates".

pirates.concordance("Jack")

"""
$$  Dispersion Plot: It's basically a graphical plot which shows where 
                     particular word in present in the whole text.

"""
                   
pirates.dispersion_plot(["Jack", "Turner", "Davy", "Elizabeth", "cannibal"])



# Frequency Distributions: What are the most frequent words that are 
#                          used in a given text.

freq_dist = nltk.FreqDist(pirates)


# What are the top 50 most common words in pirates :
freq_dist.plot(50, 
               cumulative=True, 
               title="50 most common words in Pirates")

"""
$$  Observe that the x-axis consists of not so important words in plot, 
    so i guess you know what to do get rid of this if you follow my tutorial,
    so you should use stopwords to delete these words
    to obtain more informative plot.
    
    And to eliminate punctuation we use isalpha(), which does the job perfect.
    Basically what it does is, it checks whether a given word only contains
    alphabets or not and returns True or False accordingly


"""

freq_dist_no_punc = nltk.FreqDist(
        dict((word, freq) for word, freq in freq_dist.items() if word.isalpha()))

freq_dist_no_punc.plot(50,
                   cumulative=True, 
                   title="50 most common words (Without punctuation)")


stopwords = nltk.corpus.stopwords.words('english')

freq_dist_no_punc_no_stopwords = nltk.FreqDist(
        dict((word, freq) for word, freq in freq_dist.items() if word not in stopwords and word.isalpha()))


# Replot fdist after stopwords filtered out.
freq_dist_no_punc_no_stopwords.plot(50, 
                                cumulative=True, 
                                title="50 most common tokens (no stopwords or punctuation)")


""" 
    That's the End of Data preprocessing part -1 concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""

    
