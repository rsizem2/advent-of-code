import numpy as np

def read_file(test = True):
    if test:
        filename = '../tests/day13.txt'
    else:
        filename = '../input/day13.txt'
    with open(filename) as file:
        points, folds = list(), list()
        for line in file:
            if ',' in line:
                points.append(tuple(map(int,line.strip().split(','))))
            elif '=' in line:
                temp = line.strip().split()[2]
                axis, value = temp.split('=')
                folds.append((axis, int(value)))
    return points, folds




def puzzle1(test = True):
    points, folds = read_file(test)
    rows = max([y for x,y in points])
    cols = max([x for x,y in points])
    grid = [['.' for j in range(cols+1)] for i in range(rows+1)]
    for x,y in points:
        grid[y][x] = '#'
    temp = np.array(grid)
    #print(grid)
    for i, (axis, val) in enumerate(folds):
        if i > 0: break
        if axis == 'y':
            half1 =  temp[:val, :]
            half2 = np.flipud(temp[val+1:, :])
        elif axis == 'x':
            half1 =  temp[:, :val]
            half2 = np.fliplr(temp[:, val+1:])
        temp = half1.copy()
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                if half2[i][j] == '#':
                    temp[i][j] = '#'
    count = 0  
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if temp[i][j] == '#':
                count += 1
    print(count)
            
        
        
            

def puzzle2(test = True):
    points, folds = read_file(test)
    rows = max([y for x,y in points])
    cols = max([x for x,y in points])
    grid = [['.' for j in range(cols+1)] for i in range(rows+1)]
    for x,y in points:
        grid[y][x] = '#'
    temp = np.array(grid)
    #print(grid)
    for i, (axis, val) in enumerate(folds):
        #if i > 0: break
        if axis == 'y':
            half1 =  temp[:val, :]
            half2 = np.flipud(temp[val+1:, :])
        elif axis == 'x':
            half1 =  temp[:, :val]
            half2 = np.fliplr(temp[:, val+1:])
        temp = half1.copy()
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                if half2[i][j] == '#':
                    temp[i][j] = '#'
    count = 0  
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if temp[i][j] == '#':
                count += 1
    print(count)
    for row in temp:
        print(''.join(row))


puzzle1(False)
puzzle2(False)