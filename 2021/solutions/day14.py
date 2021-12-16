import numpy as np
from collections import deque, Counter

def read_file(test = True):
    if test:
        filename = '../tests/day14.txt'
    else:
        filename = '../input/day14.txt'
    with open(filename) as file:
        insertions = dict()
        for line in file:
            if '->' in line:
                pair, char = line.strip().split(' -> ')
                insertions[pair] = char
            elif line.strip():
                start = line.strip()
    return start, insertions



def puzzle1(test = True):
    string, insertions = read_file(test)
    for step in range(10):
        temp = list()
        prev = None
        for char in string:
            if prev is None: 
                prev = char
                temp.append(char)
                continue
            pair = ''.join([prev,char])
            if pair in insertions:
                temp.append(insertions[pair])
            temp.append(char)
            prev = char
        string = ''.join(temp)
    counts = Counter(string).values()
    print(max(counts) - min(counts))
                
            

def puzzle2(test = True):
    string, insertions = read_file(test)
    counts = Counter()
    prev = None
    for char in string:
        if prev is None: 
            prev = char
            continue
        pair = ''.join([prev,char])
        counts.update([pair])
        prev = char
    print(counts)
    for step in range(40):
        temp = Counter()
        for key in counts:
            if key in insertions:
                middle = insertions[key]
                start, end = key[0], key[1]
                pair1 = ''.join([start,middle])
                pair2 = ''.join([middle,end])
                #print(pair1, counts[key])
                temp[pair1] += counts[key] 
                #print(pair2, counts[key])
                temp[pair2] += counts[key]
            else:
                #print(key, counts[key])
                temp[key] += counts[key]
        #print(temp)
        counts = temp.copy()
    #print(counts)
    temp = Counter()
    for key in counts:
        start, end = key[0], key[1]
        temp[start] += counts[key]
        temp[end] += counts[key]
    for key, val in temp.items():
        temp[key] //= 2
        if key == string[0]:
            temp[key] += 1
        elif key == string[-1]:
            temp[key] += 1
    print(temp)
    counts = temp.values()
    print(max(counts) - min(counts))


puzzle1(False)
puzzle2(False)