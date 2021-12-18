import math
import numpy as np
from itertools import permutations

def read_file(test = True):
    if test:
        filename = '../tests/day18.txt'
    else:
        filename = '../input/day18.txt'
    with open(filename) as file:
        lists, strings = list(), list()
        for line in file:
            lists.append(list(eval(line.strip())))
            strings.append(line.strip())
    return lists, strings
            

def explode(x):
    depth = 0
    start, end = 0, 0
    for i, char in enumerate(x):
        if char == '[':
            if depth == 4:
                start = i
            depth += 1
            continue
        if start and char == ']':
            end = i
            break 
        elif char == ']':
            depth -= 1
   
    # no change
    if (start, end) == (0,0):
        return False, x
    try:
        a,b = eval(x[start:end+1])
        #print('explode:',a,b)
    except:
        #print('Failed to unpack:', x[start:end+1])
        assert False
    start = list(x[:start])
    end = list(x[end+1:])
    
    
    for i in range(len(start)-1,-1, -1):
        if start[i] in '[,]': 
            continue
        if i-1 >= 0 and start[i-1] not in '[,]': 
            #print('Add:',''.join([start[i-1],start[i]]), a)
            start = start[:i-1] + [str(int(''.join([start[i-1],start[i]])) + a)] + start[i+1:]
        else:
            #print('Add:',str(int(start[i])), a)
            start[i] = str(int(start[i]) + a)
            
        break
    
    for i in range(len(end)):
        if end[i] in '[,]': 
            continue
        if i+1 < len(end) and end[i+1] not in '[,]':
            #print('Add:',''.join([end[i],end[i+1]]), b)
            end = end[:i] + [str(int(''.join([end[i],end[i+1]])) + b)] + end[i+2:]
        else:
            #print('Add:',int(end[i]), b)
            end[i] = str(int(end[i]) + b)
            
        break
    
    return True, ''.join([*start, '0', *end])
            

def split(x):
    start, end = 0, 0
    found = False
    for i, char in enumerate(x):
        if char not in '[,]':
            if i+1 < len(x) and x[i+1] not in '[,]':
                a = int(''.join([char, x[i+1]]))
                if a < 10 or a > 100:
                    assert False
                #print('split:', a)
                found = True
                break
    if not found: 
        return False, x
    start = list(x[:i])
    end = list(x[i+2:])
    #print(start, a, end)
    return True, ''.join([*start,'[',str(a // 2),',',str(math.ceil(a / 2)),']', *end])
    
def add(x,y):
    temp = ''.join(['[',x,',',y,']'])
    steps = 0
    while True:
        steps += 1
        #print(temp)
        if steps > 15:
            #assert False
            pass
        change, temp = explode(temp)
        if change: 
            continue
        change, temp = split(temp)
        if change: 
            continue
        break
    
    return temp

def magnitude(x):
    # convert to list
    print(x)
    if isinstance(x, str):
        temp = eval(x)
    else:
        temp = x
    x,y = temp
    if isinstance(x, int):
        val_x = x
    else:
        val_x = magnitude(x)
    if isinstance(y, int):
        val_y = y
    else:
        val_y = magnitude(y)
    return 3*val_x + 2*val_y
    

def puzzle1(test = True):
    _, temp = read_file(test)
    x = None
    for line in temp:
        if x is None:
            x = line
        else:
            x = add(x,line)
    print(magnitude(x))
                

def puzzle2(test = True):
    _, temp = read_file(test)
    max_val = -1
    for line1, line2 in permutations(temp,2):
        temp = magnitude(add(line1,line2))
        if temp > max_val:
            max_val = temp
    print(max_val)
            
  

def test_explode():
    assert explode('[[[[[9,8],1],2],3],4]')[1] == '[[[[0,9],2],3],4]'
    assert explode('[7,[6,[5,[4,[3,2]]]]]')[1] == '[7,[6,[5,[7,0]]]]'
    assert explode('[[6,[5,[4,[3,2]]]],1]')[1] == '[[6,[5,[7,0]]],3]'
    assert explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')[1] == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
    assert explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')[1] == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
    print('All explode() tests passed.')
    
def test_split():
    assert split('[[[[0,7],4],[15,[0,13]]],[1,1]]')[1] == '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
    assert split('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')[1] == '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'
    print('All split() tests passed.')

test_explode()
test_split()
puzzle1(False)
puzzle2(False)
