import numpy as np
from itertools import combinations

def read_file(test = True):
    if test:
        filename = '../tests/day20.txt'
    else:
        filename = '../input/day20.txt'
    with open(filename) as file:
        image = list()
        for i, line in enumerate(file):
            if i == 0:
                algorithm = line.strip()
            elif line.strip():
                image.append(line.strip())
    return algorithm, image
            


def puzzle1(test = True):
    alg, img = read_file(test)
    for line in img:
        print(line)
                
                

def puzzle2(test = True):
    alg, img = read_file(test)
    for line in img:
        print(line)


puzzle1()
puzzle2()
