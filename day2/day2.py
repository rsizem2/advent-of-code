
def puzzle1():
    valid = 0
    with open('day2.txt') as file:
        for line in file:
            x, letter, pw = line.split()
            min_val, max_val = map(int,x.split('-'))
            letter = letter[:-1]
            if min_val <= len([x for x in pw if x == letter]) <= max_val:
                valid += 1
    print('Solution 1:', valid)
                

def puzzle2():
    valid = 0
    with open('day2.txt') as file:
        for line in file:
            x, letter, pw = line.split()
            pos1, pos2 = map(int,x.split('-'))
            letter = letter[:-1]
            if (pw[pos1-1] == letter or pw[pos2-1] == letter):
                if not (pw[pos1-1] == letter and pw[pos2-1] == letter):
                    valid += 1
    print('Solution 2:', valid)

puzzle1()
puzzle2()