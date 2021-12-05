
def read_file():
    with open('../input/day3_input.txt') as file:
        temp = [line.strip() for line in file]
    return temp

def puzzle1():
    tree_map = read_file()
    n = len(tree_map[0])
    assert all(len(x) == n for x in tree_map)
    index, trees = 0, 0
    for line in tree_map:
        if line[index] == '#':
            trees += 1
        index += 3
        index %= n
    print(trees)
        
def check_trees(tree_map, right, down = 1):
    n = len(tree_map[0])
    assert all(len(x) == n for x in tree_map)
    index, trees = 0, 0
    for i, line in enumerate(tree_map):
        if (i % down) != 0:
            continue
        if line[index] == '#':
            trees += 1
        index += right
        index %= n
    return trees
    
def puzzle2():
    x = read_file()
    ans = [check_trees(x,1,1), check_trees(x,3,1), check_trees(x,5,1), check_trees(x,7,1), check_trees(x,1,2)]
    val = 1
    for x in ans:
        val *= x
    print('Total:', val)

puzzle1()
puzzle2()