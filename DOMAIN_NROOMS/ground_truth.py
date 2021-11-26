import sys
sys.path.insert(0, '../..')

from mdps.nroom_mdp import create_flat_mdp
from LMDPs.lmdps import power_method

import numpy as np

def ground_truth(**kargs):

    GRID_SIZE = kargs['GRID_SIZE']
    ROOM_SIZE = kargs['ROOM_SIZE']
    GOAL_POS = kargs['GOAL_LOCAL_POS']
    GOAL_ROOMS = kargs['GOAL_ROOMS']
    LAMBDA = kargs['LAMBDA']
    
    _, _, _, P, R = create_flat_mdp(GRID_SIZE, ROOM_SIZE, GOAL_POS, GOAL_ROOMS)

    G = np.diagflat(np.exp(R/LAMBDA))
    P[np.isnan(P)]= 0.
    
    Z = power_method(P, G, sparse=True, n_iter=2500)

    return Z