#import numpy as np
from collections import Counter

def read_file(test = True):
    if test:
        filename = '../tests/day8.txt'
    else:
        filename = '../input/day8.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            code, output = line.strip().split(" | ")
            code = code.split()
            output = output.split()
            temp.append([sorted(code, key=lambda x: len(x)), output])
    return temp

NUMBERS = {
    frozenset('abcefg') : '0',
    frozenset('cf') : '1',
    frozenset('acdeg') : '2',
    frozenset('acdfg') : '3',
    frozenset('bcdf') : '4',
    frozenset('abdfg') : '5',
    frozenset('abdefg') : '6',
    frozenset('acf') : '7',
    frozenset('abcdefg') : '8',
    frozenset('abcdfg') : '9'
    }

print(NUMBERS)

def puzzle1(test = True):
    temp = read_file(test)
    #print(*temp)
    count = 0
    for code, output in temp:
        for word in output:
            if len(word) in [2,3,4,7]:
                count += 1
    print(count)

def puzzle2(test = True):
    temp = read_file(test)
    count = 0
    #print(*temp)
    numbers = list()
    for code, output in temp:
        #print(code)
        cypher = dict()
        wire_count = Counter()
        for word in code:
            wire_count.update(word)
        #print(wire_count)
        for letter, count in wire_count.items():
            if count == 6:
                cypher[letter] = 'b'
            elif count == 4:
                cypher[letter] = 'e'
            elif count == 9:
                cypher[letter] = 'f'
            elif count == 8:
                if letter not in set(code[0]):
                    cypher[letter] = 'a'
                else:
                    cypher[letter] = 'c'
            elif count == 7:
                if all(letter in set(code[i]) for i in range(6,9)):
                    cypher[letter] = 'g'
                else:
                    cypher[letter] = 'd'
        #print(cypher)
        
        digits = list()
        for word in output:
            translation = frozenset([cypher[x] for x in word])
            digits.append(NUMBERS[translation])
        numbers.append(int(''.join(digits)))
    print(sum(numbers))

puzzle1(False)
puzzle2(False)