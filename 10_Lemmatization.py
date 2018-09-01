# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

################ Lemmatization ####################

"""

$$  Lemmatization : 
            It is same as the stemming, i.e.., extracting the
    base form of the word. But the difference is that lemmatization 
    takes the word from the lemmas(taught in concept of synsets)
    and it is more accurate than stemming.


    The only major thing to note is that lemmatize takes a part of speech (POS)
    parameter. If not supplied, the default is "noun." This means that an 
    attempt will be made to find the closest noun

    A very similar operation to stemming is called lemmatizing. 
    The major difference between these is, as you saw earlier, stemming 
    can often create non-existent words, whereas lemmas are actual words.

"""

## importing libraries

from nltk.stem import WordNetLemmatizer

my_lemmatizer = WordNetLemmatizer()

my_lemmatizer.lemmatize('dancing')
## it is wrong,,,let's check one more

my_lemmatizer.lemmatize('working')
## still wrong

"""

$$  So, have you figured out why it is comming wrong, remembered the 
    concept of synsets where it gives the lemmas of the word along with 
    part of speech.

    So, here the lemmatize method is considering dancing, working as noun, 
    therefore a noun cannot have a base form, so we need to specifically 
    mention it as a verb.

    So, let's try that :

"""

my_lemmatizer.lemmatize('dancing', pos = 'v')

my_lemmatizer.lemmatize('working', pos = 'v')


### let's check out the difference b/w stemming and lemmatization

from nltk.stem import PorterStemmer

pstemmer = PorterStemmer()
pstemmer.stem('dancing')

pstemmer.stem('buses')
my_lemmatizer.lemmatize('buses')
my_lemmatizer.lemmatize('King')


""" 
    That's the End of Stemming concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""

