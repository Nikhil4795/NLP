# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

"""
$$  This tutorial covers about Wordnets, Synsets, Hypernyms, Hyponyms, Meronyms,
    Holonyms, Entailments, lowest common hypernyms, common hypernyms.
    
    There are also bunch of other important methods wordnet has, you can view it
    here : http://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html
    
    it has ths source code of wordnet class you can check it out.
    
"""

"""
    NLTK module includes the English WordNet with 155287 words and 117659
    synonym sets that are logically related to each other.

    
    WordNet : WordNet is a huge lexical database for the English language, which was created
              by Princeton, and is part of the NLTK corpus.
              
              The english words in the wordnet are linked together by their semantic relationships.
              It's like a supercharged dictionary with a graph structure.
              This structure makes it a useful tool for computational linguistics and
              natural language processing.
              
              It groups English words into sets of synonyms called synsets, provides
              short definitions and usage examples, and records a number of relations
              among these synonym sets or their members. 
              
              You can use WordNet alongside the NLTK module to find the meanings of words,
              synonyms, antonyms, and more.
              
    
    Synsets : A set of one or more synonyms.
    
              As you already know, synonyms are the words that have similar meanings. 
            
              Synsets are basically synonyms of a word.
              For understanding just simply think that synsets are a subsets of wordnet.
    
    
    WordNet Hierarchy : one synset forms relations with other synset to form a hierarchy
                        of concepts, ranging from very general to moderate abstract to very
                        specific.
                        
                        For a given synsets, its...,
                        
                        Hypernyms : These are the synsets that are more generic.
                        Hyponyms  : These are the synsets that are more specific.
                        
                        Hyponyms have an "is-a" relationship to their hypernyms.
                        
                        also we can see "is-made-of" and "comprises" relationships. 
                        
                        For a given synset.,, it's...,
                        
                        Holonyms : these are the things that the item is contained in. 
                        Meronyms : these are the components or substances that make up the item.
                        
                        
                        simply we can say that..,
                        Meronyms - denotes a part of something
                        Holonyms - denotes a membership to something
                        
                        under meronyms and holonyms we can take advantage of two NLTK's functions : 
                            1. part_meronyms() or part_holonyms - obtains parts
                            2. substance_meronyms() or substance_holonyms- obtains substances
    
    
    Entailments : It basically denotes how verbs are involved
    
    min_depth : returns The length of the shortest hypernym path from this synset to the root.
                        
"""


""" 
    If you don't understand the theory part, dont worry about that now, first check out the 
    below examples of each terminology and then you can see the thoery part. Then i hope
    you can understand what each terminology means...
    
"""


## let's take a example word

input_word = "weapon"

## import the necessary package
from nltk.corpus import wordnet

synsets_array = wordnet.synsets(input_word)

print(synsets_array)

"""
    as you can see there are two synsets for the given word.
    In that if you can see there is an .n. written which describes Noun. 
    
    The synset string comprises of : 
    1. <lemma>              :   It is the word's morphological stem.
    2. <part-of-speech>     :   which mentions the part of speech of word like noun, verb, adjective etc..,
    3. <number>             :   is the sense number, starting from 0.
    
    Each synset contains one or more lemmas, which represent a specific sense of a specific word.
    
    Lemmas : It's something like a root word. Don't worry about it now, we will disuss that later. 
    
    Sense number : Senses are generally ordered from most to least frequently used,
                   with the most common sense numbered 1 . Frequency of use is determined
                   by the number of times a sense is tagged in the various
                   semantic concordance texts.

"""

my_word = synsets_array[0]
print(my_word)

### name of the synset
print(my_word.name())

### you can view the lemmas of a particular synset by :
print(my_word.lemmas())


### Just the word you can see by :
print(my_word.lemmas()[0].name())


### You can view the definition of the word
print(my_word.definition())

### you can view the sample examples of the given word in a sentence.
print(my_word.examples())


### you can view the part-of-speech tagged for the word by :
print(my_word.pos())


"""
    Commonly used pos tags : 
    n : noun
    a : adjective
    r : adverb
    v : verb

"""


## Hypernyms : more abstact (or) geniric
hypernym_list = my_word.hypernyms()
print(hypernym_list)


## Hyponyms : more specific
hyponym_list = my_word.hyponyms()
print(hyponym_list)


### let us take now another word to show the meronyms and holonyms

input_word_2 = "tree"
synsets_array_2 = wordnet.synsets(input_word_2)

my_word_2 = synsets_array_2[0]

#### part meronyms - obtains parts (here it shows parts of a tree)
print(my_word_2.part_meronyms())


#### substance meronyms - obtains substances
print(my_word_2.substance_meronyms())


## lets take the words atom and hydrogen

## Part holonyms of the word atom
print(wordnet.synset('atom.n.01').part_holonyms())


### substance holonyms of the word hydrogen
print(wordnet.synset('hydrogen.n.01').substance_holonyms())


#### Entailments

## let us test the with the example verb word eat. 

print(wordnet.synset('eat.v.01').entailments())


#### Similarity

"""
    You have seen that words in WordNet are linked to each other in different ways.
    Given a particular synset you can traverse the whole network to find related objects

    Recall that each synset has one or more parents (hypernyms). If two of them are
    linked to the same root they might have several hypernyms in common — that fact
    might mean that they are closely related. You can get to it with function
    lowest_common_hypernyms()
    
    
    You can also view the list of common hypernyms which two words share by
    common_hypernyms()
    
"""


### let's check the what all words hydrogen and atom have in common 

hydrogen = wordnet.synset('hydrogen.n.01')
atom = wordnet.synset('atom.n.01')

print(hydrogen.lowest_common_hypernyms(atom))

print(hydrogen.common_hypernyms(atom))


### Also you can check how specific a word is by analysing it's depth in hierarchy


## min_depth - returns The length of the shortest hypernym path from this synset to the root

print(wordnet.synset('weapon.n.01').min_depth())

print(wordnet.synset('tree.n.01').min_depth())



"""
    You can also view the similarities between two words and also you can list out
    all the synonyms and antonyms of a particular word.
    
    Those will be heavy topics which i will cover in the next tutorial.

"""


""" 
    That's the End of wordnets and synsets concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""



