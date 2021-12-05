''' 
My original idea using a unique string format for each hexagon passes for puzzle1 and the test input but fails for the actual puzzle input. I switched to a faster, easier coordinate based approach.
'''

from collections import Counter

def read_file_string():
    moves = list()
    with open('../input/day24_input.txt') as file:
        for line in file:
            line = line.strip()
            temp = generate_counter(line)
            moves.append(temp)
    return moves

def read_file_coords():
    with open('../input/day24_input.txt') as file:
        black = set()
        for line in file:
            line = line.strip()
            x,y,z = 0,0,0
            while line:
                if line.startswith('e'):
                    x += 1
                    y -= 1
                    line = line[1:]
                elif line.startswith('w'):
                    x -= 1
                    y += 1
                    line = line[1:]
                elif line.startswith('se'):
                    y -= 1
                    z += 1
                    line = line[2:]
                elif line.startswith('sw'):
                    x -= 1
                    z += 1
                    line = line[2:]
                elif line.startswith('nw'):
                    z -= 1
                    y += 1
                    line = line[2:]
                elif line.startswith('ne'):
                    x += 1
                    z -= 1
                    line = line[2:]
            if (x,y,z) in black:
                black.remove((x,y,z))
            else:
                black.add((x,y,z))
    return black

def reduce_moves(move):
    # cancel triangular moves
    if move["nw"] and move["sw"] and move["e"]:
        temp = min(move["nw"], move["sw"], move["e"])
        move.subtract(["nw","sw","e"]*temp)
    if move["ne"] and move["se"] and move["w"]:
        temp = min(move["ne"], move["se"], move["w"])
        move.subtract(["ne","se","w"]*temp)
    # cancel opposite moves
    if move["e"] and move["w"]:
        temp = min(move["w"],move["e"])
        move.subtract(["e","w"]*temp)
    if move["ne"] and move["sw"]:
        temp = min(move["sw"],move["ne"])
        move.subtract(["ne","sw"]*temp)
    if move["se"] and move["nw"]:
        temp = min(move["nw"],move["se"])
        move.subtract(["se","nw"]*temp)
    # replace two moves with equivalent one move
    if move["nw"] and move["sw"]:
        temp = min(move["nw"], move["sw"])
        move.subtract(["nw","sw"]*temp)
        move.update(["w"]*temp)
    if move["e"] and move["nw"]:
        temp = min(move["e"], move["nw"])
        move.subtract(["e","nw"]*temp)
        move.update(["ne"]*temp)
    if move["sw"] and move["e"]:
        temp = min(move["e"], move["sw"])
        move.subtract(["e","sw"]*temp)
        move.update(["se"]*temp)
    if move["ne"] and move["w"]:
        temp = min(move["ne"], move["w"])
        move.subtract(["ne","w"]*temp)
        move.update(["nw"]*temp)
    if move["w"] and move["se"]:
        temp = min(move["w"], move["se"])
        move.subtract(["w","se"]*temp)
        move.update(["sw"]*temp)
    if move["ne"] and move["se"]:
        move.subtract(["ne","se"])
        move.update(["e"])
    return move

def generate_counter(line):
    temp = Counter()
    while line:
        if line.startswith("e"):
            temp.update(["e"])
            line = line[1:]
        elif line.startswith("w"):
            temp.update(["w"])
            line = line[1:]
        elif line.startswith("se"):
            temp.update(["se"])
            line = line[2:]
        elif line.startswith("sw"):
            temp.update(["sw"])
            line = line[2:]
        elif line.startswith("nw"):
            temp.update(["nw"])
            line = line[2:]
        elif line.startswith("ne"):
            temp.update(["ne"])
            line = line[2:]
    return temp

def generate_neighbors(line):
    nbhrs = [reduce_moves(generate_counter(line+x)) for x in ["e","ne","nw","w","sw","se"]]
    return ["".join(sorted(move.elements())) for move in nbhrs]

def puzzle1_string():
    moves = read_file_string()
    tiles = Counter()
    for move in moves:
        move = reduce_moves(move)
        tiles.update(["".join(sorted(move.elements()))])
    count = 0
    black = list()
    for key, val in sorted(tiles.items(), key = lambda x: x[1]):
        if val % 2:
            count += 1
            black.append(key)
    print(count)
    return black

def puzzle2_string():
    black = set(puzzle1_string())
    print("Start:", len(black))
    for day in range(100):
        white = set()
        flip = set()
        for tile in black:
            nhbrs = generate_neighbors(tile)
            temp = [x for x in nhbrs if x in black]
            if len(temp) == 0 or len(temp) > 2:
                flip.add(tile)
            white.update(x for x in nhbrs if x not in black)
        white = [reduce_moves(generate_counter(x)) for x in white]
        white = set(["".join(sorted(move.elements())) for move in white])
        for tile in white:
            nhbrs = generate_neighbors(tile)
            if len([x for x in nhbrs if x in black]) == 2:
                flip.add(tile)
        flip = [reduce_moves(generate_counter(x)) for x in flip]
        flip = set(["".join(sorted(move.elements())) for move in flip])
        black.symmetric_difference_update(flip)
        black = [reduce_moves(generate_counter(x)) for x in black]
        black = set(["".join(sorted(move.elements())) for move in black])
        print("Day "+str(day+1)+":", len(black))

def generate_neighbors_coords(x,y,z):
    return [(x+dx,y+dy,z+dz) for (dx,dy,dz) in [(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,1,-1),(1,0,-1)]]

def puzzle2_coords():
    black = read_file_coords()
    print("Start:", len(black))
    for day in range(100):
        white = set()
        flip = set()
        for tile in black:
            nhbrs = generate_neighbors_coords(*tile)
            temp = [x for x in nhbrs if x in black]
            if len(temp) == 0 or len(temp) > 2:
                flip.add(tile)
            white.update(x for x in nhbrs if x not in black)
        for tile in white:
            nhbrs = generate_neighbors_coords(*tile)
            if len([x for x in nhbrs if x in black]) == 2:
                flip.add(tile)
        black.symmetric_difference_update(flip)
        print("Day "+str(day+1)+":", len(black))


puzzle2_coords()