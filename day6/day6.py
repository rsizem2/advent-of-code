
def puzzle1():
    with open('input.txt') as file:
        groups = []
        current_group = set()
        for line in file:
            current = line.strip()
            if len(current) == 0:
                if len(current_group) > 0:
                    groups.append(current_group)
                current_group = set()
            else:
                current = set(current)
                #print(current)
                current_group = current_group.union(current)
        if len(current_group) > 0:
            groups.append(current_group)
    print(sum([len(x) for x in groups]))


def puzzle2():
    with open('input.txt') as file:
        groups = []
        current_group = []
        for line in file:
            current = line.strip()
            if len(current) == 0:
                groups.append(current_group)
                current_group = []
            else:
                current_group.append(set(current))
        if len(current_group) > 0:
            groups.append(current_group)
    print(sum([len(set.intersection(*x)) for x in groups]))

puzzle1()
puzzle2()