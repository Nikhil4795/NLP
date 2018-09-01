# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

import nltk
from nltk.text import Text
# We will continue the visuaizing text part

from nltk.corpus import webtext
pirates = Text(nltk.corpus.webtext.words('pirates.txt'))

freq_dist = nltk.FreqDist(pirates)


# Hapaxes: These are the words that occur exactly once in the text.

print(freq_dist.hapaxes())

print(len(freq_dist.hapaxes()))


# Collocations: A pair or group of words that are habitually juxtaposed. 

print(pirates.collocations())

# Get words from text (what we did in Part 1):

pirates_words = nltk.corpus.webtext.words('pirates.txt')

# Note that Python does not print out the entire list or words. The ellipsis 
# (...) sequence denotes that there is more content that is supressed from output.

print(pirates_words)
print(len(pirates_words))

# Get characters from pirates :
pirates_chars = nltk.corpus.webtext.raw('pirates.txt')
print(pirates_chars)
print(len(pirates_chars))

# Get sentences from "Alice in Wonderland": 
pirates_sents = nltk.corpus.webtext.sents('pirates.txt')
print(pirates_sents)
print(len(pirates_sents))

# With the above chars, words, and sentences extracted from Pirates text
# we can make use of these to calculate some cursory information on the text:

print("Average Word length : ",int(len(pirates_chars) / len(pirates_words)))

print("Average sentence length : ",int(len(pirates_words) / len(pirates_sents)))

# Let us turn the above two metrics into functions, and determine the average 
# word length and sentence length of all the texts in the Gutenberg collection. 


def avg_word_len(num_chars, num_words):
    return int(num_chars/num_words)


def avg_sent_len(num_words, num_sents):
    return int(num_words/num_sents)

for file_id in nltk.corpus.webtext.fileids():
    num_chars = len(nltk.corpus.webtext.raw(file_id))
    num_words = len(nltk.corpus.webtext.words(file_id))
    num_sents = len(nltk.corpus.webtext.sents(file_id))

    print(file_id + 
          " has an average word length of " + 
          str(avg_word_len(num_chars, num_words)) + 
          " and an average sentence length of " + 
          str(avg_sent_len(num_words, num_sents)))

# Sentence length tends to vary, while word length among all of these texts 
# is consistent.

# Inaugural Address Corpus:

# This is a collection of presidential inaugural addresses; the speech that the 
# president makes prior to officially starting their term in office. 

# Let us print out the files provided to us via the inaugural corpus :

for file_id in nltk.corpus.inaugural.fileids():
    print(file_id) 

# Let us loop through each address. While doing so, let us keep a running tally 
# of the number of times the word "America" is used in each address.


for fileid in nltk.corpus.inaugural.fileids():
    america_count = 0 
    # Loop through all words in current inaugural address:
    for w in nltk.corpus.inaugural.words(fileid):
        # We convert the word to lowercase before checking 
        # This makes checking for the occurrence more consistent.
        # Note that the "startswith" function also catches words like 
        # "American", "Americans", etc.
        if w.lower().startswith('america'):
            america_count += 1
    # Output both the inaugural address name and count for America:
    president = fileid[5:-4]
    year = fileid[:4]
    print("President " + president + 
          " of year " + year + 
          " said America " + str(america_count) + " times.")

"""

$$  Say I also want to see how many times the word "citizen" is present in
    each of the inaugural addresses. It may be preferable to consider a plot
    output as opposed to one that simply outputs to terminal.

    Let us consider a conditional frequency distribution, that is a frequency
    distribution that is a collection of frequency distributions run under
    different conditions.

    Recall the FreqDist function took a list as input. NLTK provides a 
    ConditionalFreqDist function as well which takes a list of pairs. 
    Each pair has the form (condition, event).

    In our example, we care about the case when either the word "America"
    or "citizen" is used in each of the inaugural addresses.

"""

conditional_freq_dist = nltk.ConditionalFreqDist(
            (target, fileid[:4])
            for fileid in nltk.corpus.inaugural.fileids() 
            for w in nltk.corpus.inaugural.words(fileid)
            for target in ['america', 'citizen']
            if w.lower().startswith(target))

conditional_freq_dist.plot()

""" 
    That's the End of Data preprocessing part -2 concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""