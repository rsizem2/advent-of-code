

def read_file(test = True):
    if test:
        filename = '..\input\day2_test.txt'
    else:
        filename = '..\input\day2_input.txt'
    with open(filename) as file:
        temp = [line.strip().split() for line in file]
    return temp

def puzzle1(test = True):
    temp = read_file(test)
    x, y = 0,0
    for move, steps in temp:
        if move == "forward":
            x += int(steps)
        elif move == "down":
            y += int(steps)
        else:
            y -= int(steps)
    print(x*y)


def puzzle2(test = True):
    temp = read_file(test)
    aim = 0
    x, y = 0,0
    for move, steps in temp:
        if move == "forward":
            x += int(steps)
            y += aim*int(steps)
        elif move == "down":
            aim += int(steps)
        else:
            aim -= int(steps)
    print(x*y)
    
puzzle1(False)
puzzle2(False)