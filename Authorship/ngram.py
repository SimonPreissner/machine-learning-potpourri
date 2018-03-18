import sys

n=4

def record_ngrams(filename):
  ngrams={}
  f=open(filename,'r')
  for l in f:
    l=l.rstrip('\n')
    for i in range(len(l)-n):
      ngram=l[i:i+n]
      if ngram in ngrams:
        ngrams[ngram]+=1
      else:
        ngrams[ngram]=1
  f.close()
  return ngrams

ngrams=record_ngrams(sys.argv[1])

for g in sorted(ngrams, key=ngrams.get, reverse=True):
  print g+"\t"+str(ngrams[g])
