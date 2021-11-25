import networkx as nx
import numpy as np

def create_taxi_room(dim):
    
    # Returns a taxi room with 4 terminal states.
    graph = nx.grid_graph((dim, dim)).to_directed()
    graph = nx.DiGraph(graph)
    # Change node names from (x,y) to (0,x,y) so we can have terminals @ (1,0,0) ... (1,r_dim-1, r_dim-1)
    mapping = {node:(0, *node) for node in graph.nodes}

    graph = nx.relabel_nodes(graph, mapping)

    graph.add_edge((0, 0, 0), (1, 0, 0))
    graph.add_edge((0, dim-1, 0), (1, dim-1, 0))
    graph.add_edge((0, 0, dim-1), (1, 0, dim-1))
    graph.add_edge((0, dim-1, dim-1), (1, dim-1, dim-1))

    for node in graph.nodes:
        graph.add_edge(node, node)

    states = list(graph.nodes)

    A = nx.adjacency_matrix(graph).todense()
    P = np.asarray(A / A.sum(axis=1))

    R = np.full((4, dim**2 + 4), -1, dtype=np.float64)
    R[:, -4:] = -np.inf
    
    for i, t in enumerate(states[-4:]):
        idx = states.index(t)
        R[i, idx] = 0

    P = np.asarray(P)
    P[P==0] = np.nan
    
    return P, states, R

def create_flat_mdp(dim=5, interior_reward = -1, goal_reward = 0, terminals_non_goals=True):
    
    '''
    This method creates the flat MDP for our taxi domain.

    States are represented by a tuple (grid_location, passenger_location, final_destination), thus the information 
    for the goal is included in the state representation.

    The dynamics can be thought of different gridworlds in which first the (sub)goal is determined by the passenger location
    and when he/she is picked-up, the final destination conditions the next gridworld that is accessed right after in which
    such destination is the final goal.
    '''

    nav_locs = [(i,j) for i in range(dim) for j in range(dim)]

    corners = [(0,0), (dim-1,0), (0,dim-1), (dim-1,dim-1)]
    passenger_locs = corners + ['TAXI']

    # create possible transitions
    loc_and_neighbors = {}

    for loc in nav_locs:
        neighbors = []
        # UP and LEFT
        if loc[0] - 1 > -1: neighbors.append((loc[0] - 1, loc[1]))
        if loc[1] - 1 > -1: neighbors.append((loc[0], loc[1] - 1))
        # DOWN and RIGHT
        if loc[0] + 1 < dim: neighbors.append((loc[0] + 1, loc[1]))
        if loc[1] + 1 < dim: neighbors.append((loc[0], loc[1] + 1))

        loc_and_neighbors[loc] = neighbors

    transitions_1 = []
    transitions_2 = []

    # First of all, add the transition between the (exit)states. This is between the pick-up
    # locations and the next state in which the agent is in the TAXI.
    for c0 in corners:
        for c1 in corners:
            if c0 == c1: continue
            # exit state transition
            transition = (c0, c0, c1), (c0, 'TAXI', c1)
            transition_reversed = (c0, 'TAXI', c1), (c0, c0, c1)
            transitions_1.append(transition)
            transitions_1.append(transition_reversed)

    # Then, add the transitions regarding the navigation within same gridworlds.
    for c0 in passenger_locs:
        for c1 in corners:
            if c0 == c1: continue
            for xy in nav_locs:
                for neighbor in loc_and_neighbors[xy]:
                    transition = (xy, c0, c1), (neighbor, c0, c1)
                    transition_reversed = (neighbor, c0, c1), (xy, c0, c1)
                    transitions_2.append(transition)
                    transitions_2.append(transition_reversed)

    terminal_edges = []

    # Then, for each terminal goal I add a directed edge in which the passenger is at final destination.
    for corner in corners:
        transition = (corner, 'TAXI', corner), (corner, 'D', corner)
        terminal_edges.append(transition)

    # Also, I need to add some terminals in the 'first' gridworlds to allow exploration, these terminals happen
    # (taxi_loc, pass, dst) whenever taxi_loc = corner and taxi_loc != pass.
    # only if so specified by argument <terminal_non_goals>
    if terminals_non_goals:
        for taxi in corners:
            for passenger in corners:
                for dst in corners:
                    if taxi == passenger: continue
                    if passenger == dst: continue
                    transition = (taxi, passenger, dst), (taxi, 'Forbidden', None)
                    terminal_edges.append(transition)


    graph = nx.DiGraph()
    graph.add_edges_from(transitions_1)
    graph.add_edges_from(transitions_2)
    graph.add_edges_from(terminal_edges)

    for node in graph.nodes():
        graph.add_edge(node, node)

    states = list(graph.nodes())

    sample_states = [s for s in states if s[1] not in ('D', 'TAXI', 'Forbidden')]

    goal_states = [s for s in states if s[1] == 'D']
    non_goal_states = [s for s in states if s[1] == 'Forbidden']


    A = nx.linalg.adjacency_matrix(graph).todense()
    P = A / A.sum(axis=1)
     
    R = np.ndarray(P.shape[0], dtype=np.float64)

    terminal_states = goal_states + non_goal_states
    interior_states = [s for s in states if s not in terminal_states]

    R[[states.index(s) for s in interior_states]] = interior_reward
    R[[states.index(s) for s in goal_states]] = goal_reward
    R[[states.index(s) for s in non_goal_states]] = -np.inf

    P = np.asarray(P)
    P[P==0] = np.nan

    return sample_states, interior_states, terminal_states, P, R
