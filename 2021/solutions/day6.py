from collections import Counter

def read_file(test = True):
    if test:
        filename = '../tests/day6.txt'
    else:
        filename = '../input/day6.txt'
    with open(filename) as file:
        for line in file:
            temp = list(map(int, line.strip().split(',')))
    return temp

def puzzle1(test = True):
    fish = read_file(test)
    for day in range(80):
        temp = list()
        for i, x in enumerate(fish):
            if x == 0:
                temp.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
        fish.extend(temp) 
    print(f'Number of Fish: {len(fish)}')

def puzzle2(test = True):
    days = 256
    fish = Counter(read_file(test))
    for day in range(days):
        temp = {age:0 for age in range(9)}
        for age, num in fish.items():
            if age == 0:
                temp[6] += num
                temp[8] += num
            else:
                temp[age - 1] += num
        fish = temp 
    total = 0
    for key, val in fish.items():
        total += val
    print(f'Number of Fish: {total}')

puzzle1()
puzzle2(False)