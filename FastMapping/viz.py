import numpy as np
from utils import sim_to_matrix, readDM, run_PCA
import sys

def visualise(words, space):
    run_PCA(space,words,words[0]+"_space.png")


'''Read semantic space'''
space = readDM(sys.argv[1])
neighbours = sim_to_matrix(space, space[sys.argv[2]], int(sys.argv[3]))
#print(neighbours)
visualise(neighbours,space)
