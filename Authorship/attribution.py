import os
import sys
import math
from utils import process_document_words, process_document_ngrams

ngram_length = 4
alpha = 0.000001

def process_collection():
    '''Take table of authors and associated document frequencies
    to calculate probability of each author.'''
    author_probabilities = {}
    author_freqs = {}
    author_wordcounts = {}
    files = [os.path.join('./data/training/', f) for f in os.listdir('./data/training/') if os.path.isfile(os.path.join('./data/training/', f))]
    num_documents = len(files)
    for f in files:
        #author, doc_length, words = process_document_words(f)
        author, doc_length, words = process_document_ngrams(f, ngram_length)
        if author in author_probabilities:
            author_probabilities[author] += 1
            author_wordcounts[author] += doc_length
            for w,f in words.items():
                if w in author_freqs[author]:
                    author_freqs[author][w] += f
                else:
                    author_freqs[author][w] = f
        else:
            author_probabilities[author] = 1
            author_wordcounts[author] = doc_length
            author_freqs[author] = words
    for author,doc_freq in author_probabilities.items():
        author_probabilities[author] = doc_freq / num_documents
    #print(author_probabilities,author_wordcounts, author_freqs.keys())
    return author_probabilities, author_wordcounts, author_freqs


def naive_bayes(test_words, author_freqs, author_probabilities, author):
    '''Run Naive Bayes with test_ngrams = new text\
    and author = particular value for author.'''
    nb=0
    for w,f in test_words.items():  # For each word in the test document
        w_freq = 0
        if w in author_freqs[author]:
            w_freq = author_freqs[author][w]
        for i in range(f):
            '''Add to score the log of P(word|author)'''
            nb += math.log((w_freq + alpha) / (author_wordcounts[author] * (1 + alpha)))
    nb += math.log(author_probabilities[author])
    print("NB score for author",author,":",nb)


#Training
author_probabilities, author_wordcounts, author_freqs = process_collection()

#Testing
#author, doc_length, words = process_document_words(sys.argv[1])
author, doc_length, words = process_document_ngrams(sys.argv[1], ngram_length)

for a in list(author_probabilities.keys()):
     naive_bayes(words, author_freqs, author_probabilities, a)
