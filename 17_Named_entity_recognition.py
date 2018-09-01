# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

"""
Now that we've learned how to do some custom forms of chunking, and chinking, 
let's discuss a built-in form of chunking that comes with NLTK, and that is named entity recognition.

One of the most major forms of chunking in natural language processing is called 
"Named Entity Recognition." The idea is to have the machine immediately be able to 
pull out "entities" like people, places, things, locations, monetary figures, and more.

This can be a bit of a challenge, but NLTK is this built in for us. There are two major 
options with NLTK's named entity recognition: either recognize all named entities, or 
recognize named entities as their respective type, like people, places, locations, etc.

"""

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
    except Exception as e:
        print(str(e))


process_content()

"""
Here, with the option of binary = True, this means either something is a named 
entity, or not. There will be no further detail. 

If you set binary = False

Immediately, you can see a few things. When Binary is False, it picked up the 
same things, but wound up splitting up terms like White House into "White" and 
"House" as if they were different, whereas we could see in the binary = True option, 
the named entity recognition was correct to say White House was part of the same named entity.

Depending on your goals, you may use the binary option how you see fit. 
Here are the types of Named Entities that you can get if you have binary as false:

NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian

"""

""" 
    That's the End of Named Entity Recognition concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""