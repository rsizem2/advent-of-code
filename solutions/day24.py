from collections import Counter

def read_file():
    moves = list()
    with open('../input/day24_input.txt') as file:
        for line in file:
            line = line.strip()
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
            moves.append(temp)
    return moves

def reduce_moves(move):
    if move["nw"] and move["sw"] and move["e"]:
        temp = min(move["nw"], move["sw"], move["e"])
        move.subtract(["nw","sw","e"]*temp)
    if move["ne"] and move["se"] and move["w"]:
        temp = min(move["ne"], move["se"], move["w"])
        move.subtract(["ne","se","w"]*temp)
    #cancel opposite moves
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

def puzzle1():
    moves = read_file()
    tiles = Counter()
    for move in moves:
        # cancel out circular moves
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

def puzzle2():
    black = puzzle1()
    print(sorted(black))
    for day in range(100):
        for tile in black:
            pass
        

puzzle2()