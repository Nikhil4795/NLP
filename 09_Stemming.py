# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""
############# Stemming ####################

"""

$$  Stemming : It is basically chopping of the words as smaller as possible
               to extract the base form.
        
        The conversion of a word into a base form, is called as stemming.
    
        Ex : write is the base form of writting, written, writes etc..
    
    Why do we do that ?
        to save space and iterate through less words rather than going 
        through all the words which comes under a stem.
        
        example : run, running, runs, ran etc... for all these words we 
        can just keep only word run, the base meaning won't change so no 
        problem in doing that and it saves lot of space.
    
    How do you convert a word into stem ?
        Stemmers. We can use something which are called stemmers to convert 
        any word ito its base form.
    
    Kinds of stemmers :
        1. PorterStemmer - most popular
        2. LancasterStemmer
        3. RegexpStemmer
        4. SnowballStemmer - for languages other than engish.
        
    Buzz Words : 
        1. Aggressive - Most aggressive means cutting down
        the words quite aggressively.
        
"""

## importing the Libraries

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer

######## PorterStemmer ###########

pstemmer = PorterStemmer()

pstemmer.stem('dancing')

pstemmer.stem('dancer')

pstemmer.stem('dance')


"""

$$  some of Those are ofcourse not a recognised words in english, just 
    showing this results because, just to get you a clear idea about what 
    was happening in the background and understand the errors which arised. 

    Let's not worry about the errors, you will get to how to 
    eliminate those in next tutorial about Lemmatizing, so just
    hold your breath for some more time.

    so let's continue..,

    Also Porterstemmer is called Least aggressive

"""

######## LancasterStemmer ###########

lstemmer = LancasterStemmer()
lstemmer.stem('dancing')

"""
$$  LancasterStemmer - Most Aggressive.

    LancasterStemmer is mostly used for the cases where the 
    data or text is very huge, but your accuracy might falldown
    because of its most aggressive nature.

"""

######## RegexpStemmer ###########

rstemmer = RegexpStemmer('ing')
## remove all the letters except for a given word

rstemmer.stem('cooking')
rstemmer.stem('dancing')

rstemmer.stem('king')

## as you can only k is given if we have given king...
## so should be more carefull about it.

""" 
    That's the End of Stemming concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""




