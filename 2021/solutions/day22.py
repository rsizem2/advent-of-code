
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

def area_truncate(cube):
    x,y,z = cube
    if x[0] > 50 or x[1] < -50:
        return 0
    elif y[0] > 50 or y[1] < -50:
        return 0
    elif z[0] > 50 or z[1] < -50:
        return 0
    x_min, x_max = x
    x_min = max(x_min, -50)
    x_max = min(x_max, 50)
    y_min, y_max = y
    y_min = max(y_min, -50)
    y_max = min(y_max, 50)
    z_min, z_max = z 
    z_min = max(z_min, -50)
    z_max = min(z_max, 50)
    return (x_max - x_min) * (y_max - y_min) * (z_max - z_min)
    

def puzzle1(test = True):
    temp = read_file(test)
    x_values, y_values, z_values = set(), set(), set()
    for state, coords in temp:
        x,y,z = coords
        x_values.update({*x})
        y_values.update({*y})
        z_values.update({*z})
    x_values = {x for x in x_values if -50 <= x <= 50}
    y_values = {x for x in y_values if -50 <= x <= 50}
    z_values = {x for x in z_values if -50 <= x <= 50}
    x_values = sorted(x_values)
    y_values = sorted(y_values)
    z_values = sorted(z_values)
    disjoint_on = set()
    for state, coords in temp:
        x,y,z = coords
        x_vals = sorted([i for i in x_values if x[0] <= i <= x[1]])
        y_vals = sorted([i for i in y_values if y[0] <= i <= y[1]])
        z_vals = sorted([i for i in z_values if z[0] <= i <= z[1]])
        x_min, y_min, z_min = None, None, None
        for x_max in x_vals:
            if x_min is None:
                x_min = x_max
                continue
            assert x_min < x_max
            for y_max in y_vals:
                if y_min is None:
                    y_min = y_max
                    continue
                assert y_min < y_max
                for z_max in z_vals:
                    if z_min is None:
                        z_min = z_max
                        continue
                    assert z_min < z_max, f'{z_min} not less than {z_max}'
                    if state == 'off':
                        try:
                            disjoint_on.remove(
                                ((x_min,x_max),(y_min,y_max),(z_min,z_max))
                                )
                        except:
                            pass
                    elif state == 'on':
                        disjoint_on.add(
                            ((x_min,x_max),(y_min,y_max),(z_min,z_max))
                            )
                    else:
                        assert False
                    z_min = z_max
                y_min = y_max
                z_min = None
            x_min = x_max
            y_min = None
    total = 0
    for cube in disjoint_on:
        total += area(cube)
    print(total)
                    

def puzzle2(test = True):
    temp = read_file(test)

                    


puzzle1()
puzzle2()