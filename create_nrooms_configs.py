from DOMAIN_NROOMS.ground_truth import ground_truth
import numpy as np
import pickle
from mdps.nroom_mdp import create_room_hierarchical
from LMDPs.lmdps import power_method


def create_config(name, grid_size, goal_rooms, max_n_samples, lamda=1, r_dim=5, goal_pos=(2,3)):

    execution = {
        'GRID_SIZE': grid_size,
        'ROOM_SIZE': r_dim,
        'GOAL_LOCAL_POS': goal_pos,
        'GOAL_ROOMS': goal_rooms,
        'LAMBDA': lamda,
        'MAX_N_SAMPLES': max_n_samples,
        'GOAL_REWARD': 0,
        'NON_GOAL_REWARD': -1
    }
    
    P, abs_states, R = create_room_hierarchical(r_dim, goal_pos)
    P[np.isnan(P)]= 0.

    subtasks = []

    for t in range(R.shape[0]):
        q = np.exp(R[t, :] / lamda)
        G = np.diagflat(q)
        SOL = power_method(P, G, 10000)
        subtasks.append(SOL)

    opt_Z_i = np.array(subtasks).reshape(R.shape[0], len(abs_states))

    Z_true = ground_truth(**execution)

    execution['Z_OPT'] = Z_true
    execution['Z_OPT_SUBTASKS'] = opt_Z_i

    pickle.dump(execution, open(f'configs/nroom/{name}.dict', 'wb'))

if __name__ == '__main__':
    create_config('3x3_goal@0-0_rooms5x5', (3,3), [(0, 0)], 50000, goal_pos=(2,3))
    create_config('5x5_goal@0-0_rooms3x3', (5,5), [(0, 0)], 50000, goal_pos=(1,1), r_dim=3)
    create_config('8x8_goal@0-0_rooms5x5', (8,8), [(0, 0)], 50000, goal_pos=(2,3))


