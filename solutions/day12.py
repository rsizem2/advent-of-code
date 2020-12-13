from collections import deque

def read_file():
    temp = []
    with open('../input/day12_input.txt') as file:
        for line in file:
            temp.append(line.strip())
    return temp

    
def puzzle1():
    temp = read_file()
    bearing = deque(list("ENWS"))
    position = [0,0]
    for line in temp:
        action, units = line[0], int(line[1:])
        if action == "N":
            position[1] += units
        elif action == "S":
            position[1] -= units
        elif action == "E":
            position[0] += units
        elif action == "W":
            position[0] -= units
        elif action == "L":
            assert units % 90 == 0
            for _ in range((units // 90) % 4):
                char = bearing.popleft()
                bearing.append(char)
        elif action == "R":
            assert units % 90 == 0
            for _ in range((units // 90) % 4):
                char = bearing.pop()
                bearing.appendleft(char)
        else:
            assert action == "F"
            if bearing[0] == "N":
                position[1] += units
            elif bearing[0] == "S":
                position[1] -= units
            elif bearing[0] == "E":
                position[0] += units
            elif bearing[0] == "W":
                position[0] -= units
    print(sum(list(map(abs,position))))
    
def puzzle2():
    temp = read_file()
    position = [0,0]
    waypoint = [10,1]
    for line in temp:
        action, units = line[0], int(line[1:])
        if action == "N":
            waypoint[1] += units
        elif action == "S":
            waypoint[1] -= units
        elif action == "E":
            waypoint[0] += units
        elif action == "W":
            waypoint[0] -= units
        elif action == "L":
            assert units % 90 == 0
            for _ in range((units // 90) % 4):
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        elif action == "R":
            assert units % 90 == 0
            for _ in range((units // 90) % 4):
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        else:
            assert action == "F"
            for _ in range(units):
                position[0] += waypoint[0]
                position[1] += waypoint[1]
    print(sum(list(map(abs,position))))
            
puzzle1()
puzzle2()