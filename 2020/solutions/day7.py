import re
from collections import deque, defaultdict, Counter

def parse_rules(string):
    first, temp = string.split(" bags contain ")
    temp = re.split(" bag[s]?[,.]?[ ]?", temp)[:-1]
    contents = []
    for bags in temp:
        bags = bags.split()
        if len(bags) == 2:
            return first, contents
        number, adjective, color = bags
        number = int(number)
        for _ in range(number):
            contents.append(" ".join([adjective, color]))
    return first, contents

def read_file():
    temp = {}
    with open('../input/day7_input.txt') as file:
        for line in file:
            string = line.strip()
            color, contents = parse_rules(string)
            temp[color] = contents
    return  temp, list(temp.keys())

def puzzle1():
    contains, bags = read_file()
    contained_in = defaultdict(set)
    for container, contents in contains.items():
        for color in contents:
            contained_in[color].add(container)
    found = set()
    queue = deque(["shiny gold"])
    while queue:
        current = queue.popleft()
        for color in contained_in[current]:
            if color not in found:
                queue.append(color)
                found.add(color)
    print(len(found))

def puzzle2():
    contains, bags = read_file()
    contents = {key: Counter(value) for key, value in contains.items()}
    def count(item, d):
        temp = 0
        print(item)
        for bag, cnt in d[item].items():
            temp += cnt + cnt*count(bag, d)
        return temp
    print(count('shiny gold', contents))
        
puzzle1()    
puzzle2()
