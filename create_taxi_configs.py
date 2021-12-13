import pickle

from LMDPs.lmdps import power_method
from mdps.taxi_mdps import create_taxi_room
from DOMAIN_TAXI.ground_truth import ground_truth
import numpy as np


def create_config(name, dim, max_n_samples, lambda_=1):

    execution = {
        'DIM': dim,
        'LAMBDA': lambda_,
        'MAX_N_SAMPLES': max_n_samples,
        'GOAL_REWARD': 0,
        'NON_GOAL_REWARD': -1
    }

    Z_true = ground_truth(dim, lambda_)

    P, abs_states, R = create_taxi_room(dim)

    P[np.isnan(P)]= 0.

    subtasks = []

    for t in range(R.shape[0]):
        q = np.exp(R[t, :] / lambda_)
        G = np.diagflat(q)
        SOL = power_method(P, G, 10000)
        subtasks.append(SOL)

    Z_i_opt = np.array(subtasks).reshape(R.shape[0], len(abs_states))
    
    execution['Z_OPT'] = Z_true
    execution['Z_OPT_SUBTASKS'] = Z_i_opt

    pickle.dump(execution, open(f'configs/taxi/{name}.dict', 'wb'))


if __name__ == '__main__':

    create_config('taxi_5_1', 5, 1e5, 1)
    create_config('taxi_10_1', 10, 1e5, 1)
