import numpy as np
from math import sqrt

def readDM(dm_file):
    dm_dict = {}
    version = ""
    with open(dm_file) as f:
        dmlines=f.readlines()
    f.close()

    #Make dictionary with key=row, value=vector
    for l in dmlines:
        items=l.rstrip().split()
        row=items[0]
        vec=[float(i) for i in items[1:]]
        vec=np.array(vec)
        dm_dict[row]=vec
    return dm_dict

def mk_training_matrices(pairs, en_dimension, cat_dimension, english_space, catalan_space):
    en_mat = np.zeros((len(pairs),en_dimension)) 
    cat_mat = np.zeros((len(pairs),cat_dimension))
    c = 0
    for p in pairs:
        en_word,cat_word = p.split()
        en_mat[c] = english_space[en_word]   
        cat_mat[c] = catalan_space[cat_word]   
        c+=1
    return en_mat,cat_mat


def linalg(mat_english,mat_catalan):
    w = np.linalg.lstsq(mat_english,mat_catalan)[0] # obtaining the parameters
    #print(w.shape)
    return w


def cosine_similarity(v1, v2):
    if len(v1) != len(v2):
        return 0.0
    num = np.dot(v1, v2)
    den_a = np.dot(v1, v1)
    den_b = np.dot(v2, v2)
    return num / (sqrt(den_a) * sqrt(den_b))


def neighbours(dm_dict,vec,n):
    cosines={}
    c=0
    for k,v in dm_dict.items():
        cos = cosine_similarity(vec, v)
        cosines[k]=cos
        c+=1
    c=0
    neighbours = []
    for t in sorted(cosines, key=cosines.get, reverse=True):
        if c<n:
             #print(t,cosines[t])
             neighbours.append(t)
             c+=1
        else:
            break
    return neighbours



'''Read semantic spaces'''
english_space = readDM("data/english.subset.dm")
catalan_space = readDM("data/catalan.subset.dm")

'''Read all word pairs'''
all_pairs = []
f = open("data/pairs.txt")
for l in f:
    l = l.rstrip('\n')
    all_pairs.append(l)
f.close()

'''Make training/test fold'''
training_pairs = all_pairs[:100]
test_pairs = all_pairs[101:]

'''Make training/test matrices'''
en_mat, cat_mat = mk_training_matrices(training_pairs, 400, 300, english_space, catalan_space)
params = linalg(en_mat,cat_mat)

'''Test'''

'''Sanity check -- is the regression matrix retrieving the training vectors?'''
#print(training_pairs[0])
#en, cat = training_pairs[0].split()
#predict = np.dot(params.T,english_space[en])
#print(predict[:20])
#print(catalan_space[cat][:20])

'''Loop through test pairs and evaluate translations'''
score = 0
for p in test_pairs:
    en, cat = p.split()
    predicted_vector = np.dot(params.T,english_space[en])
    #print(predicted_vector)
    nearest_neighbours = neighbours(catalan_space,predicted_vector,5)
    if cat in nearest_neighbours:
        score+=1
        print(en,cat,nearest_neighbours,"1")
    else:
        print(en,cat,nearest_neighbours,"0")

print("Precision:",score/len(test_pairs))

