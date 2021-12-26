

def read_file(test = True):
    if test:
        filename = '../tests/day25.txt'
    else:
        filename = '../input/day25.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(list(line.strip()))
    return temp

def puzzle1(test = True):
    temp = read_file(test)
    right, down = set(), set()
    rows, cols = len(temp), len(temp[0])
    for row, line in enumerate(temp):
        for col, x in enumerate(line):
            if x == 'v':
                down.add((row, col))
            elif x == '>':
                right.add((row, col))
    steps = 0
    while True:
        new_right, new_down = set(), set()
        change = False
        for i,j in right:
            k = (j + 1) % cols
            # nothing in the way
            if (i,k) not in right and (i,k) not in down:
                new_right.add((i,k))
                change = True
            else:
                new_right.add((i,j))
        for i,j in down:
            k = (i + 1) % rows
            if (k,j) not in new_right and (k,j) not in down:
                new_down.add((k,j))
                change = True
            else:
                new_down.add((i,j))
        if not change:
            steps += 1
            break
        right, down = new_right, new_down
        steps += 1
        #print(steps)
    print(steps)

def puzzle2(test = True):
    temp = read_file(test)
    for line in temp:
         pass
        
puzzle1(False)
puzzle2()