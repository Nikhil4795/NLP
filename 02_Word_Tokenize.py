# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

###################### Word Tokenizers ########################

""" 

$$  Tokenization is the act of breaking up a sequence of strings into pieces
    such as words, keywords, phrases, symbols and other elements, which are called tokens

    With nltk you can perform tokenizing the words, which simply means that you can,
    break a multiple words of sentence or text into small pieces (technically called Tokens),
    so that it becomes easy for anyone to handle huge text data and draw some insights out of it.
       
    Tokenizing text is important since text can’t be processed without tokenization.
    
"""

sentence = "I love coding in python especially problems involving machine learning. Do you also love it?"

sentence_1 = "I love coding in python especially problems involving machine learning."

################ Word Tokenizer ################

from nltk.tokenize import word_tokenize

word_tokenize_array = word_tokenize(sentence)

print(word_tokenize_array)

################ TreebankWord Tokenizer ################

from nltk.tokenize import TreebankWordTokenizer

treebank_tokenizer = TreebankWordTokenizer()

treebank_array = treebank_tokenizer.tokenize(sentence)
treebank_array_1 = treebank_tokenizer.tokenize(sentence_1)

print(treebank_array)
print(treebank_array_1)

""" 

$$  You can see that both sentence and sentence_1 are same for first sentence. 
    but treebank_array and treebank_array_1 produces different results.
    one considered dot(.) as a word but one doesn't.

"""

################ WordPunctTokenizer ################


from nltk.tokenize import WordPunctTokenizer

wordpunct_tokenizer = WordPunctTokenizer()

wordpunct_array = wordpunct_tokenizer.tokenize(sentence)

print(wordpunct_array)


"""

$$  Also there is an another word tokenizer called PunktWordTokenizer but unfortunally,
    i can't show that due to some version problem. 


$$  There in the results arrays you can see that punctuation marks is also treated
    as a word, let's not worry about that now, you can later remove those punctuations,
    by small code.


$$  Apart from the punctuation marks, everything is same in all the different tokenizers
    but the difference comes with the words like can't , wont't, etc..,
    
"""

#### Let's test this

test_sentence = "Hi there, I won't be able to come tomorrow. can't you understand it. It's my opinion.\
                 The sky is pinkish-blue in color."


word_tokenize_test = word_tokenize(test_sentence)
treebank_test = treebank_tokenizer.tokenize(test_sentence)
wordpunct_test = wordpunct_tokenizer.tokenize(test_sentence)

""" 
$$  PunktWordTokenizer gives a different output for the test_sentence, it would be something like,
    "can", "'t", "won", "'t" etc... 

"""

""" 
$$  So you can solve these problems by
    1. replace can't, won't words with fullforms like cannot, wouldnot, shallnot etc..
       and then after tokenizing you can bring it back to original position depending upon
       your requirements. 
       
    2. you can use regular expressions and then tokenize.

"""

"""
$$  Regular Expressions : 
            some basics...,
    [\w]    :   represents anything that has a letter, like a word.
    [\w]+   :   it means that letter followed by a letter. 
    [\d]    :   represents a digit.
    [\d]+   :   represents a sequence of digits.
    [\s]    :   represents a space.
    
"""

from nltk.tokenize  import regexp_tokenize

"""
$$  regexp_tokenize takes two parameters, one is text and other is the 
    expression you want to use.
    
"""
regexp_tokenizer_test = regexp_tokenize(test_sentence,"[\w']+")

## when you see the result, you can see that the problem has been sorted out

""" 
$$  if you don't keep an (') in the regular expression above, the results would be something like..,
    ""can", "t", "won", "t"...etc..
    
"""
## also you can directly instantiate the Regexp tokenize class. 

from nltk.tokenize import RegexpTokenizer

reg_exp_tokenizer = RegexpTokenizer("[\w']+")

regexp_tokenizer_test_1 = reg_exp_tokenizer.tokenize(test_sentence)

print(regexp_tokenizer_test_1)

""" 

$$   A small description about each tokenizers..,
     word_tokenize is a wrapper function that calls tokenize by the TreebankWordTokenizer.
     PunktTokenizer splits on punctuation, but keeps it with the word.
     WordPunctTokenizer splits all punctuations into separate tokens. 
     
"""

"""  
$$   You can choose which tokenizer you want to use based on your requirements.
     
     Also there a lots of options of tokenizing your text, you can check it out at,
     http://www.nltk.org/api/nltk.tokenize.html
     
"""


""" 
    That's the End of Word Tokenizer concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""




