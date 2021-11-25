from networkx.algorithms import wiener
from tqdm import tqdm
import numpy as np
from .utilities import get_exit_states, unproject_state
import sys

sys.path.insert(0, '..')

from mdps.taxi_mdps import create_flat_mdp, create_taxi_room

def __init__():
    pass

def HRL(version, c0, c1, **kargs):

    DIM = kargs['DIM']
    Z_TRUE = kargs['Z_OPT']
    Z_OPT_SUBTASKS = kargs['Z_OPT_SUBTASKS']
    MAX_N_SAMPLES = kargs['MAX_N_SAMPLES']
    LAMBDA = kargs['LAMBDA']
    
    # Retrieve the problem and the subtasks
    sample_states, S, T, P, R = create_flat_mdp(DIM)
    P_, abs_states, R_ = create_taxi_room(DIM)
    P_[np.isnan(P_)] = 0.

    # Declare the full state space
    F = S+T

    # Get the partitions and the exit set
    partitions = get_exit_states(DIM, T)
    exit_set = [e for key in partitions for e in partitions[key]['exit_states']]

    # Metric states are the states in the exit set that are non-terminal, bc value at terminal states is fixed
    M1 = list(map(F.index, [e for e in exit_set if e not in T]))
    M2 = list(map(exit_set.index, [e for e in exit_set if e not in T]))

    # Declare the variables for storing the value functions
    Z_SUBTASKS = np.ones(R_.shape)
    Z_SUBTASKS[:, -4:] = np.exp(R_[:, -4:])

    Z = np.ones((len(exit_set),1))
    for e in exit_set:
        if e in T:
            Z[exit_set.index(e), 0] = np.exp(R[F.index(e)])

    errors = []     # High-level errors
    errors_i = []   # Low-level errors

    # Auxiliary variables, ...
    n_samples = 0   
    n_episodes = 0

    pbar = tqdm(total=MAX_N_SAMPLES)    

    KH = 0
    KL = 0

    alphaHL = c0 / (c0 + KH)
    alphaLL = c1 / (c1 + KL)

    while n_samples < MAX_N_SAMPLES:
        
        n_episodes += 1
        state = sample_states[np.random.choice(len(sample_states))]


        while state not in T:
            
            # Partition in taxi domain are indeed each of the (sub)problems, identify by the tuple <passenger_location, final_destination>
            current_partition = state[1], state[2]

            pbar.set_description(f'alphas HL={alphaHL:.4f} LL={alphaLL:.4f} LL_episodes={n_episodes}')

            local_exits = partitions[current_partition]['exit_states']
            exit_idxs = [exit_set.index(e) for e in local_exits]

            # Learn the subtasks!
            while state not in local_exits:

                weights = Z[exit_idxs]
                local_z = np.dot(weights.T, Z_SUBTASKS)

                alphaHL = c0 / (c0 + KH)
                alphaLL = c1 / (c1 + KL)
                
                # Project current state
                proj_state = 0, *state[0]
                idx_proj_state = abs_states.index(proj_state)
                
                # Get local estimated policy (at current state) and transition probabilities
                u = P_[idx_proj_state, :] * local_z[0, :]
                d = np.nansum(u)
                sample_prob = (u / d)

                # Take new sample according to estimated policy
                idxs = np.where(~np.isnan(sample_prob))[0]
                idx_proj_next_state = np.random.choice(idxs, p=sample_prob[idxs])

                n_samples += 1
                pbar.update(1)

                # Project next state
                proj_next_state = abs_states[idx_proj_next_state] 
                next_state = unproject_state(proj_next_state, current_partition)

                # Perform Intra-Task learning
                probabilities = np.zeros(Z_SUBTASKS.shape)

                next_sampled_states = []

                for s in range(4):
                    probabilities[s, :] = (P_[idx_proj_state, :] * Z_SUBTASKS[s, :] / np.nansum(P_[idx_proj_state, :] * Z_SUBTASKS[s, :]))
                    if np.any(np.isnan(probabilities)):
                        print(np.where(np.isnan(P)))
                        print(proj_state, Z_SUBTASKS[s, :])
                        exit()
                    next_sampled_states.append((s, np.random.choice(len(abs_states), p=probabilities[s, :])))

                # Update the sub-tasks doing off-policy intra-task learning (equivalent to IS).
                Z_SUBTASKS[:, idx_proj_state] = (1-alphaLL) * Z_SUBTASKS[:, idx_proj_state] + alphaLL * np.exp(R_[:, idx_proj_state]/LAMBDA) * np.multiply(P_[None, idx_proj_state, :], Z_SUBTASKS[:, :]).sum(axis=1)
                
                # V1: if current state is in the exit set, as agent transitions from it, it should be updated
                if state in exit_set and version=="V1":
                    current_estimates = np.dot(weights.T, Z_SUBTASKS)
                    Z[exit_set.index(state), 0] = (1 - alphaHL) * Z[exit_set.index(state), 0] + alphaHL * current_estimates[0, idx_proj_state]
                
                # V2: If next state is exit of current partition then I need to update the exit states *inside* the partition
                if next_state in local_exits and version=="V2":
                    current_estimates = np.dot(weights.T, Z_SUBTASKS)
                    for e in partitions[current_partition]['exit_states_inside']:
                        e_proj = 0, *e[0]
                        idx_e_proj = abs_states.index(e_proj)
                        Z[exit_set.index(e), 0] = (1 - alphaHL) * Z[exit_set.index(e), 0] + alphaHL * current_estimates[0, idx_e_proj]

                # V3: Update all exit states
                if next_state in local_exits and version=="V3":
                    H = [current_partition]
                    H.extend([h for h in partitions if h != current_partition])

                    for h in H:
                        
                        le = partitions[h]['exit_states']
                        idxs = [exit_set.index(x) for x in le]
                        weights = Z[idxs]
                        current_estimates = np.dot(weights.T, Z_SUBTASKS)
                        for e in partitions[h]['exit_states_inside']:
                            e_proj = 0, *e[0]
                            idx_e_proj = abs_states.index(e_proj)
                            Z[exit_set.index(e), 0] = (1-alphaHL) * Z[exit_set.index(e), 0] + alphaHL * current_estimates[0, idx_e_proj]
                
                # Perform transition
                state = next_state

                # Compute high-level and low-level errors
                error = np.mean(np.abs(np.log(Z_TRUE[M1]) - np.log(Z[M2])))
                errors.append(error)

                error_i = np.abs(np.log(Z_OPT_SUBTASKS[:, :DIM**2]) - np.log(Z_SUBTASKS[:, :DIM**2])).mean()
                errors_i.append(error_i)

                if n_samples > MAX_N_SAMPLES - 1:
                    break

            # Add one to low-level episode counter
            KL+=1
        
        # Add one to high-level episode counter
        KH+=1

    return Z, Z_SUBTASKS, errors, errors_i
