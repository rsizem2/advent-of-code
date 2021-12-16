import numpy as np
from collections import deque, Counter

def read_file(test = True):
    if test:
        filename = '../tests/day16.txt'
    else:
        filename = '../input/day16.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp = list(line.strip())
    return temp

convert = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
    }

def parse(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6],2)
    print(version, type_id)
    index = 6
    if type_id == 4:
        literal = list()
        while packet[index] == '1':
            literal.append(packet[index+1:index+5])
            index += 5
        literal.append(packet[index+1:index+5])
        literal = int(''.join(literal), 2)
        while index % 4 != 2:
            index += 1
        print(literal)
        print(packet[index:])
        if packet[index:]:
            parse(packet[index:])
        else:
            return
    else:
        if packet[index] == '0':
            length = int(packet[index+1,index+16], 2)
        elif packet[index] == '1':
            num_packets = int(packet[index+1,index+12], 2)
        else:
            assert False

def puzzle1(test = True):
    temp = read_file(test)
    temp = ''.join(list(map(lambda x: convert[x], temp)))
    print(temp)
    parse(temp)
                

def puzzle2(test = True):
    temp = read_file(test)


puzzle1()
puzzle2()