from functools import reduce

def read_file():
    temp = []
    with open('../input/day13_input.txt') as file:
        for line in file:
            temp.append(line.strip())
    return temp

def read_tests():
    temp = []
    with open('../input/day13_tests.txt') as file:
        for line in file:
            temp.append(line.strip().split(","))
    new = []
    for row in temp:
        new.append([(i, int(bus)) for i, bus in enumerate(row) if bus != "x"])
    return new
        

def chinese_remainder(n, a):
    # a - remainders, n - modulus (all pairwise coprime)
    temp = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        temp += a_i * inverse(p, n_i) * p
    return temp % prod

 
def inverse(a, b):
    # multiplicative inverse of a mod b
    mod = b
    x0, x1 = 0, 1
    if b == 1: 
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: 
        x1 += mod
    return x1
    
def puzzle1():
    temp = read_file()
    time = int(temp[0])
    bus_ids = set(temp[1].split(","))
    bus_ids.remove("x")
    bus_ids = sorted(map(int, bus_ids))
    waiting_times = sorted([(time + (x - time % x), x) if time % x else (time,x) for x in bus_ids])
    depart, bus = waiting_times[0]
    print((depart - time)*bus)
    
def puzzle2():
    temp = read_file()
    print(temp)
    temp = [(i, int(bus)) for i, bus in enumerate(temp[1].split(",")) if bus != "x"]
    rem = [-x[0] + x[1] for x in temp]
    mod = [x[1] for x in temp]
    print(chinese_remainder(mod, rem))
  
def test2():
    temp = read_tests()
    for line in temp:
        print(line)
        rem = [-x[0] + x[1] for x in line]
        mod = [x[1] for x in line]
        print(chinese_remainder(mod, rem))

puzzle1()
puzzle2()