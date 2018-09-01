# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

"""
Chunking : simply means the group words into meaningful
           chunks.
           
Why to do : The main aim of the chunking is to group 
            all the words into noun phrases..which is 
            latest used in Named-Entity recognition.
            
            These noun phrases are of one of more words
            that contains a noun, verb etc.,
            
            The idea is to group nouns with the words
            that are in relation to them.
            
How to do : To perform chunking, we combine the part
            of speech tags with regular expressions.


Regular Expressions : 
    
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions	  
. = Any character except a new line


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
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            #print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)

            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()

"""

chunkGram = r"Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"

RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes

1. <RB.?>* : As you can see in the part of speech tags, we take adverb first, 
            . -> indicates that any character, except for new line
            ? -> indicates that 0 or 1 , as you can see there is nothing, greater
                 than 3 charaters. 
            * -> 0 or more anyform of adverbs
        
    
    so it totally gives the RB,RBR,RBS tags under a chunk if there is atleast one.

2. <VB.?>* : same as <RB.?>

similarlly for the next ones...

why we have kept + for NNP and NN, beacause if you remove the +, and run the 
script you may see that all the nonn phrases tagged seperately, but you want 
to tag them under one chunk so, + is used for that purpose.

"""

""" 
    That's the End of Chunking concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""
