import numpy as np
from collections import Counter

def read_file(test = True):
    if test:
        filename = '../tests/day5.txt'
    else:
        filename = '../input/day5.txt'
    
    with open(filename) as file:
        temp = [line.strip().split(' -> ') for line in file]
    points = list()
    for x,y in temp:
        points.append([tuple(map(int, x.split(','))), tuple(map(int, y.split(',')))])
    
    return points

def puzzle1(test = True):
    points = read_file(test)
    lines = list()
    count = Counter()
    for a,b in points:
        x1,y1 = a
        x2,y2 = b
        if x1 == x2:
            y1, y2 = sorted([y1,y2])
            lines.append(set([(x1,y) for y in np.arange(y1,y2+1)]))
        elif y1 == y2:
            x1, x2 = sorted([x1,x2])
            lines.append(set([(x,y1) for x in np.arange(x1,x2+1)]))
    for points in lines:
        count.update(points)
    intersections = 0
    for point, num in count.items():
        if num > 1:
            intersections += 1
    print(intersections)

def puzzle2(test = True):
    points = read_file(test)
    lines = list()
    count = Counter()
    for a,b in points:
        x1,y1 = a
        x2,y2 = b
        if x1 == x2:
            y1, y2 = sorted([y1,y2])
            lines.append(set([(x1,y) for y in np.arange(y1,y2+1)]))
        elif y1 == y2:
            x1, x2 = sorted([x1,x2])
            lines.append(set([(x,y1) for x in np.arange(x1,x2+1)]))
        elif x1 < x2 and y1 < y2:
            x = np.arange(x1,x2+1)
            y = np.arange(y1,y2+1)
            lines.append(set(zip(x,y)))
        elif x1 < x2 and y1 > y2:
            x = np.arange(x1,x2+1)
            y = np.arange(y1,y2-1,-1)
            lines.append(set(zip(x,y)))
        elif x1 > x2 and y1 < y2:
            x = np.arange(x1,x2-1,-1)
            y = np.arange(y1,y2+1)
            lines.append(set(zip(x,y)))
        elif x1 > x2 and y1 > y2:
            x = np.arange(x1,x2-1,-1)
            y = np.arange(y1,y2-1,-1)
            lines.append(set(zip(x,y)))
            
    for points in lines:
        count.update(points)
    intersections = 0
    for point, num in count.items():
        if num > 1:
            intersections += 1
    print(intersections)

puzzle1(False)
puzzle2(False)
