from collections import deque


def read_file(test = True):
    if test:
        filename = '../tests/day1.txt'
    else:
        filename = '../input/day1.txt'
        
    with open(filename) as file:
        temp = [int(line.strip()) for line in file]
    return temp


def puzzle1(test = True):
    depths = read_file(test)
    prev = None
    total = 0
    for x in depths:
        if prev is not None and x > prev:
            total += 1
        prev = x
    return total

def puzzle2(test = True):
    depths = read_file(test)
    old_window = deque(depths[:3], maxlen=3)
    prev = sum(old_window)
    total = 0
    for i, x in enumerate(depths[3:]):
        old_window.append(x)
        temp = sum(old_window)
        if prev is not None and temp > prev:
            #print(old_window, temp)
            total += 1
        prev = temp
    return total
    

print(puzzle1(False))
print(puzzle2(False))
