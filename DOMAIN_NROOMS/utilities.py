def get_exit_states(D, room_size, goal_pos, T):

    partitions_set = {}

    d1, d2 = D

    for i in range(d1):
        for j in range(d2):
            x, y = i*room_size, j*room_size
            goal_x, goal_y = x + goal_pos[0], y + goal_pos[1]
            exit_states = [(0, x-1, y + room_size//2), (0, x+room_size//2, y-1), (0, x+room_size//2, y+room_size), (0, x+room_size, y+room_size//2), (1, goal_x, goal_y)]
            partitions_set[i, j] = {'exit_states' : exit_states}

    for key in partitions_set:
        partitions_set[key]['exit_states_inside'] = []

    exit_set = [e for key in partitions_set for e in partitions_set[key]['exit_states'] if e not in T]

    for e in exit_set:
        partitions_set[get_room(e, room_size)]['exit_states_inside'].append(e)

    return partitions_set

def get_room(state, room_size):

    _, x, y = state

    return (max(x // room_size, 0), max(y // room_size, 0))


def project_state(state, room_size):
    s0, s1, s2 = state
    #X, Y = get_room(state, room_size)
    #X, Y = X*room_size, Y*room_size
    return s0, s1%room_size, s2%room_size


def unproject_state(state, room, room_size):
    s0, s1, s2 = state
    X, Y = room[0] * room_size, room[1] * room_size

    return s0, X+s1, Y+s2