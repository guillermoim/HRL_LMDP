import sys
sys.path.insert(0, '../..')
from LMDPs import lmdps
from mdps.taxi_mdps import create_flat_mdp
import numpy as np


def ground_truth(dim, lambda_=1):
    _, _, _, P, R = create_flat_mdp(dim)
    G = np.diagflat(np.exp(R/lambda_))
    P[np.isnan(P)] = 0.
    Z = lmdps.power_method(P, G, sparse=True)
    return Z
