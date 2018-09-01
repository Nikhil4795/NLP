# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

############ Bigram  and trigram collocations ##################

"""

$$  Collocations : it is that a pack of words which often comes
    with other word.

    Example : united kingdom, let's go, jack sparrow, etc...

    Bi-gram : set of two words
    Tri-gram : set of three words

"""

################### bi-grams ######################

# importing necessary libraries
from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

## taking the data from webtext
textwords = [w.lower() for w in webtext.words('pirates.txt')]


## start a finder function to find bigram

finder = BigramCollocationFinder.from_words(textwords)

finder.nbest(BigramAssocMeasures.likelihood_ratio, 10)

## likelihood_ratio : it will give the words with most likelihood. 

## second_argument : 10 (how many words do you want)

"""
As you can see that the output has also got unwanted data,
like punctuations, etc..

"""

## import stopwords
from nltk.corpus import stopwords

waste_words = set(stopwords.words('english'))


## also you can import punctuation from sting class, and 
## append it to the waste_words, that i have done in the previous
## tutorial please check it out.

## now we remove punctuations other than import punctuation from string class

## the plan is we find out the length of the word, and if
## it is less than 3 , we remove it..this also ensures that
## bigrams with less characters are also eliminated which is an
## added advantange for some of the projects


logic = lambda w: len(w) < 3 or w in waste_words


finder.apply_word_filter(logic)

finder.nbest(BigramAssocMeasures.likelihood_ratio, 10)

"""

Now you can see that the results are useful

"""


#################### Tri-grams ########################

## same as bi-gram just tochange the names of the libraries

from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

from nltk.corpus import webtext

finder1 = TrigramCollocationFinder.from_words(textwords)


finder1.nbest(TrigramAssocMeasures.likelihood_ratio, 10)

logic1 = lambda w: len(w) < 4 or w in waste_words
finder1.apply_word_filter(logic1)

finder1.nbest(TrigramAssocMeasures.likelihood_ratio, 10)

### also we can see that there are some more punctuations, comming
### so it's best better to use punctuation from sting class and 
### eliminate those to get rid of this problem


## apply frequency filter - takes parameter which say that a particular
##                          trigram and bigram has occured how many times..

## for exmaple if you want to see the results, which has occured
## atleast thrice, then you may need to give 3 as input

finder1.apply_freq_filter(3)
finder1.nbest(TrigramAssocMeasures.likelihood_ratio, 10)


""" 
    That's the End of Bigram  and trigram collocations concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""