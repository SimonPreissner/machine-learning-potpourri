#spearman.py
#argv[1]: space pkl file
#argv[2]: gold standard sim file
#EXAMPLE: python spearman.py ../../spaces/wikipedia.pkl MEN_dataset_natural_form_full|egrep -v "Row string"
#-------
from composes.utils import io_utils
from composes.utils import scoring_utils
from composes.similarity.cos import CosSimilarity
import sys

#read in a space
my_space = io_utils.load(sys.argv[1])

#compute similarities of a list of word pairs
fname = sys.argv[2]
word_pairs = io_utils.read_tuple_list(fname, fields=[0,1,2])

predicted=[]
gold=[]
cos=0
for wp in word_pairs:
	try:
		cos=my_space.get_sim(wp[0],wp[1], CosSimilarity())
		if cos > 0:
			#print wp[0],wp[1],cos
			predicted.append(cos)
			gold.append(wp[2])
	except:
		print "Couldn't measure cosine..."


#compute correlations
print "Spearman"
print scoring_utils.score(gold, predicted, "spearman")
print "Pearson"
print scoring_utils.score(gold, predicted, "pearson")
