# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

"""
    Tutorial about : Wu palmer similarity, lch similarity
    
    Similiarity : It basically means a measure which shows how 
                  much two words are similar to each other.

"""

#### WU palmer similarity

## importing packages

from nltk.corpus import wordnet

## cake, loaf, bread

syn_arr1 = wordnet.synsets('cake')
syn_arr2 = wordnet.synsets('loaf')
syn_arr3 = wordnet.synsets('bread')

print(syn_arr1)

### we consider the first one
cake = syn_arr1[0]

print(syn_arr2)

loafb = syn_arr2[0]
loaf = syn_arr2[1]

print(syn_arr3)
bread = syn_arr3[0]


## Wu - Palmer similarity - based on hypernym tree.

cake.wup_similarity(loaf)
## 30.7 % similar

cake.wup_similarity(loafb)
## 26.6 % similar

loaf.wup_similarity(loafb)
## 71.4 # similar

bread.wup_similarity(loafb)
## 94.1 % similarity

"""Basically WU palmer similarity is based on Hypernym Tree

    Below is something which happens,,,in a part of calculation
"""


print(loaf.hypernyms())

## chossing the first element

ref =  loaf.hypernyms()[0]

loaf.shortest_path_distance(ref)
## 1 unit away

bread.shortest_path_distance(ref)
## 2 units away

loafb.shortest_path_distance(ref)
## 3 units away

cake.shortest_path_distance(ref)
## 8 units away

"""
You can see that bread and loafb are more nearer than
loaf and loafb,,,,that is why it has got 90 % and 71 %
results.

but this is not only the thing which happens in background
it ivloves much more complex calculation, but this gives an
idea of what is happening

"""

## 

catarr = wordnet.synsets('cat')
dogarr = wordnet.synsets('dog')

doi = dogarr[0]
coi = catarr[0]

## just do wu palmer similarity

doi.wup_similarity(coi)
## 85 % similar

## pathsimilarity - no of nodes in the shortest path b/w tow words

doi.path_similarity(coi)
## 0.2

## to chekc the range
doi.path_similarity(doi)
## max - 1.0



### leacock chodorow - LCH similarity

doi.lch_similarity(coi)
## 2.08

# to check the range
doi.lch_similarity(doi)
## max range - 3.6375

"""
LCH similarity is based on two concepts :
    1. length of the path b/w two words,
    2. maximum depth of the taxanomy
    
    also it involves a logorithm equations

"""


"""

$$  There are many more other similarities, but these are used
    more in real world.

"""

""" 
    That's the End of similarities concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""







