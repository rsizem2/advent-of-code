from collections import Counter, defaultdict
from itertools import combinations
import re


def read_file(test = True):
    if test:
        filename = '../tests/day5.txt'
    else:
        filename = '../input/day5.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(line.strip())
    return temp

def puzzle1():
    temp = read_file(False)
    nice = 0
    for line in temp:
        if sum([(x in ['a','e','i','o','u']) for x in line]) < 3:
            continue
        elif any([x in line for x in ['ab', 'cd', 'pq', 'xy']]):
            continue
        for i, x in enumerate(line):
            if i+1 == len(line):
                pass
            elif x == line[i+1]:
                nice += 1
                break
    print(nice)

def puzzle2():
    temp = read_file(False)
    nice = 0
    for line in temp:
        counts = Counter([line[i:i+2] for i in range(0,len(line)+1)])
        places = defaultdict(list)
        for i in range(0,len(line)+1):
            places[line[i:i+2]].append(i)
        if counts.most_common(1)[0][1] < 2:
            # no length 2 substring appears twice
            continue
        counts = [x for x in counts.keys() if counts[x] > 1]
        if any([abs(i-j) > 1 for x in counts for i,j in combinations(places[x], 2)]):
            # at least one length 2 substring does not overlap
            pass
        else:
            continue
        if any([line[i] == line[i+2] for i in range(len(line)-2)]):
            print(line)
        else:
            continue
        nice += 1
    print(nice)


puzzle1()
puzzle2()
