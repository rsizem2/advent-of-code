
import numpy as np

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
            

def add(x,y):
    temp = ''.join(['[',x,',',y,']'])
    while True:
        change, temp = explode(temp)
        if change: 
            continue
        change, temp = split(temp)
        if not change: break 
    return temp

def explode(x):
    depth = 0
    start, end = 0, 0
    for i, char in enumerate(x):
        if char == '[':
            if depth == 4:
                start = i
            depth += 1
            continue
        if depth != 5 and char == ']':
            depth -= 1
            continue
        elif depth != 5:
            continue
        
        if char == ']':
            end = i
            break 
   
    # no change
    if (start, end) == (0,0):
        return False, x
    a,b = eval(x[start:end+1])
    start = list(x[:start])
    end = list(x[end+1:])
    
    
    for i in range(-1,-len(start), -1):
        if start[i] in '[,]': 
            continue
        start[i] = str(int(start[i]) + a)
        break
    
    for i in range(len(end)):
        if end[i] in '[,]': 
            continue
        end[i] = str(int(end[i]) + b)
        break
    
    return ''.join([*start, '0', *end])
            

def split(x):
    pass
    


def puzzle1(test = True):
    _, temp = read_file(test)
    for line in temp:
        print(line)
                

def puzzle2(test = True):
    temp = read_file(test)
  

def test_explode():
    assert explode('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]'
    assert explode('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]'
    assert explode('[[6,[5,[4,[3,2]]]],1]') == '[[6,[5,[7,0]]],3]'
    assert explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
    assert explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
    print('All explode() tests passed.')

test_explode()
puzzle1()
puzzle2()
