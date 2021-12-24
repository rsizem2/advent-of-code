import numpy as np
from collections import defaultdict, deque
import heapq

goals = {'A': 2,'B': 4,'C': 6,'D': 8,}
rooms = {val:key for key,val in goals.items()}
move_costs = {'A': 1,'B': 10,'C': 100,'D': 1000,}


# dijkstra algorithm
def search(start, dest):
    dest = tuple(dest)
    node = tuple(start)
    costs = defaultdict(lambda: np.Inf)
    costs[node] = 0
    queue = [(0, node),]
    visited = set()
    while queue:
        cost, node = heapq.heappop(queue)
        print(cost, node)
        if node == dest:
            return costs[dest]
        if node in visited or costs[node] < cost:
            # removed node popped
            continue
        visited.add(node)
        possible_moves = get_moves(node)
        for added_cost, state in possible_moves:
            if state in visited:
                continue
            elif cost + added_cost <= costs[state]:
                costs[state] = cost + added_cost
                heapq.heappush(queue, (cost + added_cost, state))
    assert False
        
def valid_move(state, start, end):
    if not reachable(state, start, end):
        return False
    # start at a room
    if is_room(state, start):
        char = pop_room(state, start)[1]
    elif state[start] == '.':
        return False
    else:
        char = state[start]
    # end at a room
    if is_room(state, end):
        return room_ready(state, end) and end == goals[char]
    else:
        return state[end] == '.'
     
def get_moves(state):
    print('Getting Moves:', state)
    moves = list()
    for start, x in enumerate(state):
        for end, y in enumerate(state):
            if start == end: 
                continue
            elif not valid_move(state, start, end):
                continue
            else:
                cost, new_state = move(state, start, end)
                moves.append((cost, new_state))
    return moves

def move(state, start, end):
    # debugging
    assert reachable(state, start, end)
    new_state = list(state)
    # starting position is a room
    if len(state[start]) > 1:
        dist, char, new_room = pop_room(state, start)
        new_state[start] = new_room
    else:
        char = state[start]
        assert char != '.', f'moving from {start} to {end} in {state}'
        dist = 0
    # ending position is a room
    if len(state[end]) > 1:
        assert room_ready(state, end)
        cost, new_room = push_room(state, end, char)
        dist += cost
        new_state[end] = new_room
    else:
        new_state[end] = char
        dist += abs(start - end)
    return dist, tuple(new_state)
        

def reachable(state, start, end):
    x_min = min(start, end)
    x_max = max(start, end)
    for i in range(x_min, x_max+1):
        if i == start or i in goals:
            continue
        if state[i] != '.':
            return False
    return True

def room_ready(state, pos):
    room = list(state[pos])
    assert len(room) > 1
    for i, char in room:
        if char == '.':
            continue
        elif goals[char] == pos:
            continue
        else:
            return False
    return True

def room_complete(state, pos):
    assert pos in rooms
    return all(x == rooms[pos] for x in state[pos])

def pop_room(state, pos):
    if len(state[pos]) == 1:
        return 0, state[pos], '.'
    assert not room_complete(state, pos)
    assert not all(x == '.' for x in state[pos])
    room = list(state[pos])
    for i,x in enumerate(room, start = 1):
        if x != '.':
            room[i] = '.'
            return i, x, ''.join(room) 
    return 0, '.', ''.join(room)

def push_room(state, pos, char):
    assert goals[char] == pos
    room = list(state[pos])
    cost = 0
    for i,x in room:
        if x == '.':
            cost += 1
            continue
        else:
            cost += 1
            room[i-1] = char
            return cost, ''.join(room)
            break
    room[i] = char
    return cost, ''.join(room)
    
    
def is_room(state, i):
    return len(state[i]) > 1

            

def puzzle1(test = True):
    if test:
        start = tuple(['.','.','BA','.','CD','.','BC','.','DA','.','.'])
        dest = tuple(['.','.','AA','.','BB','.','CC','.','DD','.','.']) 
    else:
        temp = tuple(['.','.','BA','.','CD','.','BC','.','DA','.','.'])
    print(search(start, dest))


def puzzle2(test = True):
    pass
    
    
puzzle1()
puzzle2()