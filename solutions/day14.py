from itertools import product 

def read_file():
    temp = []
    with open('../input/day14_input.txt') as file:
        for line in file:
            temp.append(line.strip())
    return temp

def apply_mask(number, mask):
    number  = list(bin(number)[2:].rjust(36,'0'))
    mask = [(i,x) for i,x in enumerate(mask) if x != "X"]
    for i,x in mask:
        number[i] = x
    return int("".join(number), 2)

def mask_address(address, mask):
    address = list(bin(address)[2:].rjust(36,'0'))
    ones = [i for i,x in enumerate(mask) if x == "1"]
    floats = [i for i,x in enumerate(mask) if x == "X"]
    for i in ones:
        address[i] = "1"
    addresses = list()
    for number in product("01",repeat = len(floats)):
        temp = list(address)
        for i,bit in enumerate(number):
            j = floats[i]
            temp[j] = bit
        addresses.append(int("".join(temp),2))
    return addresses

def puzzle1():
    temp = read_file()
    current_mask = "".rjust(36,"X")
    memory = dict()
    for line in temp:
        if line[:4] == "mask":
            current_mask = line[-36:]
        else:
            address, number = line[3:].split(" = ")
            address = int(address[1:-1])
            number = int(number)
            memory[address] = apply_mask(number,current_mask)
    print(sum([x for i,x in memory.items()]))
    
def puzzle2():
    temp = read_file()
    memory = dict()
    for line in temp:
        if line[:4] == "mask":
            current_mask = line[-36:]
        else:
            address, number = line[3:].split(" = ")
            address = int(address[1:-1])
            number = int(number)
            addresses = mask_address(address, current_mask)
            for new_address in addresses:
                memory[new_address] = number
    print(sum([x for i,x in memory.items()]))

puzzle1()
puzzle2()