import numpy as np
from tqdm import tqdm


def zlearning(init_states, S, T, P, R, M, Z_OPT, C=3000, LAMBDA=1, TOTAL_N_SAMPLES=50000):
    
    F = S+T

    M = [F.index(m) for m in M]

    Z = np.ones((len(F), 1))
    Z[len(S):] = 0
    Z[np.where(R==0)] = 1



    i = 0
    K = 0

    errors = []

    pbar = tqdm(total=TOTAL_N_SAMPLES)

    while i < TOTAL_N_SAMPLES:

        # Sample from the initial states
        state = init_states[np.random.choice(len(init_states))] 
        alpha = C / (C + K + 1)

        while state not in T:
            
            idx_state = S.index(state)

            probabilites = np.multiply(P[idx_state, :, None], Z) / np.nansum(np.multiply(P[idx_state, :, None] , Z)).T
            idxs = np.where(~np.isnan(probabilites))[0]
            next_state = F[np.random.choice(idxs, p=probabilites[idxs, 0])]
            idx_next_state = F.index(next_state)

            isw =  P[idx_state, idx_next_state] / probabilites[idx_next_state]
            
            Z[idx_state] = (1-alpha) * Z[idx_state] + isw * alpha * np.exp(R[idx_state]/ LAMBDA) * Z[idx_next_state]

            state = next_state
        
            i+=1
            pbar.update(1)  

            error = np.abs(np.log(Z_OPT[M]) - np.log(Z[M])).mean()
            errors.append(error)

            if i > TOTAL_N_SAMPLES - 1:
                break 

        K += 1

    return Z, errors