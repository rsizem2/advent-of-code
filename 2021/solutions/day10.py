from collections import deque

def read_file(test = True):
    if test:
        filename = '../tests/day10.txt'
    else:
        filename = '../input/day10.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(list(line.strip()))
    return temp

SCORES = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
    }

def puzzle1(test = True):
    temp = read_file(test)
    score = 0
    for line in temp:
        parser = deque()
        for char in line:
            if char in '[{(<':
                parser.append(char)
            elif char in ']})>':
                opener = parser.pop()
                if opener == '[' and char != ']':
                    score += SCORES[char]
                    break
                if opener == '{'and char != '}':
                    score += SCORES[char]
                    break
                if opener == "("and char != ')':
                    score += SCORES[char]
                    break
                if opener == '<'and char != '>':
                    score += SCORES[char]
                    break
    print(score)
            


def puzzle2(test = True):
    temp = read_file(test)
    score = 0
    incomplete = list()
    for line in temp:
        parser = deque()
        corrupt = False
        for char in line:
            if char in '[{(<':
                parser.append(char)
            elif char in ']})>':
                opener = parser.pop()
                if opener == '[' and char != ']':
                    corrupt = True
                    break
                if opener == '{'and char != '}':
                    corrupt = True
                    break
                if opener == "("and char != ')':
                    corrupt = True
                    break
                if opener == '<'and char != '>':
                    corrupt = True
                    break
        if corrupt == False:
            incomplete.append(line)
    scores = list()
    for line in incomplete:
        parser = deque()
        for char in line:
            if char in '[{(<':
                parser.append(char)
            elif char in ']})>':
                opener = parser.pop()
        temp_score = 0
        while parser:
            temp_score *= 5
            char = parser.pop()
            if char == '(':
                temp_score += 1
            elif char == '[':
                temp_score += 2
            elif char == '{':
                temp_score += 3
            elif char == '<':
                temp_score += 4
        scores.append(temp_score)
        scores = sorted(scores)
                
    print(scores[len(scores)//2])

puzzle1(False)
puzzle2(False)