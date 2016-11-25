#hyponymy returns clarkeDE and invCL hyponymy measures for word pair
#USAGE: python hyponymy.py [dm space file] [word1] [word2]
#EXAMPLE: python hyponymy.py ../spaces/wikipedia.dm horse animal
#-------
from composes.utils import io_utils
from composes.similarity.cos import CosSimilarity
import math
import sys


DM=open(sys.argv[1],"r")
DM_lines=DM.readlines()
DM.close()

dic={}

for l in DM_lines:
	pair=l.rstrip("\n").split('\t')
	#print pair[0],"::",pair[1:]
	dic[pair[0]]=pair[1:]


h1=dic[sys.argv[2]]
h2=dic[sys.argv[3]]

iter=0

sum_mins=0
sum_h1=0
sum_h2=0

for weight1 in h1:
	#print sys.argv[2],w
	weight2=h2[iter]
	sum_mins+=min(float(weight1),float(weight2))
	sum_h1+=float(weight1)
	sum_h2+=float(weight2)
	iter+=1

clarkeDE=sum_mins/sum_h1
clarkeDEinv=sum_mins/sum_h2

invCL=math.sqrt(clarkeDE*(1-clarkeDEinv))

print sys.argv[2],sys.argv[3],"clarkeDE:",clarkeDE,"invCL:",invCL

