from collections import defaultdict

def read_file():
    count = 0
    rules = dict()
    temp = list()
    yours = list()
    other = list()
    with open('../input/day16_input.txt') as file:
        for line in file:
            if len(line.strip()) == 0:
                count += 1
            elif count == 0:
                temp.append(line.strip())
            elif count == 1 and not line.startswith("your"):
                yours = list(map(int, line.strip().split(",")))
            elif count == 2 and not line.startswith("nearby"):
                other.append(list(map(int, line.strip().split(","))))
    for rule in temp:
        name, numbers = rule.split(": ")
        first, second = numbers.split(" or ")
        rules[name] = tuple(map(int, first.split("-"))), tuple(map(int, second.split("-")))
    return rules, yours, other

def puzzle1():
    rules, mine, others = read_file()
    invalid = list()
    valid_tickets = list()
    for ticket in others:
        good = True
        for value in ticket:
            valid = False
            for name, (range1, range2) in rules.items():
                if range1[0] <= value <= range1[1] or range2[0] <= value <= range2[1]:
                    valid = True
                    break
            if not valid:
                invalid.append(value)
                good = False
        if good:
            valid_tickets.append(ticket)
    print("Puzzle 1:", sum(invalid))
    return rules, mine, valid_tickets

def puzzle2():
    rules, mine, tickets = puzzle1()
    temp = defaultdict(set)
    for i in range(len(mine)):
        for name, (range1, range2) in rules.items():
            if all(range1[0] <= x[i] <= range1[1] or range2[0] <= x[i] <= range2[1] for x in tickets):
                temp[name].add(i)
                
    verified = dict()
    while temp:
        key = min(temp.keys(), key = lambda x: len(temp[x]))
        assert(len(temp[key]) == 1)
        index = temp.pop(key).pop()
        verified[key] = index
        for key in temp:
            temp[key].remove(index)
    total = 1
    print(mine)
    for key, value in verified.items():
        if key.startswith("departure"):
            total *= mine[value]
    print(total)
        
        
puzzle1()
puzzle2()