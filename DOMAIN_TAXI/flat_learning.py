import sys
sys.path.insert(0, '../LMDPS')
sys.path.insert(0, '../mdps')

from LMDPs.z_learning import zlearning
from mdps.taxi_mdps import create_flat_mdp
from .utilities import get_exit_states

def flat_Z_learning(c, **kargs):

    # Retrieve problem parameters
    DIM = kargs['DIM']
    Z_OPT = kargs['Z_OPT']
    LAMBDA = kargs['LAMBDA']
    MAX_N_SAMPLES = kargs['MAX_N_SAMPLES']

    sample_states, S, T, P, R = create_flat_mdp(DIM)

    partitions = get_exit_states(DIM, T)
    M = [e for key in partitions for e in partitions[key]['exit_states'] if e not in T]

    Z, errors = zlearning(sample_states, S, T, P, R, M, Z_OPT, c, LAMBDA, MAX_N_SAMPLES)

    return Z, errors