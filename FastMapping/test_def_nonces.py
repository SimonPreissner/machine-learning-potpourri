#This test the definitional nonces on sum.
#python3 test_def_nonces.py spaces/ukwac_reduced.txt /definitions/nonce.definitions.300.test

import sys
import re
import utils

background = sys.argv[1]
dataset = sys.argv[2]
mrr = 0.0

human_responses = []
system_responses = []

dm_dict = utils.readDM(background)

c = 0
f=open(dataset)
for l in f:
  if c < 1:
    c+=1
    continue
  else:
    fields=l.rstrip('\n').split('\t')
    nonce = fields[0]
    sentence = fields[1].replace("___","").split()
    print("--")
    print(nonce)
    print("SENTENCE:",sentence)

  if nonce in dm_dict:
    nonce_v = utils.centroid(dm_dict, sentence)
    nns = utils.sim_to_matrix(dm_dict, nonce_v, len(dm_dict)) 
    print("NEAREST NEIGHBOURS:",nns[:10])

    rr = 0
    n = 1
    for nn in nns:
      if nn == nonce:
        rr = n
      else:
        n+=1

    if rr != 0:
      mrr+=float(1)/float(rr)	
    print(rr,mrr)
    c+=1
  else:
    print("nonce not known...")

f.close()

print("Final MRR: ",mrr,c,float(mrr)/float(c))
