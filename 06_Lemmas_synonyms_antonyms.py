# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

"""
    This tutorial covers about lemmas, synonyms and antonyms

"""

"""
    Lemma : It is something like a stem word. 
    
            example : 
                run is the stem word for running, runs, ran etc..
            
            It simply means the base form of the word.
                
"""

from nltk.corpus import wordnet

input_word = "win"

synsets_array = wordnet.synsets(input_word)
 
## lets consider the 3 synset i.e.., win.v.01

my_word = synsets_array[2]

## seeing the lemmas
print(my_word.lemmas())

## seeing the lemma name
print(my_word.lemmas()[0].name())


## the length of list of lemmas may not be always one, it depends upon the word

## list of all synonyms for the word win

synonyms_array = []

for synsets in synsets_array : 
    for lem in synsets.lemmas() : 
        synonyms_array.append(lem.name())

print(synonyms_array)

## len of synonyms_array

print(len(synonyms_array))

## len of unique synonyms_array

print(len(set(synonyms_array)))

## print out antonyms for a particular lemma

print(my_word.lemmas()[0].antonyms())

## list of all antonyms for the word win

antonyms_array = []

for synsets in synsets_array : 
    for lem in synsets.lemmas() : 
        for ant in lem.antonyms():
            antonyms_array.append(ant.name())
            
print(antonyms_array)  
## len of antonyms_array

print(len(antonyms_array))

## len of unique synonyms_array

print(len(set(antonyms_array)))  

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))        


""" 
    That's the End of lemmas, synonyms and antonyms concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""