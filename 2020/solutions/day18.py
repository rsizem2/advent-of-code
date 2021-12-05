from collections import deque

def read_file():
    temp = []
    with open('../input/day18_input.txt') as file:
        for line in file:
            temp.append(list(line.strip().replace(" ", "")))
    return temp

def eval_exp(i, temp):
    total = 0
    op = "+"
    while i < len(temp):
        if temp[i].isdigit():
            if op == "+":
                total += int(temp[i])
            elif op == "*":
                total *= int(temp[i])
            else:
                print("invalid op")
                assert False
            i += 1
        elif temp[i] == "(":
            i += 1
            val, i = eval_exp(i, temp)
            if op == "+":
                total += val
            else:
                total *= val
        elif temp[i] == ")":
            i += 1
            break
        else:
            op = temp[i]
            i += 1
    return total, i
    
def eval_exp2(i, temp, mult = False):
    total = 0
    op = "+"
    while i < len(temp):
        if temp[i].isdigit():
            if op == "+":
                total += int(temp[i])
            elif op == "*":
                total *= int(temp[i])
            else:
                print("invalid op")
                assert False
            i += 1
        elif temp[i] == "(":
            i += 1
            val, i = eval_exp2(i, temp)
            if op == "+":
                total += val
            else:
                total *= val
        elif temp[i] == "+":
            op = temp[i]
            i += 1
        elif temp[i] == "*":
            op = temp[i]
            i += 1
            val, i = eval_exp2(i, temp, True)
            total *= val
        else:
            if mult:
                break
            i += 1
            break
    return total, i

def puzzle1():
    temp = read_file()
    ans = []
    for line in temp:
        ans.append(eval_exp(0, line))
    print(sum([x[0] for x in ans]))
        
            
def puzzle2():
    temp = read_file()
    ans = []
    for line in temp:
        ans.append(eval_exp2(0, line))
    print([x[0] for x in ans])
    print(sum([x[0] for x in ans]))

puzzle1()
puzzle2()