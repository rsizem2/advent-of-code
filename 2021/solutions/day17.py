import numpy as np
from collections import deque, Counter
from functools import reduce

def read_file(test = True):
    if test:
        filename = '../tests/day17.txt'
    else:
        filename = '../input/day17.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            pass
    return temp


def puzzle1(test = True):
    temp = read_file(test)
    print(temp)

def puzzle2(test = True):
    temp = read_file(test)
    print(temp)


puzzle1()
puzzle2()
