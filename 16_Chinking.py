# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

"""

Chinking : Chinking means removing a chunk for chunk. The chunk which you want
           remove from a chunk is called chink.
           
Why to do : In chunking you have seen that, there are lot of words which you dont
            want to be, but somehow it came, so at that time chinking comes to play.
            
How to do : It's very simple just the chink inside } { after a chunk.

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

            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()


"""
}<VB.?|IN|DT|TO>+{ : This means we're removing from the chink one or more verbs, 
                     prepositions, determiners, or the word 'to'.

"""

""" 
    That's the End of Chinking concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""