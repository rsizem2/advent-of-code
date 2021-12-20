import numpy as np
from itertools import combinations

def read_file(test = True):
    if test:
        filename = '../tests/day19.txt'
    else:
        filename = '../input/day19.txt'
    with open(filename) as file:
        scanners = list()
        for line in file:
            if 'scanner' in line:
                temp = list()
            elif ',' in line:
                temp.append(np.array(list(map(int,line.split(',')))))
            else:
                scanners.append(temp)
    return scanners
            


def puzzle1(test = True):
    scanners = read_file(test)
    distances = list()
    for scanner in scanners:
        temp = set()
        for x,y,z in combinations(scanner,3):
            temp.add(tuple(sorted(map(int,[np.sum(np.abs(x-y)),np.sum(np.abs(x-z)),np.sum(np.abs(z-y))]))))
        distances.append(temp)
    for scanner1, scanner2 in combinations(distances, 2):
        print('overlap:', len(scanner1 & scanner2))
    pass
                
                

def puzzle2(test = True):
    scanners = read_file(test)
    pass


puzzle1()
puzzle2()
