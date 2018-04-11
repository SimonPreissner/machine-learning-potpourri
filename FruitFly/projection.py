import sys
import utils
import MEN
import numpy as np

if len(sys.argv) != 3 or sys.argv[1] not in ("bnc","wiki"):
    print("USAGE: python3 projection.py bnc|wiki [num Kenyon cells]")
    sys.exit() 

if sys.argv[1] == "bnc":
  data = "data/BNC-MEN.dm"
  MEN_annot = "data/MEN_dataset_lemma_form_full"
else:
  data = "data/wiki_all.dm"
  MEN_annot = "data/MEN_dataset_natural_form_full"

english_space = utils.readDM(data)
PN_size = len(english_space.popitem()[1])
KC_size = int(sys.argv[2])
print("SIZES PN LAYER:",PN_size,"KC LAYER:",KC_size)

projection_layer = np.zeros(PN_size)
kenyon_layer = np.zeros(KC_size)
projection_functions = []

print("Creating",KC_size,"random projections...")
projection_functions = {}
for cell in range(KC_size):
    activated_pns = np.random.randint(PN_size, size=6)
    projection_functions[cell] = activated_pns


def projection(projection_layer):
    kenyon_layer = np.zeros(KC_size)
    for cell in range(KC_size):
        activated_pns = projection_functions[cell]
        for pn in activated_pns:
            kenyon_layer[cell]+=projection_layer[pn]
    return kenyon_layer

def hash_kenyon(kenyon_layer):
    #print(kenyon_layer[:100])
    kenyon_activations = np.zeros(KC_size)
    top = int(5 * KC_size / 100)
    activated_kcs = np.argpartition(kenyon_layer, -top)[-top:]
    for cell in activated_kcs:
        kenyon_activations[cell] = 1
    return kenyon_activations

def hash_input(word):
    projection_layer = english_space[word]
    kenyon_layer = projection(projection_layer)
    return hash_kenyon(kenyon_layer)

english_space_hashed = {}

for w in english_space:
    hw = hash_input(w)
    english_space_hashed[w]=hw

#print(utils.neighbours(english_space,sys.argv[1],10))
#print(utils.neighbours(english_space_hashed,sys.argv[1],10))

sp,count = MEN.compute_men_spearman(english_space,MEN_annot)
print ("SPEARMAN BEFORE FLYING:",sp, "(calculated over",count,"items.)")
sp,count = MEN.compute_men_spearman(english_space_hashed,MEN_annot)
print ("SPEARMAN AFTER FLYING:",sp, "(calculated over",count,"items.)")
