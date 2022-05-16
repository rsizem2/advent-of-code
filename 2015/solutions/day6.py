
def read_file(test = True):
    if test:
        filename = '../tests/day6.txt'
    else:
        filename = '../input/day6.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            
            line = line.strip()
            
            if line.startswith('turn on '):
                command = 'turn on'
            elif line.startswith('turn off '):
                command = 'turn off'
            elif line.startswith('toggle '):
                command = 'toggle'
            else:
                raise ValueError
            
            line = line[len(command):].split(' through ')
            line = [command] + [tuple(map(int, x.split(','))) for x in line]
            temp.append(line)
    return temp

def puzzle1():
    temp = read_file(False)
    lights = [[0]*1000 for i in range(1000)]
    for cycle in temp:
        command, (top_x, top_y), (bottom_x, bottom_y) = cycle
        for x in range(top_x, bottom_x + 1):
            for y in range(top_y, bottom_y + 1):
                if command == 'turn on':
                    lights[x][y] = 1
                elif command == 'turn off':
                    lights[x][y] = 0
                elif command == 'toggle':
                    lights[x][y] += 1
                    lights[x][y] %= 2
                else:
                    raise ValueError
    print(sum([sum(x) for x in lights]))

def puzzle2():
    temp = read_file(False)
    lights = [[0]*1000 for i in range(1000)]
    for cycle in temp:
        command, (top_x, top_y), (bottom_x, bottom_y) = cycle
        for x in range(top_x, bottom_x + 1):
            for y in range(top_y, bottom_y + 1):
                if command == 'turn on':
                    lights[x][y] += 1
                elif command == 'turn off':
                    lights[x][y] -= 1
                    lights[x][y] = max(lights[x][y], 0)
                elif command == 'toggle':
                    lights[x][y] += 2
                else:
                    raise ValueError
    print(sum([sum(x) for x in lights]))
    
puzzle1()
puzzle2()