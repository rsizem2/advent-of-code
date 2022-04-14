from itertools import combinations


def read_file(test = True):
    if test:
        filename = '../tests/day2.txt'
    else:
        filename = '../input/day2.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(sorted(map(int,line.strip().split('x'))))
    return temp

def puzzle1():
    temp = read_file(False)
    total = 0
    for x in temp:
        for i, (side1, side2) in enumerate(combinations(x, 2)):
            if i == 0: 
                # smallest side
                total += 3*side1*side2
            else:
                # other sides
                total += 2*side1*side2
    print(total)
    
def puzzle2():
    temp = read_file(False)
    total = 0
    for x,y,z in temp:
        # ribbon
        total += 2*x + 2*y
        # bow
        total += x*y*z
    print(total)
        
puzzle1()
puzzle2()