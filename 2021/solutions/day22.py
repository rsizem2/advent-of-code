
def read_file(test = True):
    if test:
        filename = '../tests/day22.txt'
    else:
        filename = '../input/day22.txt'
    with open(filename) as file:
        temp = list()
        for line in file:
            state, coords = line.strip().split(' ')
            x,y,z = coords.split(',')
            x = tuple(map(int, x[2:].split('..')))
            y = tuple(map(int, y[2:].split('..')))
            z = tuple(map(int, z[2:].split('..')))
            temp.append((state, (x,y,z)))
    return temp

def discretize(cube1, cube2):
    assert overlap(cube1, cube2)
    pass

def area(cube):
    x,y,z = cube
    return (x[1]-x[0])*(y[1]-y[0])*(z[1]-z[0])

def overlap(cube1, cube2):
    x1,y1,z1 = cube1 
    x2,y2,z2 = cube2 
    if x1[0] > x2[1] or x1[1] < x2[0]: 
        return False
    elif y1[0] > y2[1] or y1[1] < y2[0]:
        return False
    elif z1[0] > z2[1] or z1[1] < z2[0]:
        return False
    return True
    
def truncate(cube):
    x,y,z = cube
    
    if not overlap(cube, ((-50,50),(-50,50),(-50,50))):
        return None
    
    # truncate
    x_min, x_max = max(x[0], -50), min(x[1], 50)
    y_min, y_max = max(y[0], -50), min(y[1], 50)
    z_min, z_max = max(z[0], -50), min(z[1], 50)
    return (x_min, x_max), (y_min, y_max), (z_min, z_max)

def subtract(cube1, cube2):
    pass

    

def puzzle1(test = True):
    temp = read_file(test)
    total = 0
    for i, (state, coords) in enumerate(temp):
        print(coords)
        print(truncate(coords))
        temp[i] = (state, truncate(coords))
        total += area(coords)
    print(total)
                    

def puzzle2(test = True):
    temp = read_file(test)
        


puzzle1()
puzzle2()