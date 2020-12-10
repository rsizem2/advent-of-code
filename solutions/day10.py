from collections import Counter

def read_file():
    temp = []
    with open('../input/day10_input.txt') as file:
        for line in file:
            temp.append(int(line.strip()))
    return sorted(temp)

def puzzle1():
    temp = [0]
    temp.extend(read_file())
    temp.append(temp[-1] + 3)
    diffs = []
    for i, x in enumerate(temp[1:]):
        diffs.append(x - temp[i])
    temp = Counter(diffs)
    print(temp[1]*temp[3])
    
def puzzle2():
    temp = read_file()
    num_paths = [1 for x in temp]
    for i, x in enumerate(temp):
        paths = 0
        if x <= 3:
            paths = 1
        j = i-1
        while j >= 0 and x - 3 <= temp[j]:
            paths += num_paths[j]
            j -= 1
        num_paths[i] = paths
    print(num_paths[-1])

puzzle1()
puzzle2()