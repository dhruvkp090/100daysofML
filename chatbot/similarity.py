'''
Author: Dhruv Kumar Patwari (dhruvk090@gmail.com)

Description: This file is used to check the similarity between two sentences/Questions.


'''

import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def similarity(input_question, databade_question):
    rawData = input_question.lower()
    sent_tokens = nltk.sent_tokenize(rawData)
    sent_tokens.append(databade_question.lower())
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf < 0.2):
        return False
    else:
        return True
