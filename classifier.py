
# coding: utf-8
# Heavily inspired by/stolen from Prof. Matthew Stones "using-classifiers.py" example

import nltk, re
from nltk.corpus import movie_reviews


# For this classification problem, we represent a text snippet as a collection
# of features.  The features in a document list the _informative_ words that
# _occur_ in the document.  There are a couple choices here that are not obvious
# but are important.

# I have packaged up the reasoning in a function called `compute_best_features`,
# which we'll use both to build our sentiment analyzer and our dialogue act tagger.

def compute_best_features(labels, feature_generator, n) :
    feature_fd = nltk.FreqDist()
    label_feature_fd = nltk.ConditionalFreqDist()

    for label in labels:
        for feature in feature_generator(label) :
            feature_fd[feature] += 1
            label_feature_fd[label][feature] += 1

    counts = dict()
    for label in labels:
        counts[label] = label_feature_fd[label].N()
    total_count = sum(counts[label] for label in labels)

    feature_scores = {}

    for feature, freq in feature_fd.iteritems():
        feature_scores[feature] = 0.
        for label in labels :
            feature_scores[feature] +=             nltk.BigramAssocMeasures.chi_sq(label_feature_fd[label][feature],
                                            (freq, counts[label]),
                                            total_count)

    best = sorted(feature_scores.iteritems(), key=lambda (f,s): s, reverse=True)[:n]
    return set([f for f, s in best])


# This block of code computes the features and defines a function to extract the
# features corresponding to a list of words. You won't want to execute part of
# this block - it's a coherent unit of code - so it's commented inline.  It takes
# a little while to run because it's going through the whole corpus, but it's
# not so slow for right now that it's worth pickling the best_word_list and
# loading it in later.

stop_word_file = "stop-word-list.txt"
with open(stop_word_file) as f :
    stop_words = set(line.strip() for line in f)

def candidate_feature_word(w) :
    return w not in stop_words and re.match(r"^[a-z](?:'?[a-z])*$", w) != None

def movie_review_feature_generator(category) :
    return (word
            for word in movie_reviews.words(categories=[category])
            if candidate_feature_word(word))

best_sentiment_words = compute_best_features(['pos', 'neg'], movie_review_feature_generator, 2000)

def best_sentiment_word_feats(words):
    return dict([(word, True) for word in words if word in best_sentiment_words])


# We're going to explore a few ways of doing the classification, so we'll put
# some infrastructure in place.  First, we load in all the data as a
# `training_corpus` of `(word_list, category)` pairs.  Then, we create a dummy
# Python class called `Experiment` that will let us package together comparable
# values made using different instantiations of the features and learning
# algorithms and play with the results.

training_corpus = [(list(movie_reviews.words(fileid)), category)
                   for category in movie_reviews.categories()
                   for fileid in movie_reviews.fileids(category)]

class Experiment(object) :
    pass


# Our first experiment uses the `best_word_feats` that we've just computed - it
# understands the sentiment in the text based on the most informative words that
# occur.
#
# Here's the basic strategy for building and using the classifier:
# - Create a list of training pairs for the learner of the form
#     `(feature dictionary, category label)`
# - Train a naive Bayes classifier on the training data
# - Write a feature extractor that will take raw text into a feature dictionary
# - Write a classification function that will predict the sentiment of raw text
#
# This also takes a moment to run as it scans through the corpus, makes the
# features, aggregates them into counts, and uses the counts to build a
# statistical model.  Again, if it bugs you, you could pickle the classifier.

expt1 = Experiment()
expt1.feature_data = [(best_sentiment_word_feats(d), c) for (d,c) in training_corpus]
expt1.opinion_classifier = nltk.NaiveBayesClassifier.train(expt1.feature_data)
expt1.preprocess = lambda text : best_sentiment_word_feats([w.lower() for w in re.findall(r"\w(?:'?\w)*", text)])
expt1.classify = lambda text : expt1.opinion_classifier.classify(expt1.preprocess(text))


def best_bigram_word_feats(words, score_fn=nltk.BigramAssocMeasures.chi_sq, n=200):
    bigram_finder = nltk.BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    d = dict([(bigram, True) for bigram in bigrams])
    d.update(best_sentiment_word_feats(words))
    return d

expt2 = Experiment()
expt2.feature_data = [(best_bigram_word_feats(d), c) for (d,c) in training_corpus]
expt2.opinion_classifier = nltk.NaiveBayesClassifier.train(expt2.feature_data)
expt2.preprocess = lambda text : best_bigram_word_feats([w.lower() for w in re.findall(r"\w(?:'?\w)*", text)])
expt2.classify = lambda text : expt2.opinion_classifier.classify(expt2.preprocess(text))



# Now we turn to dialogue act tagging.  NLTK comes with [a collection of text
# chat utterances that were collected by Craig Martell and colleagues at the
# Naval Postgraduate School.][1]  These items have been hand annotated with a
# number of categories indicating the different roles the utterances play in a
# conversation.  The list of tags appears here.  The best way to understand what
# the tags mean is to see an example utterance from each class, so running this
# code also prints out some examples.  The examples also show what the corpus is
# like -- including the way user names have been anonymized...
#
# [1]:http://faculty.nps.edu/cmartell/NPSChat.htm
#

chat_utterances = nltk.corpus.nps_chat.xml_posts()

dialogue_acts = ['Accept',
                 'Bye',
                 'Clarify',
                 'Continuer',
                 'Emotion',
                 'Emphasis',
                 'Greet',
                 'nAnswer',
                 'Other',
                 'Reject',
                 'Statement',
                 'System',
                 'whQuestion',
                 'yAnswer',
                 'ynQuestion']
'''
for a in dialogue_acts :
    for u in chat_utterances :
        if u.get('class') == a:
            print "Example of {}: {}".format(a, u.text)
            break
'''

# This kind of language is pretty different from the edited writing that many
# NLP tools assume.  Obviously, for machine learning, it hardly matters what the
# input to the classifier is.  But it does pay to be smarter about dividing the
# text up into its tokens (the words or other meaningful elements).  So we'll
# load in [the tokenizer that Chris Potts wrote][1] to analyze twitter feeds.
#  Some of the things that it does nicely:
# - Handles emoticons, hashtags, twitter user names and other items that mix
#    letters and punctuation
# - Merges dates, URLs, phone numbers and similar items into single tokens
# - Handles ordinary punctuation in an intelligent way as well
#
# [1]:http://sentiment.christopherpotts.net/tokenizing.html

# In[11]:

from happyfuntokenizing import Tokenizer
chat_tokenize = Tokenizer(preserve_case=False).tokenize


# Now we set up the features for this data set.  The code is closely analogous
#to what we did with the sentiment classifier earlier.  The big difference is
# the tokenization and stopword elimination.  Content-free words and weird
# punctuation bits like `what` and `:)` are going to be very important for
# understanding what dialogue act somebody is performing so we need to keep
# those features around!

# In[12]:

def chat_feature_generator(category) :
    return (word
            for post in chat_utterances
            if post.get('class') == category
            for word in chat_tokenize(post.text))

best_act_words = compute_best_features(dialogue_acts, chat_feature_generator, 2000)

def best_act_word_feats(words):
    return dict([(word, True) for word in words if word in best_act_words])

def best_act_words_post(post) :
    return best_act_word_feats(chat_tokenize(post.text))


# Here again is the setup to build the classifier and apply it to novel text.  
# No surprises here.

# In[13]:

expt3 = Experiment()
expt3.feature_data = [(best_act_words_post(p), p.get('class')) for p in chat_utterances]
expt3.act_classifier = nltk.NaiveBayesClassifier.train(expt3.feature_data)
expt3.preprocess = lambda text : best_act_word_feats(chat_tokenize(text))
expt3.classify = lambda text : expt3.act_classifier.classify(expt3.preprocess(text))


# Here's a little glimpse into what this classifier is paying attention to.

# In[14]:

# expt3.act_classifier.show_most_informative_features(20)



