from numpy import *
import re
from matplotlib import cm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

stopwords=["","(",")","a","about","an","and","are","around","as","at","away","be","become","became","been","being","by","did","do","does","during","each","for","from","get","have","has","had","her","his","how","i","if","in","is","it","its","made","make","many","most","of","on","or","s","some","that","the","their","there","this","these","those","to","under","was","were","what","when","where","who","will","with","you","your"]

num_dim=400

########################################################
# Normalise array
########################################################

def normalise(v):
    norm=linalg.norm(v)
    if norm==0: 
       return v
    return v/norm

#################################################
# Read dm file
#################################################

def readDM(dm_file):
	dm_dict = {}
	with open(dm_file) as f:
		dmlines=f.readlines()
		f.close()

	#Make dictionary with key=row, value=vector
	for l in dmlines:
		items=l.rstrip('\n').split(' ')
		row=items[0]
		vec=[float(i) for i in items[1:]]
		#dm_dict[row]=normalise(vec)
		dm_dict[row]=vec
	return dm_dict


#############################################
# Cosine function
#############################################

def cosine_similarity(peer_v, query_v):
    if len(peer_v) != len(query_v):
        raise ValueError("Peer vector and query vector must be "
                         " of same length")
    num = dot(peer_v, query_v)
    den_a = dot(peer_v, peer_v)
    den_b = dot(query_v, query_v)
    return num / (sqrt(den_a) * sqrt(den_b))

##############################################
# Make distribution for sentence by adding
##############################################

def centroid(dm_dict,words):
    # Only retain arguments which are in the distributional semantic space
    vecs_to_add = []
    for w in words:
        w=w.lower()
        if w not in stopwords:
            if w in dm_dict:
                #print "Adding word",
                vecs_to_add.append(w)
            else:
                print("UNKNOWN WORD:",w)

    vbase = array([])
    # Add vectors together
    if len(vecs_to_add) > 0:
        # Take first word in vecs_to_add to start addition
        vbase = array(dm_dict[vecs_to_add[0]])
        for item in range(1, len(vecs_to_add)):
            vbase = vbase+array(dm_dict[vecs_to_add[item]])
    vbase=normalise(vbase)
    return vbase

def sim_to_matrix(dm_dict, vec, n):
    """ Compute similarities and return top n """
    cosines = {}
    for k, v in dm_dict.items():
        cos = cosine_similarity(array(vec), array(v))
        cosines[k] = cos

    topics = []
    topics_s = ""
    c = 0
    for t in sorted(cosines, key=cosines.get, reverse=True):
        if c < n:
            if t.isalpha() and t not in stopwords:
                #print(t,cosines[t])
                topics.append(t)
        else:
            break
        c+=1
    return topics


#######################################
# Visualisation functions
#######################################

def make_figure(m_2d, labels):
    cmap = cm.get_cmap('nipy_spectral')

    existing_m_2d = pd.DataFrame(m_2d)
    existing_m_2d.index = labels
    existing_m_2d.columns = ['PC1','PC2']
    existing_m_2d.head()

    ax = existing_m_2d.plot(kind='scatter', x='PC2', y='PC1', figsize=(30,18), c=range(len(existing_m_2d)), colormap=cmap, linewidth=0, legend=False)
    ax.set_xlabel("A dimension of meaning")
    ax.set_ylabel("Another dimension of meaning")

    for i, word in enumerate(existing_m_2d.index):
        #print(word+" "+str(existing_m_2d.iloc[i].PC2)+" "+str(existing_m_2d.iloc[i].PC1))
        ax.annotate(
            word,
            (existing_m_2d.iloc[i].PC2, existing_m_2d.iloc[i].PC1), color='black', size='large', textcoords='offset points')

    fig = ax.get_figure()
    return fig


def run_PCA(dm_dict, words, savefile):
    m = []
    labels = []
    for w in words:
        labels.append(w)
        m.append(dm_dict[w])
    pca = PCA(n_components=2)
    pca.fit(m)
    m_2d = pca.transform(m)
    png = make_figure(m_2d,labels)
    cax = png.get_axes()[1]
    cax.set_visible(False)
    #png.savefig(savefile)
    plt.show()

