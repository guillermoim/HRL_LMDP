import numpy as np
import networkx as nx
from itertools import product


def create_flat_mdp(dims, room_size, goal_pos, goal_rooms, interior_reward=-1,  goal_reward=0, non_goal_terminals=True):

    assert room_size % 2 > 0, "The room size should be an odd number"

    col_rooms, row_rooms = dims

    X = col_rooms * room_size
    Y = row_rooms * room_size

    graph = nx.grid_graph(dim=[X, Y])

    renaming = {n: (0, *n) for n in graph.nodes()}
    graph = nx.relabel_nodes(graph, renaming)

    # Change from one room to another happens at the middle position
    pass_p = room_size // 2
    cols = [x*(room_size)-1 for x in range(1, X)]
    rows = [y*(room_size)-1 for y in range(1, Y)]

    #Remove intra-connections
    for (s, u, v) in graph.nodes():
        if v in cols and (u % room_size != pass_p) and v != X-1:
            graph.remove_edge((s, u, v), (s, u, v + 1))
        if u in rows and (v % room_size != pass_p) and u != Y-1:
            graph.remove_edge((s, u, v), (s, u + 1, v))

    graph = nx.DiGraph(graph)

    # Place the top & bottom walls
    if non_goal_terminals:
        for i in range(pass_p, col_rooms*room_size, room_size):
            graph.add_edge((0, 0, i), (0, -1, i))
            graph.add_edge((0, room_size*row_rooms-1, i), (0, room_size*row_rooms,  i))

        # Place the left and right walls
        for j in range(pass_p, row_rooms * room_size, room_size):
            graph.add_edge((0, j, 0), (0, j, -1))
            graph.add_edge((0, j, room_size*col_rooms - 1), (0, j, room_size * col_rooms))

    for (i, j) in product(range(col_rooms), range(row_rooms)):
        if (i, j) in goal_rooms or non_goal_terminals:
            goal_i, goal_j = (room_size*j)+goal_pos[0], (room_size*i)+goal_pos[1]
            graph.add_edge((0, goal_i, goal_j), (1, goal_i, goal_j))

    # self edges
    for node in graph.nodes():
        graph.add_edge(node, node)

    A = nx.linalg.graphmatrix.adjacency_matrix(graph)
    P = A.multiply(1/A.sum(axis=1))

    goals_indices = [list(graph.nodes).index((1, room_size*j+goal_pos[0], room_size*i+goal_pos[1])) for (i,j) in goal_rooms]

    R = np.full(P.shape[0], interior_reward, dtype=np.float16)
    
    N = np.product(dims) * room_size ** 2
    
    interior_states = list(graph.nodes())[:N]
    terminal_states = list(graph.nodes())[N:]

    R[N:] = -np.inf

    for i in goals_indices:
        R[i] = goal_reward

    P = P.toarray()
    P[P==0] = np.nan

    return interior_states, interior_states, terminal_states, P, R


def create_room_hierarchical(room_size, goal_pos):

    graph = nx.DiGraph(nx.grid_graph(dim=[room_size, room_size]))

    renaming = {n: (0, *n) for n in graph.nodes()}
    graph = nx.relabel_nodes(graph, renaming)

    terminal_neighbors = [(0, 0, room_size//2), (0, room_size//2, 0), (0, room_size//2, room_size-1), (0, room_size-1, room_size//2), (0, *goal_pos)]
    terminal_states = [(0, -1, room_size//2), (0, room_size//2, -1), (0, room_size//2, room_size), (0, room_size, room_size//2), (1, *goal_pos)]

    for i, n in enumerate(terminal_neighbors):
        t = terminal_states[i]
        graph.add_edge(n, t)

    for i in graph.nodes():
        graph.add_edge(i, i)

    A = nx.linalg.graphmatrix.adjacency_matrix(graph)
    P = A.multiply(1/A.sum(axis=1))

    states = list(graph.nodes()) 

    R = np.zeros(( len(terminal_states),  len(states) ))

    R[:, :room_size**2] = -1

    for i, t in enumerate(terminal_states):
        R[i, room_size**2:] = -np.inf
        R[i, states.index(t)] = 0

    P = P.toarray()
    P[P==0] = np.nan
    
    return P, states, R


