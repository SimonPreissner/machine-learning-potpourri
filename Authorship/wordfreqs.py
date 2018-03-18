import sys

def record_words(filename):
  words={}
  f=open(filename,'r')
  for l in f:
    l=l.rstrip('\n')
    for w in l.split():
      if w in words:
        words[w]+=1
      else:
        words[w]=1
  f.close()
  return words

words=record_words(sys.argv[1])

for g in sorted(words, key=words.get, reverse=True):
  print g+"\t"+str(words[g])
