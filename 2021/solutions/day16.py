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

def pop(queue, n):
    temp = list()
    for i in range(n):
        temp.append(queue.popleft())
    return ''.join(temp), queue

def parse1(packet, count):
    
    if not packet:
        return count, packet
    
    try:
        current = list()
        
        # Version number
        version, packet = pop(packet, 3)
        current.extend(list(version))
        version = int(version,2)
        count += version
        
        # Type ID
        type_id, packet = pop(packet, 3)
        current.extend(list(type_id))
        type_id = int(type_id,2)
        print(count)
        
        # Parse literal
        if type_id == 4:
            temp, packet = pop(packet, 1)
            current.append(temp)
            literal = list()
            # read while indicator bit = 1
            while temp == '1':
                temp, packet = pop(packet, 4)
                current.extend(list(temp))
                literal.append(temp)
                temp, packet = pop(packet, 1)
                current.extend(list(temp))
            temp, packet = pop(packet, 4)
            current.extend(list(temp))
            literal.append(temp)
            literal = int(''.join(literal), 2)
            # Find extraneous 0's
            while len(current) % 4 and packet:
                temp, packet = pop(packet, 1)
                current.extend(list(temp))
                assert temp == '0'
            print(literal)
            if packet:
                return parse1(packet, count)
            return packet, count
        temp, packet = pop(packet, 1)
        current.extend(list(temp))
        if temp == '0':
            # find length of subpackets
            temp, packet = pop(packet, 15)
            current.extend(list(temp))
            total_bits = int(temp,2)
            # Parse subpackets
            temp, packet = pop(packet, total_bits)
            current.extend(list(temp))
            new = deque(temp)
            _, count = parse1(new, count)
            if packet:
                return parse1(packet, count)
            return packet, count
        elif temp == '1':
            # find number of subpackets
            temp, packet = pop(packet, 11)
            current.extend(list(temp))
            total_packets = int(temp,2)
            for i in range(total_packets):
                packet, count = parse1(packet, count)
            if packet:
                return parse1(packet, count)
            return packet, count
    except:
        return deque(), count
                

def puzzle1(test = True):
    temp = ''.join(list(map(lambda x: convert[x], read_file(test))))
    temp = deque(temp)
    _, count = parse1(temp, 0)
    print(count)


def puzzle2(test = True):
    temp = read_file(test)


puzzle1()
puzzle2()
