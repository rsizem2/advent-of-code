from collections import defaultdict, Counter


def read_file():
    tiles = defaultdict(list)
    with open('../input/day20_test.txt') as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            elif line.startswith("Tile"):
                tile_id = int(line[5:-1])
            else:
                tiles[tile_id].append(line)
    return tiles

def generate_edges(tile):
    sides = [top_edge(tile), right_edge(tile), bottom_edge(tile), left_edge(tile)]
    temp = []
    for x in sides:
        temp.append(min(x,x[::-1]))
    return temp

def top_edge(tile):
    return ''.join(tile[0])

def right_edge(tile):
    return ''.join([x[-1] for x in tile])

def bottom_edge(tile):
    return ''.join(tile[-1])

def left_edge(tile):
    return ''.join([x[0] for x in tile])

def flip(tile):
    return [x[::-1] for x in tile]

def rotate(tile):
    return [''.join(x) for x in zip(*reversed(tile))]

def all_orientations(tile):
    for tile in all_rotations(tile):
        yield from all_sides(tile)

def all_rotations(tile):
    for rotation in range(4):
        yield tile
        tile = rotate(tile)

def all_sides(tile):
    for side in range(2):
        yield tile
        tile = flip(tile)

def print_tile(tile):
    for line in tile:
        print(*line)
    print()

def puzzle1():
    tiles = read_file()
    edge_count, poss_edges = Counter(), dict()
    corners, borders, middle = set(), set(), set()
    for tile_id, tile in tiles.items():
        poss_edges[tile_id] = generate_edges(tile)
        edge_count.update(poss_edges[tile_id])
    for tile_id in tiles.keys():
        if len([x for x in poss_edges[tile_id] if edge_count[x] == 1]) == 2:
            corners.add(tile_id)
        elif len([x for x in poss_edges[tile_id] if edge_count[x] == 1]) == 1:
            borders.add(tile_id)
        else:
            middle.add(tile_id)
    total = 1
    print("Corners:", corners)
    print("Borders:", borders)
    print("Middle:", middle)
    for key in corners:
        total *= key
    print(total)
    return tiles, poss_edges, corners, borders, middle, edge_count

def print_grid(grid, tiles, space = True):
    new_grid = []
    for row in grid:
        temp = [tiles[tile_num] for tile_num in row]
        if space:
            new_grid.extend([' '.join(x) for x in zip(*temp)])
            new_grid.append('')
        else:
            new_grid.extend([''.join(x) for x in zip(*temp)])
    #print(new_grid)
    return new_grid

def form_grid(grid, tiles):
    new = [[] for x in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            temp = tiles[grid[row][col]]
            temp = temp[1:-1]
            temp = [x[1:-1] for x in temp]
            new[row].append(temp)
    new_grid = []
    for row in new:
        new_grid.extend([''.join(x) for x in zip(*row)])
    return new_grid

def get_mask():
    offsets = []
    temp = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
    for i, row in enumerate(temp):
        for j, char in enumerate(row):
            if char == "#": 
                offsets.append((i,j))
    print(offsets)
    return i+1, j+1, offsets

def form_image():
    tiles, poss_edges, corners, borders, middle, edge_count = puzzle1()
    total = len(tiles.keys())
    size = 1
    while size*size < total:
        size += 1
    grid = [[] for x in range(size)]
    for row in range(size):
        for col in range(size):
            # top-left corner
            if (row,col) == (0,0):
                tile_num = corners.pop()
                found_orientation = False
                for tile in all_orientations(tiles[tile_num]):
                    left, top = left_edge(tile), top_edge(tile)
                    if edge_count[min(left, left[::-1])] == 1 and edge_count[min(top,top[::-1])] == 1:
                        found_orientation = True
                        break
                assert found_orientation
                tiles[tile_num] = tile
                grid[row].append(tile_num)
            # top row
            elif row == 0 and col != (size -1):
                match = right_edge(tiles[grid[row][col-1]])
                found_tile = False
                for tile_num in borders:
                    if min(match, match[::-1]) in poss_edges[tile_num]:
                        found_tile = True
                        break
                assert found_tile
                found_orientation = False
                for tile in all_orientations(tiles[tile_num]):
                    left, top = left_edge(tile), top_edge(tile)
                    if left == match and edge_count[min(top,top[::-1])] == 1:
                        found_orientation = True
                        break
                assert found_orientation
                borders.remove(tile_num)
                tiles[tile_num] = tile
                grid[row].append(tile_num)
            # top right corner
            elif row == 0 and col == (size - 1):
                match = right_edge(tiles[grid[row][col-1]])
                found_tile = False
                for tile_num in corners:
                    if min(match, match[::-1]) in poss_edges[tile_num]:
                        found_tile = True
                        break
                assert found_tile
                found_orientation = False
                for tile in all_orientations(tiles[tile_num]):
                    left, top, right = left_edge(tile), top_edge(tile), right_edge(tile)
                    if left  == match and edge_count[min(top,top[::-1])] == 1 and edge_count[min(right,right[::-1])] == 1:
                        found_orientation = True
                        break
                assert found_orientation
                corners.remove(tile_num)
                tiles[tile_num] = tile
                grid[row].append(tile_num)
            # left border
            elif col == 0 and row != (size - 1):
                match = bottom_edge(tiles[grid[row-1][col]])
                found_tile = False
                for tile_num in borders:
                    if min(match, match[::-1]) in poss_edges[tile_num]:
                        found_tile = True
                        break
                assert found_tile
                found_orientation = False
                for tile in all_orientations(tiles[tile_num]):
                    top, left = top_edge(tile), left_edge(tile)
                    if top == match and edge_count[min(left,left[::-1])] == 1:
                        found_orientation = True
                        break
                assert found_orientation
                borders.remove(tile_num)
                tiles[tile_num] = tile
                grid[row].append(tile_num)
            # middle tiles
            elif 0 < row < (size - 1) and 0 < col < (size -1):
                match = bottom_edge(tiles[grid[row-1][col]])
                match_2 = right_edge(tiles[grid[row][col-1]])
                found_tile = False
                for tile_num in middle:
                    if min(match,match[::-1]) in poss_edges[tile_num] and min(match_2,match_2[::-1]) in poss_edges[tile_num]:
                        found_tile = True
                        break
                assert found_tile
                found_orientation = False
                for tile in all_orientations(tiles[tile_num]):
                    if left_edge(tile) == match_2 and top_edge(tile) == match:
                        found_orientation = True
                        break
                assert found_orientation
                middle.remove(tile_num)
                tiles[tile_num] = tile
                grid[row].append(tile_num)
            # right border
            elif col == (size - 1) and 0 < row < (size - 1):
                match = bottom_edge(tiles[grid[row-1][col]])
                match_2 = right_edge(tiles[grid[row][col-1]])
                found_tile = False
                for tile_num in borders:
                    if min(match,match[::-1]) in poss_edges[tile_num] and min(match_2, match_2[::-1]) in poss_edges[tile_num]:
                        found_tile = True
                        break
                assert found_tile
                found_orientation = False
                for tile in all_orientations(tiles[tile_num]):
                    if left_edge(tile) == match_2 and top_edge(tile) == match:
                        found_orientation = True
                        break
                assert found_orientation
                borders.remove(tile_num)
                tiles[tile_num] = tile
                grid[row].append(tile_num)
            # bottom left corner
            elif row == (size - 1) and col == 0:
                match = bottom_edge(tiles[grid[row-1][col]])
                found_tile = False
                for tile_num in corners:
                    if min(match, match[::-1]) in poss_edges[tile_num]:
                        found_tile = True
                        break
                assert found_tile
                found_orientation = False
                for tile in all_orientations(tiles[tile_num]):
                    top, left = top_edge(tile), left_edge(tile)
                    if top == match and edge_count[min(left,left[::-1])] == 1:
                        found_orientation = True
                        break
                assert found_orientation
                corners.remove(tile_num)
                tiles[tile_num] = tile
                grid[row].append(tile_num)
            # bottom row
            elif row == (size - 1) and 0 < col < (size - 1):
                match = bottom_edge(tiles[grid[row-1][col]])
                match_2 = right_edge(tiles[grid[row][col-1]])
                found_tile = False
                for tile_num in borders:
                    if min(match,match[::-1]) in poss_edges[tile_num] and min(match_2,match_2[::-1]) in poss_edges[tile_num]:
                        found_tile = True
                        break
                assert found_tile
                found_orientation = False
                for tile in all_orientations(tiles[tile_num]):
                    if left_edge(tile) == match_2 and top_edge(tile) == match:
                        found_orientation = True
                        break
                assert found_orientation
                borders.remove(tile_num)
                tiles[tile_num] = tile
                grid[row].append(tile_num)
            # bottom right corner
            elif row == (size - 1) and col == (size - 1):
                match = bottom_edge(tiles[grid[row-1][col]])
                match_2 = right_edge(tiles[grid[row][col-1]])
                found_tile = False
                tile_num = corners.pop()
                found_orientation = False
                for tile in all_orientations(tiles[tile_num]):
                    if left_edge(tile) == match_2 and top_edge(tile) == match:
                        found_orientation = True
                        break
                assert found_orientation
                tiles[tile_num] = tile
                grid[row].append(tile_num)

    print_tile(print_grid(grid, tiles))
    return form_grid(grid, tiles)
    
def puzzle2():
    image = form_image()
    height, width, offsets = get_mask()
    test = [[' ']*width for x in range(height)]
    print(width, height)
    for i, j in offsets:
        test[i][j] = "#"
    test = [''.join(x) for x in test]
    print_tile(test)
    for tile in all_orientations(image):
        print_tile(tile)
        monsters = set()
        for i in range(len(image) - height):
            for j in range(len(image) - width):
                if all([tile[i+x][j+y] == "#" for x,y in offsets]):
                    monsters.add((i,j))
        if len(monsters): break 
    count = Counter()
    for row in tile:
        count.update(row)
    print(count)
    print(monsters)
    print(count['#'] - len(offsets)*len(monsters))

def test():
    temp = [['0','1','2'],['3','4','5'],['6','7','8']]
    #for tile in all_orientations(temp):
    #    print_tile(tile)
    print(*generate_edges(temp))
    print_tile(temp)
    print_tile(rotate(temp))

test()
puzzle2()
