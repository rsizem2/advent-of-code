from collections import deque

def read_file(test = True):
    if test:
        filename = '../tests/day11.txt'
    else:
        filename = '../input/day11.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(list(map(int,list(line.strip()))))
    return temp

def puzzle1(test = True):
    temp = read_file(test)
    rows = len(temp)
    cols = len(temp[0])
    flashes = 0
    for step in range(100):
        flashed = set()
        will_flash = deque()
        if step < 3:
            for x in temp:
                print(*x)
            print(f'\n{flashes}\n')
        for i in range(rows):
            for j in range(cols):
                temp[i][j] += 1
                if temp[i][j] > 9:
                    flashed.add((i,j))
                    will_flash.append((i,j))
        while will_flash:
            i,j = will_flash.pop()
            if i > 0:
                temp[i-1][j] += 1
                if temp[i-1][j] > 9 and (i-1,j) not in flashed:
                    will_flash.append((i-1,j))
                    flashed.add((i-1,j))
            if i < rows-1:
                temp[i+1][j] += 1
                if temp[i+1][j] > 9 and (i+1,j) not in flashed:
                    will_flash.append((i+1,j))
                    flashed.add((i+1,j))
            if j > 0:
                temp[i][j-1] += 1
                if temp[i][j-1] > 9 and (i,j-1) not in flashed:
                    will_flash.append((i,j-1))
                    flashed.add((i,j-1))
            if j < cols-1:
                temp[i][j+1] += 1
                if temp[i][j+1] > 9 and (i,j+1) not in flashed:
                    will_flash.append((i,j+1))
                    flashed.add((i,j+1))
            if i > 0 and j > 0:
                temp[i-1][j-1] += 1
                if temp[i-1][j-1] > 9 and (i-1,j-1) not in flashed:
                    will_flash.append((i-1,j-1))
                    flashed.add((i-1,j-1))
            if i > 0 and j < cols-1:
                temp[i-1][j+1] += 1
                if temp[i-1][j+1] > 9 and (i-1,j+1) not in flashed:
                    will_flash.append((i-1,j+1))
                    flashed.add((i-1,j+1))
            if i < rows - 1 and j > 0:
                temp[i+1][j-1] += 1
                if temp[i+1][j-1] > 9 and (i+1,j-1) not in flashed:
                    will_flash.append((i+1,j-1))
                    flashed.add((i+1,j-1))
            if i < rows-1 and j < cols-1:
                temp[i+1][j+1] += 1
                if temp[i+1][j+1] > 9 and (i+1,j+1) not in flashed:
                    will_flash.append((i+1,j+1))
                    flashed.add((i+1,j+1))
        flashes += len(flashed)
        for i,j in flashed:
            temp[i][j] = 0
    print(flashes)
            


def puzzle2(test = True):
    temp = read_file(test)
    temp = read_file(test)
    rows = len(temp)
    cols = len(temp[0])
    total = rows*cols
    flashes = 0
    for step in range(20000):
        flashed = set()
        will_flash = deque()
        if step < 3:
            for x in temp:
                print(*x)
            print(f'\n{flashes}\n')
        for i in range(rows):
            for j in range(cols):
                temp[i][j] += 1
                if temp[i][j] > 9:
                    flashed.add((i,j))
                    will_flash.append((i,j))
        while will_flash:
            i,j = will_flash.pop()
            if i > 0:
                temp[i-1][j] += 1
                if temp[i-1][j] > 9 and (i-1,j) not in flashed:
                    will_flash.append((i-1,j))
                    flashed.add((i-1,j))
            if i < rows-1:
                temp[i+1][j] += 1
                if temp[i+1][j] > 9 and (i+1,j) not in flashed:
                    will_flash.append((i+1,j))
                    flashed.add((i+1,j))
            if j > 0:
                temp[i][j-1] += 1
                if temp[i][j-1] > 9 and (i,j-1) not in flashed:
                    will_flash.append((i,j-1))
                    flashed.add((i,j-1))
            if j < cols-1:
                temp[i][j+1] += 1
                if temp[i][j+1] > 9 and (i,j+1) not in flashed:
                    will_flash.append((i,j+1))
                    flashed.add((i,j+1))
            if i > 0 and j > 0:
                temp[i-1][j-1] += 1
                if temp[i-1][j-1] > 9 and (i-1,j-1) not in flashed:
                    will_flash.append((i-1,j-1))
                    flashed.add((i-1,j-1))
            if i > 0 and j < cols-1:
                temp[i-1][j+1] += 1
                if temp[i-1][j+1] > 9 and (i-1,j+1) not in flashed:
                    will_flash.append((i-1,j+1))
                    flashed.add((i-1,j+1))
            if i < rows - 1 and j > 0:
                temp[i+1][j-1] += 1
                if temp[i+1][j-1] > 9 and (i+1,j-1) not in flashed:
                    will_flash.append((i+1,j-1))
                    flashed.add((i+1,j-1))
            if i < rows-1 and j < cols-1:
                temp[i+1][j+1] += 1
                if temp[i+1][j+1] > 9 and (i+1,j+1) not in flashed:
                    will_flash.append((i+1,j+1))
                    flashed.add((i+1,j+1))
        flashes += len(flashed)
        for i,j in flashed:
            temp[i][j] = 0
        if len(flashed) >= total:
            print('Done')
            print(step+1)
            return


puzzle1(False)
puzzle2(False)