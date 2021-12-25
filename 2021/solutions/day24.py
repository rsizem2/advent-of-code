# Went on reddit for this one, will look at solution later

def read_file():
    filename = '../input/day24.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            temp.append(line.strip())
    return temp


def run_program(program, num = None):
    values = dict()
    index = 0
    for line in program:
        #print(line)
        line = line.strip().split()
        if len(line) == 2:
            command, arg1 = line[0], line[1]
            assert command == 'inp'
            exec(f'{arg1} = {num[index]}')
            index += 1
        else:
            command, arg1, arg2 = line
            try:
                eval(arg1)
            except:
                exec(f'{arg1} = 0')
            try:
                eval(arg2)
            except:
                exec(f'{arg2} = 0')
            if command == 'add':
                exec(f'{arg1} += {arg2}')
            elif command == 'mul':
                exec(f'{arg1} *= {arg2}')
            elif command == 'div':
                exec(f'{arg1} //= {arg2}')
            elif command == 'mod':
                exec(f'{arg1} %= {arg2}')
            elif command == 'eql':
                exec(f'{arg1} = int({arg1} == {arg2})')
            exec(f'values[arg1] = {eval(arg1)}')
            #print(values)
    return values


def solve(lines, minimize = False):
    # Source: https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hpswoij/
    pairs = [(int(lines[i * 18 + 5][6:]), int(lines[i * 18 + 15][6:])) for i in range(14)]
    stack = []
    links = {}
    for i, (a, b) in enumerate(pairs):
        if a > 0:
            stack.append((i, b))
        else:
            j, bj = stack.pop()
            links[i] = (j, bj + a)
    
    assignments = {}
    for i, (j, delta) in links.items():
        assignments[i] = max(1, 1 + delta) if minimize else min(9, 9 + delta)
        assignments[j] = max(1, 1 - delta) if minimize else min(9, 9 - delta)
    print("".join(str(assignments[x]) for x in range(14)))

def puzzle1():
    lines = read_file()
    solve(lines)

def puzzle2():
    lines = read_file()
    solve(lines, True)



puzzle1()
puzzle2()