#import numpy as np
from collections import deque

def read_file(test = True):
    if test:
        filename = '../tests/day9.txt'
    else:
        filename = '../input/day9.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(list(map(int,list(line.strip()))))
    return temp

def puzzle1(test = True):
    temp = read_file(test)
    rows = len(temp)
    cols = len(temp[0])
    #print(*temp)
    minima = list()
    for i in range(rows):
        for j in range(cols):
            if i == 0 or temp[i][j] < temp[i-1][j]:
                pass
            else:
                continue
            if i == rows - 1 or temp[i][j] < temp[i+1][j]:
                pass
            else:
                continue
            if 0 == j or temp[i][j] < temp[i][j-1]:
                pass
            else:
                continue
            if j == cols - 1 or temp[i][j] < temp[i][j+1]:
                pass
            else:
                continue
            minima.append(temp[i][j])
    print(sum(minima) + len(minima))

def puzzle2(test = True):
    temp = read_file(test)
    rows = len(temp)
    cols = len(temp[0])
    #print(*temp)
    minima = list()
    for i in range(rows):
        for j in range(cols):
            if i == 0 or temp[i][j] < temp[i-1][j]:
                pass
            else:
                continue
            if i == rows - 1 or temp[i][j] < temp[i+1][j]:
                pass
            else:
                continue
            if 0 == j or temp[i][j] < temp[i][j-1]:
                pass
            else:
                continue
            if j == cols - 1 or temp[i][j] < temp[i][j+1]:
                pass
            else:
                continue
            minima.append((i,j))
    
    sizes = list()
    for point in minima:
        visited = set()
        unvisited = deque([point])
        while unvisited:
            i,j = unvisited.pop()
            if i > 0 and (i-1,j) not in visited and temp[i-1][j] != 9:
                unvisited.append((i-1,j))
            if i < rows - 1  and (i+1,j) not in visited and temp[i+1][j] != 9:
                unvisited.append((i+1,j))
            if j > 0  and (i,j-1) not in visited and temp[i][j-1] != 9:
                unvisited.append((i,j-1))
            if j < cols - 1  and (i,j+1) not in visited and temp[i][j+1] != 9:
                unvisited.append((i,j+1))
            visited.add((i,j))
        sizes.append(len(visited))
    x,y,z = sorted(sizes, reverse = True)[:3]
    print(x*y*z)


puzzle1(False)
puzzle2(False)