from collections import deque, defaultdict, Counter

def read_file(test = True):
    if test:
        filename = '../tests/day12-3.txt'
    else:
        filename = '../input/day12.txt'
    with open(filename) as file:
        temp = defaultdict(set)
        for line in file:
            start, end = line.strip().split('-')
            temp[start].add(end)
            temp[end].add(start)
    return temp


def bfs_part1(start_node, visited, adj_list):
    
    if start_node == 'end': 
        return 1
    
    paths = 0
    for end_node in adj_list[start_node]:
        if end_node not in visited:
            if end_node.islower():
                temp = {end_node}
            else:
                temp = set()
            paths += bfs_part1(end_node, visited | temp, adj_list)
        
    return paths

def bfs_part2(start_node, visited, adj_list):
    
    if start_node == 'end': 
        return 1
    
    paths = 0
    for end_node in adj_list[start_node]:
        if end_node not in visited:
            if end_node.islower():
                temp = {end_node}
            else:
                temp = set()
            paths += bfs_part2(end_node, visited | temp, adj_list)
        elif end_node != 'start':
            paths += bfs_part1(end_node, visited, adj_list)
        
    return paths
                


def puzzle1(test = True):
    temp = read_file(test)
    print(bfs_part1('start', {'start'}, temp))
        
            

def puzzle2(test = True):
    temp = read_file(test)
    print(bfs_part2('start', {'start'}, temp))


puzzle1(False)
puzzle2(False)