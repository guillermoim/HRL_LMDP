import sys
sys.path.insert(0, '../LMDPS')
sys.path.insert(0, '../mdps')

from LMDPs.z_learning import zlearning
from mdps.nroom_mdp import create_flat_mdp
from .utilities import get_exit_states

def flat_Z_learning(c, **kargs):

    # Retrieve problem parameters
    GRID_SIZE = kargs['GRID_SIZE']
    ROOM_SIZE = kargs['ROOM_SIZE']
    GOAL_POS = kargs['GOAL_LOCAL_POS']
    GOAL_ROOMS = kargs['GOAL_ROOMS']
    MAX_N_SAMPLES = kargs['MAX_N_SAMPLES']
    Z_OPT = kargs['Z_OPT']
    LAMBDA = kargs['LAMBDA']

    sample_states, S, T, P, R = create_flat_mdp(GRID_SIZE, ROOM_SIZE, GOAL_POS, GOAL_ROOMS)

    partitions = get_exit_states(GRID_SIZE, ROOM_SIZE, GOAL_POS, T)
    M = [e for key in partitions for e in partitions[key]['exit_states'] if e not in T]

    Z, errors = zlearning(sample_states, S, T, P, R, M, Z_OPT, c, LAMBDA, MAX_N_SAMPLES)

    return Z, errors