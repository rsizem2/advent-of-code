from itertools import product
from collections import namedtuple

Range = namedtuple("Range", ["min", "max"])

def read_file3d():
    temp = []
    with open('../input/day17_input.txt') as file:
        for line in file:
            temp.append(list(line.strip()))
            
    cubes = set()
    for y, row in enumerate(temp):
        for x, cube in enumerate(row):
            if cube == "#":
                cubes.add((x,y,0))
    x = Range(0,x)
    y = Range(0,y)
    z = Range(0,0)
    return cubes, (x,y,z)

def read_file4d():
    temp = []
    with open('../input/day17_input.txt') as file:
        for line in file:
            temp.append(list(line.strip()))
    
    cubes = set()
    for y, row in enumerate(temp):
        for x, cube in enumerate(row):
            if cube == "#":
                cubes.add((x,y,0,0))
    x = Range(0,x)
    y = Range(0,y)
    z = Range(0,0)
    w = Range(0,0)
    return cubes, (x,y,z,w)

def neighbors3d(x,y,z):
    return [(x+a,y+b,z+c) for (a,b,c) in product([-1,0,1], repeat = 3) if (a,b,c) != (0,0,0)]

def neighbors4d(x,y,z,w):
    return [(x+a,y+b,z+c,w+d) for (a,b,c,d) in product([-1,0,1], repeat = 4) if (a,b,c,d) != (0,0,0,0)]

def iterate3d(cubes, dims):
    new = set()
    old_x, old_y, old_z = dims
    new_x, new_y, new_z = None, None, None
    
    if old_x is None:
        return set(), (None, None, None)
    
    for x in range(old_x.min-1, old_x.max+2):
        for y in range(old_y.min-1, old_y.max+2):
            for z in range(old_z.min-1, old_z.max+2):
                nhbrs = neighbors3d(x,y,z)
                temp = [x for x in nhbrs if x in cubes]
                if (x,y,z) in cubes and len(temp) in [2,3]:
                    new.add((x,y,z))
                    if new_x is None:
                        new_x = Range(x,x)
                    elif new_x.min > x:
                        new_x = Range(x, new_x.max)
                    elif new_x.max < x:
                        new_x = Range(new_x.min, x) 
                    if new_y is None:
                        new_y = Range(y,y)
                    elif new_y.min > y:
                        new_y = Range(y, new_y.max)
                    elif new_y.max < y:
                        new_y = Range(new_y.min, y) 
                    if new_z is None:
                        new_z = Range(z,z)
                    elif new_z.min > z:
                        new_z = Range(z, new_z.max)
                    elif new_z.max < z:
                        new_z = Range(new_z.min, z) 
                elif (x,y,z) not in cubes and len(temp) == 3:
                    new.add((x,y,z))
                    if new_x is None:
                        new_x = Range(x,x)
                    elif new_x.min > x:
                        new_x = Range(x, new_x.max)
                    elif new_x.max < x:
                        new_x = Range(new_x.min, x) 
                    if new_y is None:
                        new_y = Range(y,y)
                    elif new_y.min > y:
                        new_y = Range(y, new_y.max)
                    elif new_y.max < y:
                        new_y = Range(new_y.min, y) 
                    if new_z is None:
                        new_z = Range(z,z)
                    elif new_z.min > z:
                        new_z = Range(z, new_z.max)
                    elif new_z.max < z:
                        new_z = Range(new_z.min, z)      
    return new, (new_x, new_y, new_z)

def iterate4d(cubes,dims):
    new = set()
    old_x, old_y, old_z, old_w = dims
    new_x, new_y, new_z, new_w = None, None, None, None
    
    if old_x is None:
        return set(), (None, None, None, None)
    
    for x in range(old_x.min-1, old_x.max+2):
        for y in range(old_y.min-1, old_y.max+2):
            for z in range(old_z.min-1, old_z.max+2):
                for w in range(old_w.min-1, old_w.max+2):
                    nhbrs = neighbors4d(x,y,z,w)
                    temp = [x for x in nhbrs if x in cubes]
                    if (x,y,z,w) in cubes and len(temp) in [2,3]:
                        new.add((x,y,z,w))
                        if new_x is None:
                            new_x = Range(x,x)
                        elif new_x.min > x:
                            new_x = Range(x, new_x.max)
                        elif new_x.max < x:
                            new_x = Range(new_x.min, x) 
                        if new_y is None:
                            new_y = Range(y,y)
                        elif new_y.min > y:
                            new_y = Range(y, new_y.max)
                        elif new_y.max < y:
                            new_y = Range(new_y.min, y) 
                        if new_z is None:
                            new_z = Range(z,z)
                        elif new_z.min > z:
                            new_z = Range(z, new_z.max)
                        elif new_z.max < z:
                            new_z = Range(new_z.min, z) 
                        if new_w is None:
                            new_w = Range(w,w)
                        elif new_w.min > w:
                            new_w = Range(w, new_w.max)
                        elif new_w.max < w:
                            new_w = Range(new_w.min, w) 
                    elif (x,y,z,w) not in cubes and len(temp) == 3:
                        new.add((x,y,z,w))
                        if new_x is None:
                            new_x = Range(x,x)
                        elif new_x.min > x:
                            new_x = Range(x, new_x.max)
                        elif new_x.max < x:
                            new_x = Range(new_x.min, x) 
                        if new_y is None:
                            new_y = Range(y,y)
                        elif new_y.min > y:
                            new_y = Range(y, new_y.max)
                        elif new_y.max < y:
                            new_y = Range(new_y.min, y) 
                        if new_z is None:
                            new_z = Range(z,z)
                        elif new_z.min > z:
                            new_z = Range(z, new_z.max)
                        elif new_z.max < z:
                            new_z = Range(new_z.min, z)    
                        if new_w is None:
                            new_w = Range(w,w)
                        elif new_w.min > w:
                            new_w = Range(w, new_w.max)
                        elif new_w.max < w:
                            new_w = Range(new_w.min, w) 
    return new, (new_x, new_y, new_z, new_w)



def puzzle1():
    cubes, dims = read_file3d()
    for i in range(6):
        cubes, dims = iterate3d(cubes, dims)
    print(len(cubes))

def puzzle2():
    cubes, dims = read_file4d()
    for i in range(6):
        cubes, dims = iterate4d(cubes, dims)
    print(len(cubes))

puzzle1()
puzzle2()