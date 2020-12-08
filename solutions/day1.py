

def read_file():
    with open('../input/day1_input.txt') as file:
        temp = [int(line.strip()) for line in file]
    return temp
            
def puzzle1():
    numbers = read_file()
    for i, x in enumerate(numbers):
        for y in numbers[i:]:
            if x + y == 2020:
                print('Solution 1:', x*y)
                return
    print('No Solution Found!')

def puzzle2():
    numbers = read_file()
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers[i:]):
            if i + j >= 2020: 
                continue
            for z in numbers[j:]:
                if x + y + z == 2020:
                    print('Solution 2:', x*y*z)
                    return
    print('No Solution Found!')

puzzle1()
puzzle2()
