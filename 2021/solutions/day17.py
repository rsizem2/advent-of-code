# disgusting brute force solution ;/
import numpy as np

def read_file(test = True):
    if test:
        filename = '../tests/day17.txt'
    else:
        filename = '../input/day17.txt'
    with open(filename) as file:
        for line in file:
            pass
        temp = line.split(':')[1].strip()
        temp = list(map(lambda x: x[2:], temp.split(', ')))
        x = tuple(map(int, temp[0].split('..')))
        y = tuple(map(int, temp[1].split('..')))
    return x,y
            
    


def puzzle1(test = True):
    width, height = read_file(test)
    max_steps = max(map(abs, [*width, *height]))
    max_steps *= 2
    x_range = set()
    for x_init in range(max_steps):
        x = 0
        x_vel = x_init
        if width[0] <= x <= width[1]:
            x_range.add(x_init)
        for step in range(max_steps):
            x += x_vel 
            if x_vel < 0:
                x_vel += 1
            elif x_vel > 0:
                x_vel -= 1
            if width[0] <= x <= width[1]:
                x_range.add(x_init)
    y_range = set()
    for y_init in range(max_steps):
        y = 0
        y_vel = y_init
        if height[0] <= y <= height[1]:
            y_range.add(y_init)
        for step in range(max_steps):
            y += y_vel 
            y_vel -= 1
            if height[0] <= y <= height[1]:
                y_range.add(y_init)
    
    y_val = -np.Inf
    for y_init in y_range:
        for x_init in x_range:
            y_positions = set()
            x,y = 0,0
            x_vel,y_vel = x_init, y_init
            valid = False
            for step in range(max_steps):
                x += x_vel
                y += y_vel
                y_positions.add(y)
                y_vel -= 1
                if x_vel < 0:
                    x_vel += 1
                elif x_vel > 0:
                    x_vel -= 1
                if height[0] <= y <= height[1] and width[0] <= x <= width[1]:
                    valid = True
            if valid:
                temp = max(y_positions)
                if temp > y_val:
                    y_val = temp
    print(y_val)
                
                

def puzzle2(test = True):
    width, height = read_file(test)
    max_steps = max(map(abs, [*width, *height]))
    max_steps *= 4
    x_range = set()
    for x_init in range(max_steps):
        x = 0
        x_vel = x_init
        if width[0] <= x <= width[1]:
            x_range.add(x_init)
        for step in range(max_steps):
            x += x_vel 
            if x_vel < 0:
                x_vel += 1
            elif x_vel > 0:
                x_vel -= 1
            if width[0] <= x <= width[1]:
                x_range.add(x_init)
    y_range = set()
    for y_init in range(max_steps):
        y = 0
        y_vel = y_init
        if height[0] <= y <= height[1]:
            y_range.add(y_init)
        for step in range(max_steps):
            y += y_vel 
            y_vel -= 1
            if height[0] <= y <= height[1]:
                y_range.add(y_init)
    
    x_max =  max(map(abs, [*width]))
    y_min =  min([*height])
    velocities = 0
    count = 0
    for y_init in range(-max_steps,max_steps):
        for x_init in range(-max_steps,max_steps):
            if count % 100000 == 0:
                print(f'count {count} of {4*max_steps**2}')
            y_positions = set()
            x,y = 0,0
            x_vel,y_vel = x_init, y_init
            valid = False
            for step in range(max_steps):
                x += x_vel
                y += y_vel
                y_positions.add(y)
                y_vel -= 1
                if x_vel < 0:
                    x_vel += 1
                elif x_vel > 0:
                    x_vel -= 1
                if height[0] <= y <= height[1] and width[0] <= x <= width[1]:
                    valid = True
                if x > x_max or y < y_min: break
            if valid:
                velocities += 1
            count += 1
    print(velocities)


puzzle1()
puzzle2(False)
