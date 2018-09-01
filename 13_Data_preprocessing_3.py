# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

import nltk

# We will continue the visuaizing text part - 3

"""

$$  We shall make use of what we have learned so far in NLTK to generate a
    word cloud (also known as tag cloud). This is a fun and interesting
    way in which to visually represent how prominent certain words are in
    a text resource.

"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud

## let us take a sample piece of text

sample_text = "Hai how are you? I hope you are doing great. I feel good to code in python"

word_cloud = WordCloud().generate(sample_text)

# Using matplotlib to show the word cloud:
plt.imshow(word_cloud)
plt.axis("off")
plt.show()


## let's make above 3 lines which we will using more often as a function.

def plot_wordcloud(wordcloud):
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

"""

$$  You can see that there are few which are missing in the wordcloud plot,
    This is because the wordcloud module ignores stopwords by default.

    If we wish, we can specify our own set of stopwords, instead
    of the stopwords provided by default.

"""

word_cloud_stopwords = WordCloud(stopwords={'are', 'you','to'}).generate(sample_text)
plot_wordcloud(word_cloud_stopwords)

"""

$$  Another optional parameter for WordCloud is that of
    relative_scaling, which corresponds to how the size of the
    text in the word cloud scales based on the content.

    With relative_scaling=0, only the ranks of the words are
    considered. If we alter this to relative_scaling=1.0, then
    a word that appears twice as frequently will appear twice the
    size. By default, relative_scaling=0.5.

"""
sample_text_1 = "I like to solve problems in python python python"
word_cloud_relative_scaling = WordCloud(relative_scaling=1.0,
                      stopwords={'to', 'in',"I"}).generate(sample_text_1)
plot_wordcloud(word_cloud_relative_scaling)

"""
$$  Note that the word "python" in the world cloud is relatively much
    larger than the other words.

    Let us read in the raw content of the 1789 inaugural address of
    Washington and the 2009 address of Obama.

"""
washington = nltk.corpus.inaugural.raw('1789-Washington.txt')
obama = nltk.corpus.inaugural.raw('2009-Obama.txt')

# Word cloud for Washington:
wordcloud = WordCloud(relative_scaling=1.0).generate(washington)
plot_wordcloud(wordcloud)


# By default, if the WordCloud function is not provided a dictionary of stopwords,
# the WordCloud function will use the ones provided by default. This is okay, but 
# perhaps we notice in the word cloud generated above that words such as "every" 
# and "will" are present, but are not particularly useful in extracting information 
# into what makes Washington's address more unique over others. 

# What we can do then is to add in the words "every" and "will" into the set of 
# stopwords that the WordCloud function considers. 

from wordcloud import STOPWORDS
stopwords = set(STOPWORDS)
stopwords.add("every")
stopwords.add("will")
stopwords.add("us")

## word cloud for washington
wordcloud = WordCloud(stopwords=stopwords, relative_scaling=1.0).generate(washington)
plot_wordcloud(wordcloud)

# Word cloud for Obama:
wordcloud = WordCloud(stopwords=stopwords, relative_scaling=1.0).generate(obama)
plot_wordcloud(wordcloud)

""" 
    That's the End of Data preprocessing part -3 concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""