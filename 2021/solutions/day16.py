import numpy as np
from collections import deque, Counter
from functools import reduce

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

def pop(packet, n):
    temp = list()
    for i in range(n):
        temp.append(packet.popleft())
    return packet, ''.join(temp),

def parse_outer(packet):
    
    # Version number
    packet, version = pop(packet, 3)
    version = int(version,2)
    count = version
        
    # Type ID
    packet, type_id = pop(packet, 3)
    type_id = int(type_id,2)
    
    if type_id == 4:
        # Literal
        #print('Literal')
        #print(version, count)
        literal = list()
        packet, temp = pop(packet, 1)
        while temp == '1':
            packet, temp = pop(packet, 4)
            literal.append(temp)
            packet, temp = pop(packet, 1)
        # remaining bits
        packet, temp = pop(packet, 4)
        literal.append(temp)
        literal = int(''.join(literal), 2)
    else:
        #print('Operator')
        #print(version, count)
        # Operator
        packet, temp = pop(packet, 1)
        if temp == '0':
            # find length of subpackets
            packet, temp = pop(packet, 15)
            subpacket_length = int(temp,2)
            packet, temp = pop(packet, subpacket_length)
            # Parse subpackets
            #print('subpackets:', subpacket_length, 'bits:')
            temp = deque(temp)
            while temp:
                temp, count = parse_inner(temp, count)
        elif temp == '1':
            # find number of subpackets
            packet, temp = pop(packet, 11)
            subpackets = int(temp,2)
            #print(f'{subpackets} sub packets:')
            # Parse subpackets
            for i in range(subpackets):
                packet, count = parse_inner(packet, count)
    #print(packet)
    return count


def parse_inner(packet, count):
    
    current = list()
    # Version number
    packet, version = pop(packet, 3)
    current.append(version)
    version = int(version,2)
    count += version
        
    # Type ID
    packet, type_id = pop(packet, 3)
    current.append(type_id)
    type_id = int(type_id,2)
    
    if type_id == 4:
        # Literal
        #print('Literal')
        #print(version, count)
        literal = list()
        packet, temp = pop(packet, 1)
        current.append(temp)
        while temp == '1':
            packet, temp = pop(packet, 4)
            literal.append(temp)
            current.append(temp)
            packet, temp = pop(packet, 1)
            current.append(temp)
        # remaining bits
        packet, temp = pop(packet, 4)
        current.append(temp)
        literal.append(temp)
        literal = int(''.join(literal), 2)
        #print(''.join(current))
    else:
        #print('Operator')
        #print(version, count)
        # Operator
        packet, temp = pop(packet, 1)
        current.append(temp)
        if temp == '0':
            # find length of subpackets
            packet, temp = pop(packet, 15)
            current.append(temp)
            subpacket_length = int(temp,2)
            packet, temp = pop(packet, subpacket_length)
            current.append(temp)
            # Parse subpackets
            #print('subpackets:', subpacket_length, 'bits:')
            temp = deque(temp)
            while temp:
                temp, count = parse_inner(temp, count)
        elif temp == '1':
            # find number of subpackets
            packet, temp = pop(packet, 11)
            current.append(temp)
            subpackets = int(temp,2)
            #print(f'{subpackets} sub packets:')
            # Parse subpackets
            for i in range(subpackets):
                packet, count = parse_inner(packet, count)
    #print(''.join(current))
    return packet, count
                

def puzzle1(test = True):
    temp = ''.join(list(map(lambda x: convert[x], read_file(test))))
    temp = deque(temp)
    count = parse_outer(temp)
    print(count)

def parse_outer2(packet):
    
    # Version number
    packet, version = pop(packet, 3)
    version = int(version,2)
        
    # Type ID
    packet, type_id = pop(packet, 3)
    type_id = int(type_id,2)
    
    if type_id == 4:
        # Literal
        #print('Literal')
        #print(version, count)
        literal = list()
        packet, temp = pop(packet, 1)
        while temp == '1':
            packet, temp = pop(packet, 4)
            literal.append(temp)
            packet, temp = pop(packet, 1)
        # remaining bits
        packet, temp = pop(packet, 4)
        literal.append(temp)
        literal = int(''.join(literal), 2)
        return literal
    else:
        #print('Operator')
        #print(version, count)
        # Operator
        packet, temp = pop(packet, 1)
        if temp == '0':
            # find length of subpackets
            packet, temp = pop(packet, 15)
            subpacket_length = int(temp,2)
            packet, temp = pop(packet, subpacket_length)
            # Parse subpackets
            #print('subpackets:', subpacket_length, 'bits:')
            temp = deque(temp)
            values = list()
            while temp:
                temp, value = parse_inner2(temp)
                values.append(value)
        elif temp == '1':
            # find number of subpackets
            packet, temp = pop(packet, 11)
            subpackets = int(temp,2)
            #print(f'{subpackets} sub packets:')
            # Parse subpackets
            values = list()
            for i in range(subpackets):
                packet, value = parse_inner2(packet)
                values.append(value)
    #print(packet)
    if type_id == 0:
        # sum
        return reduce(lambda x,y: x+y, values)
    elif type_id == 1:
        # product
        return reduce(lambda x,y: x*y, values)
    elif type_id == 2:
        # minimum
        return min(values)
    elif type_id == 3:
        # maximum
        return max(values)
    elif type_id == 5:
        # greater than
        assert len(values) == 2
        if values[0] > values[1]:
            return 1
        else:
            return 0
    elif type_id == 6:
        # less than
        assert len(values) == 2
        if values[0] < values[1]:
            return 1
        else:
            return 0
    elif type_id == 7:
        # equal to
        assert len(values) == 2
        if values[0] == values[1]:
            return 1
        else:
            return 0


def parse_inner2(packet):
    
    # Version number
    packet, version = pop(packet, 3)
    version = int(version,2)
        
    # Type ID
    packet, type_id = pop(packet, 3)
    type_id = int(type_id,2)
    
    if type_id == 4:
        # Literal
        #print('Literal')
        #print(version, count)
        literal = list()
        packet, temp = pop(packet, 1)
        while temp == '1':
            packet, temp = pop(packet, 4)
            literal.append(temp)
            packet, temp = pop(packet, 1)
        # remaining bits
        packet, temp = pop(packet, 4)
        literal.append(temp)
        literal = int(''.join(literal), 2)
        return packet, literal
    else:
        #print('Operator')
        #print(version, count)
        # Operator
        packet, temp = pop(packet, 1)
        if temp == '0':
            # find length of subpackets
            packet, temp = pop(packet, 15)
            subpacket_length = int(temp,2)
            packet, temp = pop(packet, subpacket_length)
            # Parse subpackets
            #print('subpackets:', subpacket_length, 'bits:')
            temp = deque(temp)
            values = list()
            while temp:
                temp, value = parse_inner2(temp)
                values.append(value)
        elif temp == '1':
            # find number of subpackets
            packet, temp = pop(packet, 11)
            subpackets = int(temp,2)
            #print(f'{subpackets} sub packets:')
            # Parse subpackets
            values = list()
            for i in range(subpackets):
                packet, value = parse_inner2(packet)
                values.append(value)
    #print(packet)
    if type_id == 0:
        # sum
        return packet, reduce(lambda x,y: x+y, values)
    elif type_id == 1:
        # product
        return packet, reduce(lambda x,y: x*y, values)
    elif type_id == 2:
        # minimum
        return packet, min(values)
    elif type_id == 3:
        # maximum
        return packet, max(values)
    elif type_id == 5:
        # greater than
        assert len(values) == 2
        if values[0] > values[1]:
            return packet, 1
        else:
            return packet, 0
    elif type_id == 6:
        # less than
        assert len(values) == 2
        if values[0] < values[1]:
            return packet, 1
        else:
            return packet, 0
    elif type_id == 7:
        # equal to
        assert len(values) == 2
        if values[0] == values[1]:
            return packet, 1
        else:
            return packet, 0

def puzzle2(test = True):
    temp = ''.join(list(map(lambda x: convert[x], read_file(test))))
    temp = deque(temp)
    count = parse_outer2(temp)
    print(count)


puzzle1(False)
puzzle2(False)
