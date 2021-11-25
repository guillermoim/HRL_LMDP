def get_exit_states(DIM, T):

    partitions_set = {}

    corners = [(0,0), (DIM-1,0), (0,DIM-1), (DIM-1, DIM-1)]
    passenger_locs = corners + ['TAXI']

    for c1 in passenger_locs:
        for c2 in corners:
            if c1 != c2:
                partition = (c1, c2)
                if c1 == 'TAXI':
                    aux = [(c, c, c2) for c in corners if c != c2] + [(c2, 'D', c2)]
                    exit_states = [None, None, None, None]
                    for e in aux:
                        if e[1] != 'D':
                            exit_states[corners.index(e[1])] = e
                        else:
                            exit_states[corners.index(e[2])] = e
                else:
                    aux = [(c, 'Forbidden', None) for c in corners if c != c1] + [(c1, 'TAXI', c2)]
                    exit_states = [None, None, None, None]
                    for e in aux:
                        exit_states[corners.index(e[0])] = e

                partitions_set[partition] = {'exit_states' : exit_states}


    exit_set = [e for key in partitions_set for e in partitions_set[key]['exit_states'] if e not in T]

    for key in partitions_set:
        partitions_set[key]['exit_states_inside'] = []

    exit_set = [e for key in partitions_set for e in partitions_set[key]['exit_states'] if e not in T]

    for e in exit_set:
        partition = e[1], e[2]
        partitions_set[partition]['exit_states_inside'].append(e)

    return partitions_set

def unproject_state(state, partition):
    if state[0] == 0:
        return ((state[1], state[2]), *partition)
    else:
        if partition[0] != 'TAXI':
            return ((state[1], state[2]), 'TAXI', partition[1])
        else:
            loc = (state[1], state[2])
            if loc == partition[1]:
                return (loc, 'D', partition[1])
            else:
                return (loc, loc, partition[1])