from collections import defaultdict

def read_file(test = True):
    if test:
        filename = '../tests/day7.txt'
    else:
        filename = '../input/day7.txt'
    with open(filename) as file:
        temp = dict()
        for line in file:
            line = line.strip().split()
            temp[line[-1]] = line[:-2]
    return temp

def evaluate(component, connections, values):
    try:
        # 'component' is a constant signal, no need to check inputs
        val = int(component)
        values[component] = val
        return
    except ValueError:
        pass
    command = connections[component]
    if len(command) == 1:
        try:
            # input is constant signal
            values[component] = int(command[0])
        except ValueError:
            # input is another wire
            evaluate(command[0], connections, values)
            values[component] = values[command[0]]
    elif len(command) == 2:
        # bitwise NOT of source
        operator, source = command
        if operator != "NOT":
            raise ValueError
        if source not in values:
            # source has no signal yet
            evaluate(source, connections, values)
        values[component] = ~ values[source]
    elif len(command) == 3:
        # binary operator on two sources
        source1, operator, source2 = command
        if source1 not in values:
            evaluate(source1, connections, values)
        if source2 not in values:
            evaluate(source2, connections, values)
        if operator == "AND":
            values[component] = values[source1] & values[source2]
        elif operator == "OR":
            values[component] = values[source1] | values[source2]
        elif operator == "RSHIFT":
            values[component] = values[source1] >> int(source2)
        elif operator == "LSHIFT":
            values[component] = values[source1] << int(source2)
        else:
            raise ValueError

def puzzle1(test = True):
    connections, values = read_file(test), dict()
    evaluate('a', connections, values)
    print(values['a'])


def puzzle2(test = True):
    connections, values = read_file(test), dict()
    evaluate('a', connections, values)
    
    # give output signal of wire a to wire b
    connections['b'] = [values['a']]
    
    # reset circuit
    values = dict()
    evaluate('a', connections, values)
    print(values['a'])

puzzle1(False)
puzzle2(False)