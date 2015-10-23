#testAnalogy.py
#argv[1]: space pkl file
#argv[2]: analogy test file
#EXAMPLE: python testAnalogy.py ../../spaces/wikipedia.pkl analogy_dataset.txt
#-------
from composes.utils import io_utils
from composes.utils import scoring_utils
from composes.similarity.cos import CosSimilarity
from composes.composition.weighted_additive import WeightedAdditive
import sys

add = WeightedAdditive(alpha = 1, beta = 1.2)
sub = WeightedAdditive(alpha = 1, beta = -1)

#read in a space
space = io_utils.load(sys.argv[1])


def computeAnalogy(w1,w2,w3):
	composed_space = sub.compose([(w1,w2, "step1")], space)
	composed_space2 = add.compose([("step1", w3, "step2")], (composed_space,space))
	guess=composed_space2.get_neighbours("step2", 1, CosSimilarity(),space)
	return guess


score=0

#read in test file
fname = sys.argv[2]
f=open(fname,'r')
flines=f.readlines()
f.close()

num_analogies_computed=0
for l in flines:
	l=l.rstrip('\n')
	if l[0] not in [':','/']:	
		fields=l.split()
		print fields
		try:
			guess=computeAnalogy(fields[0],fields[1],fields[3])
			print guess[0][0]
			num_analogies_computed+=1
			if guess[0][0] == fields[2]:
				score+=1
				print ">>> SCORE +1"				
		except:
			print "Analogy could no be computed"

print score,num_analogies_computed
print "OVERALL SCORE:",float(score)/float(num_analogies_computed)
