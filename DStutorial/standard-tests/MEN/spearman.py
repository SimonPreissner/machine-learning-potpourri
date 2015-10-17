#spearman.py
#argv[1]: space pkl file
#argv[2]: gold standard sim file
#EXAMPLE: python spearman.py ../../data/pride/out/CORE_SS.pride.ppmi.row.pkl MEN_dataset_lemma_form_full_gold.txt|egrep -v "Row string| 0.0$"
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
for wp in word_pairs:
	cos=my_space.get_sim(wp[0],wp[1], CosSimilarity())
	if cos > 0:
		#print wp[0],wp[1],cos
		predicted.append(cos)
		gold.append(wp[2])

#predicted = my_space.get_sims(word_pairs, CosSimilarity())

#compute correlations
#gold = io_utils.read_list(fname, field=2)
print "Spearman"
print scoring_utils.score(gold, predicted, "spearman")
print "Pearson"
print scoring_utils.score(gold, predicted, "pearson")
