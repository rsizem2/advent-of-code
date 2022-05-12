
def read_file(test = True):
    if test:
        filename = '../tests/day3.txt'
    else:
        filename = '../input/day3.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(line.strip())
    return temp

def puzzle1():
    temp = read_file(False)
    houses = set()
    for line in temp:
        pos = [0,0]
        for move in line:
            if move == "^":
                pos[0] += 1
                houses.add(tuple(pos))
            elif move == 'v':
                pos[0] -= 1
                houses.add(tuple(pos))
            elif move == ">":
                pos[1] += 1
                houses.add(tuple(pos))
            elif move == '<':
                pos[1] -= 1
                houses.add(tuple(pos))
    print(len(houses))
    
def puzzle2():
    temp = read_file(False)
    houses = set()
    pos1 = [0,0]
    pos2 = [0,0]
    houses.add(tuple(pos1))
    for line in temp:
        pos1 = [0,0]
        pos2 = [0,0]
        for i, move in enumerate(line):
            if i % 2 == 0:
                if move == "^":
                    pos1[0] += 1
                    houses.add(tuple(pos1))
                elif move == 'v':
                    pos1[0] -= 1
                    houses.add(tuple(pos1))
                elif move == ">":
                    pos1[1] += 1
                    houses.add(tuple(pos1))
                elif move == '<':
                    pos1[1] -= 1
                    houses.add(tuple(pos1))
            else:
                if move == "^":
                    pos2[0] += 1
                    houses.add(tuple(pos2))
                elif move == 'v':
                    pos2[0] -= 1
                    houses.add(tuple(pos2))
                elif move == ">":
                    pos2[1] += 1
                    houses.add(tuple(pos2))
                elif move == '<':
                    pos2[1] -= 1
                    houses.add(tuple(pos2))
    print(len(houses))
        
puzzle1()
puzzle2()