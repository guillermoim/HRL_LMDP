import numpy as np
from numpy.linalg import eig
from scipy.sparse.linalg import eigs
import scipy


def power_method(P, G, sparse=True, n_iter=1000):
    z = np.ones((G.shape[0], 1))

    if sparse:
        P = scipy.sparse.csr_matrix(P)
        G = scipy.sparse.csr_matrix(G)
        z = scipy.sparse.csr_matrix(z)
    else:
        P = np.asarray(P) if not scipy.sparse.issparse(P) else P.todense()
        G = np.asarray(G) if not scipy.sparse.issparse(G) else G.todense()

    for _ in range(n_iter):
        z = G * P * z

    if sparse:
        z = z.todense()

    return z


def eigenvector(P, G):

    if scipy.sparse.issparse(P):
        w, v = eigs(G * P)
    else:
        w, v = eig(G * P)

    z = v[:, np.abs(w)==1].copy()

    z = np.mean(z, axis=1)

    return z


def solve_lmdp(P, q, t_states, t=1, n_iter=1000):
    
    z = np.ones(q.shape)
    G = np.diagflat(np.exp(q/t),)

    z_I = z.copy()
    z_I[t_states, 0] = 0
    z_B = np.zeros(z_I.shape)
    z_B[t_states, 0] = G[t_states, t_states]
    z_B[[i for i in range(P.shape[0]) if i not in t_states]] = 0

    P_II = P.copy() #np.delete(np.delete(P, t_states, axis=0), t_states, axis=1)
    P_II[t_states, :] = 0
    P_II[:, t_states] = 0
    P_IB = P.copy()
    P_IB[t_states, :] = 0
    P_IB[:, [i for i in range(P.shape[0]) if not i in t_states]] = 0

    for _ in range(n_iter):

        z_I = G * P_II * z_I + G * P_IB * z_B

    return z_I + z_B


def get_policy(P, z):

    A = P.copy()
    Z = z.reshape(-1,1)
    for i in range(P.shape[0]):
        row = np.multiply(P[i, None], Z.T)
        if row.sum() == 0:
            continue

        A[i, None] = row / row.sum()

    return A

def get_greedy_policy(P):
    P[P == 0] = np.inf
    return P.argmin(axis=1)





