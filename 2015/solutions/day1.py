
def read_file(test = True):
    if test:
        filename = '../tests/day1.txt'
    else:
        filename = '../input/day1.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(line.strip())
    return temp

def puzzle1():
    temp = read_file(False)[0]
    floor = 0
    for char in temp:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            raise ValueError
    print(floor)
    
def puzzle2():
    temp = read_file(False)[0]
    floor = 0
    for i, char in enumerate(temp, start = 1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            raise ValueError
        if floor == -1:
            break
    print(i)
    
puzzle1()
puzzle2()