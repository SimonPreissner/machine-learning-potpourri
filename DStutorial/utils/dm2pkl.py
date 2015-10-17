#Convert .dm file to .pkl
#Usage: python dm2pkl bnc

from composes.semantic_space.space import Space
from composes.utils import io_utils
import sys

#load a space
space = Space.build(data=sys.argv[1]+".dm", cols=sys.argv[1]+".cols", format='dm')
#print space.cooccurrence_matrix
io_utils.save(space, "/home/aurelie/dissect/"+sys.argv[1]+".pkl")
