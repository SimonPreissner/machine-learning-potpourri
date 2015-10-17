#getcofreqs.py
#USAGE: python getcofreqs [lemma file]
#EXAMPLE: python getcofreqs lemmas.txt
#_______

import sys

win_one_side=int(sys.argv[2])	#How many words on either side of the target? i.e. 5 corresponds to a 11_word window
win_both_sides=int(win_one_side) * 2
win_full=win_both_sides + 1

cofreqs_dict = {}
freqs_dict = {}

#Shift window by one word
def shiftwindow(w):
  for c in range(win_both_sides):
    w[c]=w[c+1]			#Shift window up to last element, which remains the same (to be replaced by reading new line in lemma file)

#Get cofreqs, and while we're at it, count words
def getcofreqs(w):
  for c in range(win_full):
    if c is not win_one_side:			#We don't count co-occurrences of the word with itself
      co=w[win_one_side]+" "+w[c]
      #print co
      if co in cofreqs_dict:
        cofreqs_dict[co]+=1
      else:
	cofreqs_dict[co] = 1
    else:
      if w[c] in freqs_dict:
        freqs_dict[w[c]]+=1
      else:
        freqs_dict[w[c]]=1
  

#open the lemma file
filename=sys.argv[1]
lemmas=open(filename,"r")

window=[]

#Initialise window
for c in range(win_full):
	window.append('#')

for l in lemmas:
	#print window
	shiftwindow(window)
	#print window
	window[win_both_sides]=l.rstrip()	#Replace last element in window with new lemma line (last part of shift action)
	#print window
	getcofreqs(window)

lemmas.close()

fcofreqs=open(sys.argv[1]+".sm",'w')
for el in cofreqs_dict:
  fcofreqs.write(el+" "+str(cofreqs_dict[el])+"\n")
fcofreqs.close()

ffreqs=open(sys.argv[1]+".freqs",'w')
for w in sorted(freqs_dict, key=freqs_dict.get, reverse=True):
  ffreqs.write(str(freqs_dict[w])+" "+w+"\n")
ffreqs.close()
