
def read_file(test = True):
    if test:
        filename = '../tests/day8.txt'
    else:
        filename = '../input/day8.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            line = line.strip()
            temp.append(line)
    return temp

def puzzle1(test = True):
    temp = read_file(test)
    total = sum([len(line) for line in temp])
    for line in temp:
        copy = str(line[1:-1])
        while copy.find(r'\\') != -1:
            idx = copy.find(r'\\')
            copy = ''.join([copy[:idx],'a', copy[idx+2:]]) 
        while copy.find(r'\"') != -1:
            idx = copy.find(r'\"')
            copy = ''.join([copy[:idx],'a', copy[idx+2:]]) 
        while copy.find(r'\x') != -1:
            idx = copy.find(r'\x')
            try:
                int(copy[idx+2:idx+4], 16)
                copy = ''.join([copy[:idx],'a', copy[idx+4:]])
            except:
                copy = ''.join([copy[:idx],'aa', copy[idx+2:]]) 
        total -= len(copy)
    print(total)

def puzzle2(test = True):
    temp = read_file(test)
    total = sum([-len(line) for line in temp])
    for line in temp:
        copy = str(line[1:-1])
        while copy.find(r'\\') != -1:
            idx = copy.find(r'\\')
            copy = ''.join([copy[:idx],'$$', copy[idx+1:]]) 
        copy = copy.replace('"', '**')
        # repr and +4 accounts for the enclosing " and \" characters
        total += len(repr(copy)) + 4
        #print(repr(copy), len(repr(copy)) + 4)
    print(total)

puzzle1(False)
puzzle2(False)