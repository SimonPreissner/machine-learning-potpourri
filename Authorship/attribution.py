import sys
import math

vocab={}
ngrams_dicts=[]
alpha=0.0001


def fill_vocab(author_ngrams):
    for ngram,freq in author_ngrams.items():
      if ngram in vocab:
        vocab[ngram]+=freq
      else:
        vocab[ngram]=freq



def read_ngrams(filename):
  ngrams={}
  f=open(filename,'r')
  for l in f:
    l=l.rstrip('\n')
    ngram=l.split("\t")[0]
    freq=int(l.split("\t")[1])
    ngrams[ngram]=freq
  f.close()
  fill_vocab(ngrams)
  return ngrams

def naive_bayes(test_ngrams,author):
  nb=0
  for ngram,freq in test_ngrams.items():
    if ngram in ngrams_dicts[author]:
      for i in range(freq):
        nb=nb+math.log(ngrams_dicts[author][ngram])
    else:
      if ngram in vocab:
        for i in range(freq):
          nb=nb+math.log(float(alpha)/float(vocab[ngram]+alpha))
  print nb



#Training
#ngrams_dicts.append(read_ngrams("wind.ngrams"))
#ngrams_dicts.append(read_ngrams("junglebook.ngrams"))
#ngrams_dicts.append(read_ngrams("alice.ngrams"))
#ngrams_dicts.append(read_ngrams("pride.ngrams"))

ngrams_dicts.append(read_ngrams("wind.words"))
ngrams_dicts.append(read_ngrams("junglebook.words"))
ngrams_dicts.append(read_ngrams("alice.words"))
ngrams_dicts.append(read_ngrams("pride.words"))

#Testing
#test_ngrams=read_ngrams("emma.ngrams")
test_ngrams=read_ngrams("emma.words")

#Calculate ngram probabilities for each author in ngrams_dicts
for d in ngrams_dicts:
  for ngram,freq in d.items():
    d[ngram]=float(freq+alpha)/float(vocab[ngram]+alpha)

naive_bayes(test_ngrams,0)
naive_bayes(test_ngrams,1)
naive_bayes(test_ngrams,2)
naive_bayes(test_ngrams,3)
