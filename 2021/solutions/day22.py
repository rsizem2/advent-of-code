from collections import deque

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

def puzzle1(test = True):
    # calculate all unit cubes explicitly
    temp = read_file(test)
    cubes = set()
    for state, coords in temp:
        x,y,z = coords
        x1, x2 = x
        y1, y2 = y
        z1, z2 = z
        for x in range(max(-50,x1), min(51,x2+1)):
            for y in range(max(-50,y1), min(51,y2+1)):
                for z in range(max(-50,z1), min(51,z2+1)):
                    if state == 'on':
                        cubes.add((x,y,z))
                    elif state == 'off':
                        cubes.discard((x,y,z))
                    else:
                        assert False
    print(len(cubes))


# helper for part2
def intersect_pair(pair1, pair2):
    assert pair1[0] <= pair1[1] and pair2[0] <= pair2[1]
    if pair2[0] > pair1[1] or pair1[0] > pair2[1]:
        return None
    nums = sorted([pair1[0], pair1[1], pair2[0], pair2[1]])
    return [nums[1], nums[2]]

# helper for part2
def intersect_cubes(cube1, cube2):
    x1,y1,z1 = cube1
    x2,y2,z2 = cube2
    x = intersect_pair(x1, x2)
    y = intersect_pair(y1, y2)
    z = intersect_pair(z1, z2)
    if not all([x, y, z]):
        return None
    return x, y, z

# data structure for cube and it's empty spaces contained within
class Cuboid:
    def __init__(self, coords) -> None:
        self.coords = coords
        self.vacuums = []
    def remove(self, coords):
        shaved_coords = intersect_cubes(self.coords, coords)
        if not shaved_coords:
            return
        for vacuum in self.vacuums:
            vacuum.remove(shaved_coords)
        self.vacuums.append(Cuboid(shaved_coords))
    def volume(self):
        x,y,z = self.coords
        return (x[1]-x[0]+1)*(y[1]-y[0]+1)*(z[1]-z[0]+1)-sum(vacuum.volume() for vacuum in self.vacuums)

def puzzle2(test = True):
    temp = read_file(test)
    cuboids = []
    for state, coords in temp:
        for cuboid in cuboids:
            cuboid.remove(coords)
        if state == 'on':
            cuboids.append(Cuboid(coords))

    print(sum(cuboid.volume() for cuboid in cuboids))

puzzle1()
puzzle2(False)