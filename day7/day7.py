import re

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
    contains = {}
    with open('testcase.txt') as file:
        for line in file:
            string = line.strip()
            color, contents = parse_rules(string)
            contains[color] = contents
    return contains, list(contains.keys())

def puzzle1():
    rules, bags = read_file()
    count = 0
    can_contain = {}
    for bag in bags:
        if b
    
puzzle1()