# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

###################### Sentence Tokenizers ########################

"""

$$ Previously, in the last tutorial we have seen how to tokenenize words
   from a sentence, in this tutorail we will see how to tokenize sentences from
   paragraphs.

$$  Tokenization is the act of breaking up a sequence of strings into pieces
    such as words, keywords, phrases, symbols and other elements, which are called tokens


    with nltk you can perform tokenizing the sentence, which simply means that you can,
    break a multiple lines of paragraph or text into small pieces (technically called Tokens),
    so that it becomes easy for anyone to handle huge text data and further you can divide
    those sentences into words and draw some insights out of it.
    
    
    Tokenizing text is important since text can’t be processed without tokenization.
    
"""

###################### Sent Tokenize #######################

from nltk.tokenize import sent_tokenize

## taking some random text.
test_paragraph = "Hi how are you. I hope every thing is going good with you. \
             Glad to have you here. You are just awesome."

## tokenizing text into sentences(Tokens) and storing it into a array.
sent_tokenize_array = sent_tokenize(test_paragraph)

print(sent_tokenize_array)

## here sentence_array is list of tokens of the paragraph text.
## you can access that list for individual assignments.
## for example..,

print(sent_tokenize_array[3])

"""

$$  sent_tokenize uses an instance of PunktSentenceTokenizer
    from the nltk. tokenize.punkt module.
    
    This instance has been already trained on many languages, so it know where
    exactly the sentence ends and begins. 
    
    you can just simply understand that sent_tokenize is a small function
    in the main class PunktSentenceTokenizer.

"""

## so now let's check how to tokenize using PunktSentenceTokenizer.

###################### PunktSentence Tokenizer (English) ######################

import nltk.data

## creating an object from the punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

## let us take the text which we've used above

punkt_tokenizer = tokenizer.tokenize(test_paragraph)

print(punkt_tokenizer)


""" 
$$  There are around 17 european languages that NLTK supports for tokenizing
    the sentences. 
    
    Pickle : The pickle module implements binary protocols for serializing and
             de-serializing a Python object structure. “Pickling” is the process
             whereby a Python object hierarchy is converted into a byte stream,
             and “unpickling” is the inverse operation, whereby a byte stream
             (from a binary file or bytes-like object) is converted back into
             an object hierarchy. Pickling (and unpickling) is alternatively
             known as serialization, marshalling or flattening
    
    you can know more about picle from here..,
    https://pythontips.com/2013/08/02/what-is-pickle-in-python

"""


###################### PunktSentence Tokenizer (Spanish) ######################

tokenizer_spanish = nltk.data.load('tokenizers/punkt/spanish.pickle')


spanish_paragraph = "Hola como estás? Todo va bien?"

punkt_spanish_array = tokenizer_spanish.tokenize(spanish_paragraph)

print(punkt_spanish_array)


"""  
$$   If you want to check out for others languages also, just go the
     nltk installed folder and find some pickle files and make use of it.

"""

""" 

$$  You may think that this is an easy task, i can tokenize the text based on
    punctuation marks using python some code or by using regular expressions.
    There is no need of NLTK modules.
    
    It is correct upto some extent, but sometimes even a single sentence may 
    contain punctuations, in that case your accuracy might fall down. 
    
    So, if you're concerened with accuracy i suggest you to use NLTK modules.
    
    checkout the below example. 

"""

test_paragraph_1 = "Hello Mr. Smith, how are you? I hope everything is going well. \
                  will you join me for a drink along with Mrs. David?"


# testing test paragraph with sent_tokenize
sent_tokenize_test = sent_tokenize(test_paragraph_1)
print(sent_tokenize_test)

# testing test paragraph with punkt tokenizer
punkt_tokenize_test = tokenizer.tokenize(test_paragraph_1)
print(punkt_tokenize_test)

"""

$$  you can see that nltk modules works fine with Mr. Smith and Mrs. David,
    those are not treated as multiple sentences because of punctuation marks, but
    if we regular expressions for the above test_paragraph it spoils the output.
    
"""

""" 
    That's the End of Sentence Tokenizer concept.
    If you have any questions or suggestions regarding the concept
    feel free to contact me via nikhil.ss4795@gmail.com

"""











