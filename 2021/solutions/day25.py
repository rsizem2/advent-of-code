

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
    for line in temp:
        print(*line, sep = '')
    pass

def puzzle2(test = True):
    temp = read_file(test)
    for line in temp:
        print(*line, sep = '')
    pass
        
puzzle1()
puzzle2(False)