from collections import defaultdict, Counter
from itertools import combinations
from functools import reduce

def read_file():
    tiles = defaultdict(list)
    with open('../input/day20_input.txt') as file:
        for line in file:
            line = line.strip()
            if len(line) == 0: 
                continue
            elif line.startswith("Tile"):
                current = int(line[5:-1])
            else:
                tiles[current].append(line)
    return tiles

def flip_horiz(tile):
    return [reversed(x) for x in tile]

def generate_edges(tile):
    sides = [tile[0],
            tile[-1],
            [x[0] for x in tile],
            [x[-1] for x in tile]]
    temp = set()
    for x in sides:
        string = ''.join(x)
        temp.add(string)
        temp.add(string[::-1])
    return temp

def flip_vert(tile):
    return reversed(tile)

def rotate_left(tile):
    new = list()
    for i in range(len(tile)):
        new.append([x[-i-1] for x in tile])
    return new

def rotate_right(tile):
    new = list()
    for i in range(len(tile)):
        new.append([x[i] for x in reversed(tile)])
    return new

def print_tile(tile):
    for line in tile:
        print(*line)
    print()

def puzzle1():
    tiles = read_file()
    edges = Counter()
    corners = []
    for key, val in tiles.items():
        edges.update(generate_edges(val))
    for key, val in tiles.items():
        if len([x for x in generate_edges(val) if edges[x] == 1]) > 3:
            corners.append(key)
    total = 1
    print(corners)
    for key in corners:
        total *= key
    print(total)
            
            

def puzzle2():
    pass

puzzle1()
puzzle2()