
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

def area(cube):
    x,y,z = cube
    return (x[1]-x[0])*(y[1]-y[0])*(z[1]-z[0])

def intersect(cube1, cube2):
    cubes = set()
    x1,y1,z1 = cube1 
    x2,y2,z2 = cube2 
    
    if x1[0] > x2[1] or x1[1] < x2[0]:
        return cubes
    elif y1[0] > y2[1] or y1[1] < y2[0]:
        return cubes
    elif z1[0] > z2[1] or z1[1] < z2[0]:
        return cubes
    
    x_vals = sorted({*x1, *x2})
    y_vals = sorted({*x1, *x2})
    z_vals = sorted({*x1, *x2})
    x_min, y_min, z_min = None, None, None
    
    # cube 1
    x1_min, x1_max = x1
    y1_min, y1_max = y1
    z1_min, z1_max = z1
    for x_max in x_vals:
        if x_min is None or x_min < x1_min:
            x_min = x_max
            continue
        elif x_max > x_max: 
            break
        assert x_min < x_max
        for y_max in y_vals:
            if y_min is None or y_min < y1_min:
                y_min = y_max
                continue
            elif y_max > y1_max:
                break
            assert y_min < y_max
            for z_max in z_vals:
                if z_min is None or z_min < z1_min:
                    z_min = z_max
                    continue
                elif z_max > z1_max:
                    break
                assert z_min < z_max, f'{z_min} not less than {z_max}'
                z_min = z_max
            y_min = y_max
            z_min = None
        x_min = x_max
        y_min = None

    # cube 2
    x2_min, x2_max = x2
    y2_min, y2_max = y2
    z2_min, z2_max = z2
    for x_max in x_vals:
        if x_min is None or x_min < x1_min:
            x_min = x_max
            continue
        elif x_max > x_max: 
            break
        assert x_min < x_max
        for y_max in y_vals:
            if y_min is None or y_min < y1_min:
                y_min = y_max
                continue
            elif y_max > y1_max:
                break
            assert y_min < y_max
            for z_max in z_vals:
                if z_min is None or z_min < z1_min:
                    z_min = z_max
                    continue
                elif z_max > z1_max:
                    break
                cubes.add(
                    ((x_min,x_max),(y_min,y_max),(z_min,z_max))
                    )
                assert z_min < z_max, f'{z_min} not less than {z_max}'
                z_min = z_max
            y_min = y_max
            z_min = None
        x_min = x_max
        y_min = None
    return cubes

def subtract(cube1, cube2):
    pass

def truncate(cube):
    x,y,z = cube
    if x[0] > 50 or x[1] < -50:
        return tuple()
    elif y[0] > 50 or y[1] < -50:
        return tuple()
    elif z[0] > 50 or z[1] < -50:
        return tuple()
    x_min, x_max = x
    x_min = max(x_min, -50)
    x_max = min(x_max, 50)
    y_min, y_max = y
    y_min = max(y_min, -50)
    y_max = min(y_max, 50)
    z_min, z_max = z 
    z_min = max(z_min, -50)
    z_max = min(z_max, 50)
    return (x_min, x_max), (y_min, y_max), (z_min, z_max)
    

def puzzle1(test = True):
    temp = read_file(test)
    for i, (state, coords) in enumerate(temp):
        temp[i] = (state, truncate(coords))
    disjoint = set()
    for state, cube in temp:
        new = set()
        for coords in disjoint:
            if state == 'on':
                new.update(intersect(coords, cube))
            elif state == 'off':
                new.update(subtract(coords, cube))
            else:
                assert False
    total = 0
    for cube in disjoint:
        total += area(cube)
    print(total)
                    

def puzzle2(test = True):
    temp = read_file(test)

                    


puzzle1()
puzzle2()