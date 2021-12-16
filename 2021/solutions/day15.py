import numpy as np
from collections import deque, Counter

def read_file(test = True):
    if test:
        filename = '../tests/day15.txt'
    else:
        filename = '../input/day15.txt'
    with open(filename) as file:
        costs = list()
        for line in file:
            costs.append(list(map(int,list(line.strip()))))
    return costs


def puzzle1(test = True):
    costs = read_file(test)
    seen = set([(0,0)])
    unvisited = set([(i,j) for i in range(len(costs)) for j in range(len(costs[0]))])
    dist = [[np.Inf]*len(costs) for j in range(len(costs[0]))]
    prev = [[None]*len(costs) for j in range(len(costs[0]))]
    dist[0][0] = 0
    while unvisited:
        i,j = min(unvisited & seen, key = lambda x: dist[x[0]][x[1]])
        #print(i,j)
        unvisited.remove((i,j))
        if (i-1,j) in unvisited:
            seen.add((i-1,j))
            temp = dist[i][j] + costs[i-1][j]
            if temp < dist[i-1][j]:
                dist[i-1][j] = temp
                prev[i-1][j] = (i,j)
        if (i+1,j) in unvisited:
            seen.add((i+1,j))
            temp = dist[i][j] + costs[i+1][j]
            if temp < dist[i+1][j]:
                dist[i+1][j] = temp
                prev[i+1][j] = (i,j)
        if (i,j-1) in unvisited:
            seen.add((i,j-1))
            temp = dist[i][j] + costs[i][j-1]
            if temp < dist[i][j-1]:
                dist[i][j-1] = temp
                prev[i][j-1] = (i,j)
        if (i,j+1) in unvisited:
            seen.add((i,j+1))
            temp = dist[i][j] + costs[i][j+1]
            if temp < dist[i][j+1]:
                dist[i][j+1] = temp
                prev[i][j+1] = (i,j)
        
    print(dist[len(costs)-1][len(costs[0])-1])
                

def puzzle2(test = True):
    costs = np.array(read_file(test))
    arrays = [[None]*5 for j in range(5)]
    for i in range(5):
        for j in range(5):
            if j != 0:
                arrays[i][j] = (arrays[i][j-1]) % 9 + 1
            elif i != 0:
                arrays[i][j] = (arrays[i-1][j]) % 9 + 1
            else:
                arrays[i][j] = costs
    costs = np.block(arrays)
    seen = set([(0,0)])
    unvisited = set([(i,j) for i in range(len(costs)) for j in range(len(costs[0]))])
    dist = [[np.Inf]*len(costs) for j in range(len(costs[0]))]
    prev = [[None]*len(costs) for j in range(len(costs[0]))]
    dist[0][0] = 0
    print(f'Total: {len(costs)*len(costs[0])}')
    counter = 0
    while unvisited:
        i,j = min(unvisited & seen, key = lambda x: dist[x[0]][x[1]])
        #print(i,j)
        if i == len(costs) - 1 and j == len(costs[0]) - 1:
            break
        unvisited.remove((i,j))
        counter += 1
        if counter % 1000 == 0:
            print('Count:', counter)
        if (i-1,j) in unvisited:
            seen.add((i-1,j))
            temp = dist[i][j] + costs[i-1][j]
            if temp < dist[i-1][j]:
                dist[i-1][j] = temp
                prev[i-1][j] = (i,j)
        if (i+1,j) in unvisited:
            seen.add((i+1,j))
            temp = dist[i][j] + costs[i+1][j]
            if temp < dist[i+1][j]:
                dist[i+1][j] = temp
                prev[i+1][j] = (i,j)
        if (i,j-1) in unvisited:
            seen.add((i,j-1))
            temp = dist[i][j] + costs[i][j-1]
            if temp < dist[i][j-1]:
                dist[i][j-1] = temp
                prev[i][j-1] = (i,j)
        if (i,j+1) in unvisited:
            seen.add((i,j+1))
            temp = dist[i][j] + costs[i][j+1]
            if temp < dist[i][j+1]:
                dist[i][j+1] = temp
                prev[i][j+1] = (i,j)
        
    print(dist[len(costs)-1][len(costs[0])-1])

puzzle1()
puzzle2(False)