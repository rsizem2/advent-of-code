import numpy as np

def read_file(test = True):
    if test:
        filename = '../input/day4.txt'
    else:
        filename = '../input/day4.txt'
        
    boards = list()
    temp = list()
    with open(filename) as file:
        for i, line in enumerate(file):
            if i == 0:
                numbers = list(map(int, line.strip().split(',')))
            elif line == '\n':
                if temp:
                    boards.append(dict(
                        cols = [set(x) for x in zip(*temp)],
                        rows = [set(x) for x in temp]
                        ))
                    temp = list()
            else:
                temp.append(list(map(int, line.strip().split())))
        boards.append(dict(
            cols = [set(x) for x in zip(*temp)],
            rows = [set(x) for x in temp]
            ))
    return numbers, boards

def puzzle1(test = True):
    
    numbers, boards = read_file(test)
    temp = set()
    for number in numbers:
        temp.add(number)
        for board in boards:
            if any(x <= temp for x in board['rows']):
                total = 0
                for x in board['rows']:
                    total += sum([z for z in x if z not in temp])
                print(total*number)
                return
            elif any(x <= temp for x in board['cols']):
                total = 0
                for x in board['rows']:
                    total += sum([z for z in x if z not in temp])
                print(total*number)
                return
    
def puzzle2(test = True):
    numbers, boards = read_file(test)
    boards = {i : board for i,board in enumerate(boards)}
    temp = set()
    for number in numbers:
        temp.add(number)
        if len(boards) == 1: break
        keys = set()
        for i, board in boards.items():
            if any(x <= temp for x in board['rows']):
                keys.add(i)
            elif any(x <= temp for x in board['cols']):
                keys.add(i)
        for i in keys:
            boards.pop(i)
    _, board = boards.popitem()
    total = 0
    for x in board['rows']:
        total += sum([z for z in x if z not in temp])
    print(total*number)
    return
    
puzzle1(False)
puzzle2(False)
    