import numpy as np
from collections import defaultdict, deque, Counter
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
    prev = {node: None}
    visited = set()
    while queue:
        cost, node = heapq.heappop(queue)
        #print(cost, node)
        if node == dest:
            return costs[dest], prev
        if node in visited or costs[node] < cost:
            # removed node or obsolete priority
            continue
        visited.add(node)
        possible_moves = get_moves(node)
        #break
        for added_cost, state in possible_moves:
            if state in visited:
                continue
            elif cost + added_cost < costs[state]:
                costs[state] = cost + added_cost
                prev[state] = node
                heapq.heappush(queue, (cost + added_cost, state))
    assert False
     
def get_moves(state, verbose = False):
    if verbose: print("Finding moves:", state)
    moves = list()
    # starting positions
    for start, x in enumerate(state):
        # ending positions
        for end, y in enumerate(state):
            if start == end: continue
            # starting point room
            if is_room(state, start):
                # skip complete room
                if room_complete(state, start):
                    continue
                # skip empty room or final position
                elif room_ready(state, start):
                    continue
                # move to reachable hallway points
                elif end not in rooms and reachable(state, start, end):
                    cost, new_state = move(state, start, end)
                    moves.append((cost, new_state))
                    if verbose: print(cost, new_state)
                    continue
                # move to end point
                elif room_ready(state, end) and reachable(state, start, end):
                    char = pop_room(state, start)[1]
                    if rooms[end] != char: 
                        continue
                    cost, new_state = move(state, start, goals[char])
                    moves.append((cost, new_state))
                    if verbose: print(cost, new_state)
                    continue
            # start point hallways, check destination
            elif x == '.':
                continue
            elif goals[x] == end and reachable(state, start, end) and room_ready(state, end):
                    cost, new_state = move(state, start, end)
                    moves.append((cost, new_state))
                    if verbose: print(cost, new_state)
    #print(state, len(moves))
    return moves

def move(state, start, end):
    # debugging
    #assert reachable(state, start, end), f'moving from {start} to {end} in {[(i,x) for i,x in enumerate(state)]}'
    new_state = list(state)
    # starting position is a room
    if is_room(state, start):
        x = pop_room(state, start)
        dist, char, new_room = x
        new_state[start] = new_room
    else:
        char = state[start]
        assert char != '.', f'moving from {start} to {end} in {[(i,x) for i,x in enumerate(state)]}'
        dist = 0
        new_state[start] = '.'
    multiple = move_costs[char]
    # ending position is a room
    if len(state[end]) > 1:
        #assert room_ready(state, end)
        cost, new_room = push_room(state, end, char)
        dist += abs(start - end)
        dist += cost
        new_state[end] = new_room
    else:
        new_state[end] = char
        dist += abs(start - end)
    #assert char != '.', f'moving from {start} to {end} in {[(i,x) for i,x in enumerate(state)]}'
    # sanity check
    #new, old = Counter(), Counter()
    #for x, y in zip(state, new_state):
    #    new.update(list(y))
    #    old.update(x)
    #assert new == old, f'{state} to {new_state}'
    return multiple*dist, tuple(new_state)
        

def reachable(state, start, end):
    x_min = min(start, end)
    x_max = max(start, end)
    for i in range(x_min, x_max+1):
        if i == start or i in rooms:
            continue
        if state[i] != '.':
            return False
    return True

def room_ready(state, pos):
    return is_room(state, pos) and all(x in ['.', rooms[pos]] for x in state[pos])

def room_complete(state, pos):
    #assert pos in rooms
    return all(x == rooms[pos] for x in state[pos])

def room_empty(state, pos):
    #assert pos in rooms
    return all(x == '.' for x in state[pos])

def pop_room(state, pos):
    #assert is_room(state, pos)
    #assert not room_complete(state, pos)
    room = list(state[pos])
    if all(x == '.' for x in state[pos]):
        return 0, '.', ''.join(room)
    cost = 1
    for i,x in enumerate(room):
        if x != '.':
            room[i] = '.'
            return cost, x, ''.join(room) 
        cost += 1
    assert False 

def push_room(state, pos, char):
    #assert goals[char] == pos
    #assert room_ready(state, pos)
    room = list(state[pos])
    cost = 0
    for i,x in enumerate(room):
        if x == '.':
            cost += 1
            continue
        else:
            #cost += 1
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
        start = tuple(['.','.','BC','.','BA','.','DD','.','AC','.','.'])
        dest = tuple(['.','.','AA','.','BB','.','CC','.','DD','.','.']) 
    costs, prev = search(start, dest)
    print(costs)
    # print intermediate moves
    node = dest
    while prev[node] != start:
        print(prev[node])
        node = prev[node]
    print(node)


def puzzle2(test = True):
    if test:
        start = tuple(['.','.','BDDA','.','CCBD','.','BBAC','.','DACA','.','.'])
        dest = tuple(['.','.','AAAA','.','BBBB','.','CCCC','.','DDDD','.','.'])
    else:
        start = tuple(['.','.','BDDC','.','BCBA','.','DBAD','.','AACC','.','.'])
        dest = tuple(['.','.','AAAA','.','BBBB','.','CCCC','.','DDDD','.','.'])
    costs, prev = search(start, dest)
    print(costs)
    # print intermediate moves
    node = dest
    while prev[node] != start:
        print(prev[node])
        node = prev[node]
    print(node)
    
    
#puzzle1(False)
puzzle2(False)