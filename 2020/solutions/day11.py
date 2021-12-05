from collections import Counter

OFFSETS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def read_file():
    temp = []
    with open('../input/day11_input.txt') as file:
        for line in file:
            temp.append([x for x in line.strip()])
    return temp

def change_state1(temp, threshold = 4):
    nrow, ncol = len(temp), len(temp[0])
    new = [[None for i in range(ncol)] for j in range(nrow)]
    for i, row in enumerate(temp):
        for j, space in enumerate(row):
            if temp[i][j] == 'L':
                char = "#"
                for m,n in OFFSETS:
                    if i + m < 0 or j + n < 0:
                        continue
                    elif i + m >= nrow or j + n >= ncol:
                        continue
                    elif temp[i+m][j+n] == "#":
                        char = "L"
                        break
            elif temp[i][j] == '#':
                count = 0
                char = "#"
                for m,n in OFFSETS:
                    if i + m < 0 or j + n < 0:
                        continue
                    elif i + m >= nrow or j + n >= ncol:
                        continue
                    elif temp[i+m][j+n] == "#":
                        count += 1
                if count >= threshold:
                    char = "L"
            else:
                char = temp[i][j]
            new[i][j] = char
    return new
    

def puzzle1():
    old = read_file()
    new = change_state1(old)
    while not all(x == y for x,y in zip(old,new)):
        old = [list(x) for x in new] 
        new = change_state1(new)
    count = Counter()
    for x in old:
        count.update(x)
    print(count["#"])
    
def change_state2(temp, threshold = 5):
    nrow, ncol = len(temp), len(temp[0])
    new = [[None for i in range(ncol)] for j in range(nrow)]
    for i, row in enumerate(temp):
        for j, space in enumerate(row):
            if temp[i][j] == 'L':
                char = "#"
                for m,n in OFFSETS:
                    for k in range(1,max(nrow,ncol)):
                        if not (0 <= i + k*m < nrow and 0 <= j + k*n < ncol):
                            break
                        elif temp[i+k*m][j+k*n] == ".":
                            continue
                        elif temp[i+k*m][j+k*n] == "#":
                            char = "L"
                            break
                        else:
                            break
            elif temp[i][j] == '#':
                count = 0
                char = "#"
                for m,n in OFFSETS:
                    for k in range(1,max(nrow,ncol)):
                        if not (0 <= i + k*m < nrow and 0 <= j + k*n < ncol):
                            break
                        elif temp[i+k*m][j+k*n] == ".":
                            continue
                        elif temp[i+k*m][j+k*n] == "#":
                            count += 1
                            break
                        else:
                            break
                if count >= threshold:
                    char = "L"
            else:
                char = temp[i][j]
            new[i][j] = char
    return new   
    
def puzzle2():
    old = read_file()
    for x in old:
        print("".join(x))
    print()
    new = change_state2(old)
    while not all(x == y for x,y in zip(old,new)):
        old = [list(x) for x in new]
        for x in old:
            print("".join(x))
        print()
        new = change_state2(new)
    count = Counter()
    for x in old:
        count.update(x)
    print(count["#"])
                
            
        
puzzle1()
puzzle2()