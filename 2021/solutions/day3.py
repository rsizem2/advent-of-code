# Using integer division messed up my solution for part 2 >:( 

def read_file(test = True):
    if test:
        filename = '..\input\day3_test.txt'
    else:
        filename = '..\input\day3_input.txt'
    with open(filename) as file:
        temp = [line.strip() for line in file]
    return temp

def puzzle1(test = True):
    temp = read_file(test)
    counts = [0]*len(temp[0])
    for line in temp:
        for i, char in enumerate(line):
            if char == '1':
                counts[i] += 1
    gamma, epsilon = list(), list()
    for num in counts:
        if num >= len(temp) // 2:
            gamma += ['1']
            epsilon += ['0']
        else:
            epsilon += ['1']
            gamma += ['0']
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    print(gamma*epsilon)
    
def puzzle2(test = True):
    temp = read_file(test)
    pos = 0
    while len(temp) > 1:
        count = 0
        for line in temp:
            print(line)
            if line[pos] == '1':
                count += 1
        print(count, len(temp))
        if count >= len(temp) / 2:
            temp = [x for x in temp if x[pos] == '1']
        else:
            temp = [x for x in temp if x[pos] == '0']
        pos += 1
        print(temp)
    print(temp[0])
    oxygen = int(temp[0],2)
    
    temp = read_file(test)
    pos = 0
    while len(temp) > 1:
        count = 0
        for line in temp:
            print(line)
            if line[pos] == '1':
                count += 1
        
        if count >= len(temp) / 2:
            temp = [x for x in temp if x[pos] == '0']
        else:
            temp = [x for x in temp if x[pos] == '1']
        pos += 1
        print(temp)
    print(temp[0])
    c02 = int(temp[0],2)
    
    print(oxygen*c02)

puzzle1()
puzzle2(False)