# -*- coding: utf-8 -*-
"""
Created on Sat Sep 1 00:00:00 2018

@author: Nikhil
"""

## importing all necessary libraries
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from string import punctuation

## Creating a list comprises of english stopwords and Punctuation.
eng_sw = stopwords.words('english') + list(punctuation)

"""
$$  Here we are using the dataset from the nltk library which was 
    downloaded in the beggining, from the corpora inside the movie_reviws
    section. 
    
    Go and check it out ,,,where you've downloaded the nltk data.
    
    There will 1000 neg and pos revews, categorised into two folders namely
    neg and pos.

"""
all_data_1 = []
all_data_1 = [(list(movie_reviews.words(file_name)), folder_name)
             for folder_name in movie_reviews.categories()
             for file_name in movie_reviews.fileids(folder_name)]

"""
$$  For few people the above one line code may not strike as fast,
    so i have breakup the code in regular format, and will explain 
    about each line.

"""

all_data = []

for folder_name in movie_reviews.categories():
    for file_name in movie_reviews.fileids(folder_name):
        all_data.append((list(movie_reviews.words(file_name)), folder_name))
        
"""
$$  Here the fist for loop is to iterate through the sub folders in
    the movie_reviews data under nlt.corpora...
    the two sub folders are pos and neg
    
    and the second for loop is to iterate through each and every file
    under two 2 categories...there will be total 1000 files in each
    categories which brings upto total 2000 files.
    
    and the third statement is creating a tuple of words in a particular
    file and its corresponding category in a list format and appending 
    to all_data.

"""

## shuffling all the data in the all_data so that they won't follow any order

random.shuffle(all_data)

"""
$$  Let's make two lists both will have the same data, but the difference
    is one will have words including stopwords and punctuation, and 
    another one doesn't
    
"""
cleaned_all_words = []
all_words_raw = []

for w in movie_reviews.words():
    all_words_raw.append(w.lower())

for w in movie_reviews.words():
    if w not in eng_sw:
        cleaned_all_words.append(w.lower())
        
"""
$$  There you can see that all_words_raw contains both stop words and
    punctuation but the cleaned_all_words doesn't. Why we do this 
    is because we don't want to have those stopwords and punctuation
    in our training data, otherwise it will effect the accuracy
    of your classifier.

"""

cleaned_all_words = nltk.FreqDist(cleaned_all_words)
all_words_raw = nltk.FreqDist(all_words_raw)

"""
$$  If you've followed my tutorila you must have an idea about the FreqDist..

    FreDist : Basically, it just gives the word and their count of appearing
              how many times in a dictionary format.
              
    Obviously, we won't need all those words to find the features, so
    what we gonna do is to take the top 3000 words and then check 
    which word in most common in negative and positive reviews.

"""


req_features = list(cleaned_all_words.keys())[:3000]
req_features_raw = list(all_words_raw.keys())[:3000]

def take_features(input_given):
    input_given_words = set(input_given)
    wanted_features = {}
    for word in req_features:
        wanted_features[word] = (word in input_given_words)

    return wanted_features

#print((take_features(movie_reviews.words('pos/cv001_18431.txt'))))

resulted_features = [(take_features(review), sub_category) for (review, sub_category) in all_data]

"""
$$  So, Here we have created a function of take the features from a piece
    of data which is passed to it.
    First it takes the data and then takes out the unique words from that
    data and passes it through a loop which checks whether the word is present
    in the top 3000 words which we have got earlier and saves it in a dictionary
    format.
    
    The resulted_features contains all the movie_reviews data of 2000 files,
    in a list format, which contains tuple of a dict and str, the dict contains
    all the words in a particular file as key and whether that word exists in 
    top 3000 words or not, and the str consists of the sub_category of the folder
    i.e.., either a pos or neg.
    
    Now since we have got the data we will split the data into training data
    and testing data and predict the accuracy using NaiveBayesclassifier.
    
    We need not to import and special libraries, since the nltk itself
    contains the classifiers.

"""


train_data = resulted_features[:1900]


test_data = resulted_features[1900:]

naivebayes_classifier = nltk.NaiveBayesClassifier.train(train_data)

print("Naive bayes_classifier accuracy :",(nltk.classify.accuracy(naivebayes_classifier, test_data)))

"""
$$  So, here i got 76% accuracy which is quite good, it might be different for you, 
    now we will check with other classifiers of how it will perform.
    
    Here we will take the top 20 most informative features, what it basically 
    shows is that, it will show a word and compares between pos and neg category
    and their respective ratio.
    for example you can see that the word idiotic has came in negative reviews more
    times compared to positive reviews.

"""
naivebayes_classifier.show_most_informative_features(20)

"""
$$  Now we will talk about saving a classifier, so that we need not to train the data
    everytime when we want to use that classifier multiple times for testing purpose
    and not wasting the time.
    
    I will not run that coded and i will keep that in comment section, if you
    want you can use it.

"""
## importing necessary package

#import pickle
#save_naivebayes_classifier = open("naivebayes_classifier_pickle.pickle","wb")
#pickle.dump(naivebayes_classifier, save_naivebayes_classifier)
#save_naivebayes_classifier.close()

"""
$$  The code above will saves the naivbayes_classifier in a pickle file.
    
    If you want to use the saved naivbayes_classifier use the below code
    and then directly test your data, skipping the training process.
    
"""

#naivebayes_classifier_pickle_file = open("naivebayes_classifier_pickle.pickle", "rb")
#naivebayes_classifier = pickle.load(naivebayes_classifier_pickle_file)
#naivebayes_classifier_pickle_file.close()

"""
$$  Now, we will take all the other sklearn classifiers available, and test
    the accuracy accordingly.

"""

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.linear_model.stochastic_gradient import SGDClassifier

## Multinomial Naivebayes classifier
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(train_data)
print("Multinomial Naivebayes classifier accuracy :", (nltk.classify.accuracy(MNB_classifier, test_data)))

## Bernoulli Naivebayes classifier
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(train_data)
print("Bernoulli Naivebayes classifier accuracy :", (nltk.classify.accuracy(BernoulliNB_classifier, test_data)))

## Logistic Regression
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(train_data)
print("Logistic Regression accuracy :", (nltk.classify.accuracy(LogisticRegression_classifier, test_data)))

## Stochastic Gradient descent classifier
SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(train_data)
print("Stochastic Gradient descent classifier accuracy :", (nltk.classify.accuracy(SGDClassifier_classifier, test_data)))

## Support vector classifier
SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(train_data)
print("Support vector classifier accuracy :", (nltk.classify.accuracy(SVC_classifier, test_data)))

## Linear Support vector classifier
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(train_data)
print("Linear Support vector classifier accuracy :", (nltk.classify.accuracy(LinearSVC_classifier, test_data)))

## Nu Support vector classifier
NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(train_data)
print("Nu Support vector classifier accuracy :", (nltk.classify.accuracy(NuSVC_classifier, test_data)))

"""
$$  So here you can see there are in my case all the classifiers have worked
    pretty good with an accuracy of 80% in all classifiers. 
    
    From all this classifiers you can select one and choose anyone of that,
    or you can make a group classifier which kind of takes input from all the
    classifiers and provide the results based on the majority of what all the
    other classifiers have predicted.

"""


""" 
    That's the End of Sklean classifiers analysis concept.
    If you have any questions or suggestions regarding the concept,
    feel free to contact me via nikhil.ss4795@gmail.com
    
"""