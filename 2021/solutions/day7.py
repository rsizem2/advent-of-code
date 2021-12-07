import numpy as np

def read_file(test = True):
    if test:
        filename = '../tests/day7.txt'
    else:
        filename = '../input/day7.txt'
    with open(filename) as file:
        for line in file:
            temp = list(map(int,line.strip().split(',')))
    return np.array(temp)

def puzzle1(test = True):
    temp = read_file(test)
    lower, upper = temp.min(), temp.max()
    min_total = np.Inf 
    min_val = None
    for val in np.arange(lower, upper + 1):
        #print(val)
        diff = np.abs(temp - val)
        #print(diff)
        total = diff.sum()
        #print(total)
        if total < min_total:
            min_total = total
            min_val = val
            
    print(min_total)
    

def puzzle2(test = True):
    temp = read_file(test)
    lower, upper = temp.min(), temp.max()
    min_total = np.Inf 
    min_val = None
    for val in np.arange(lower, upper + 1):
        #print(val)
        diff = np.abs(temp - val)
        #print(diff)
        total = np.array(list(map(lambda x: (x*(x+1)) // 2, diff))).sum()
        
        #print(total)
        if total < min_total:
            min_total = total
            min_val = val
            
    print(min_total)

puzzle1(False)
puzzle2(False)