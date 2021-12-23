from collections import deque

def read_file(test = True):
    if test:
        filename = '../tests/day23.txt'
    else:
        filename = '../input/day23.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(line[:-1])
    return np.array(temp)

def puzzle1(test = True):
    temp = read_file(test)
    print(temp)


def puzzle2(test = True):
    temp = read_file(test)
    
puzzle1()
puzzle2()