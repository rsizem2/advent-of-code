from collections import deque

cups = "247819356"
test = "389125467"

def do_moves_list(cups, num_moves, verbose = False):
    num_cups = len(cups)
    deck = list(map(int, list(cups)))
    deck = [x-1 for x in deck]
    current = 0
    for move in range(1,num_moves+1):
        temp = deck.copy()
        pickup = [(current + i) % num_cups for i in [1,2,3]]
        dest = (deck[current] - 1) % num_cups
        while dest in [deck[i] for i in pickup]:
            dest = (dest - 1) % num_cups
        if verbose:
            print("\n--move " + str(move)+" --")
            print("cups:", [x+1 for x in temp])
            print("pickup:", [temp[i]+1 for i in pickup])
            print("destination:", dest+1)
        dest = temp.index(dest)
        deck = [temp[i] for i in range(dest) if i not in pickup]
        deck.append(temp[dest])
        deck.extend([temp[i] for i in pickup])
        deck.extend([temp[i] for i in range(dest+1,num_cups) if i not in pickup])
        offset = deck.index(temp[current]) - current
        deck = deck[offset:] + deck[:offset]
        current = (current + 1) % num_cups
    deck = [x+1 for x in deck]
    index = deck.index(1)
    print("\n--final--")
    print("cups:", deck)
    print("string:", ''.join(map(str, deck[index+1:]+deck[:index])), "\n")
    
def initiate_linkedlist(cups, num_cups):
    temp = [(x+1) % num_cups for x in range(num_cups)]
    if num_cups == len(cups):
        print("No extra cups.")
        final = int(cups[0]) - 1
    else:
        final = len(cups)
    cups = deque(map(lambda x: int(x)-1, list(cups)))
    print(list(x+1 for x in cups))
    old = -1
    while cups:
        current = cups.popleft()
        temp[old] = current
        old = current
    print(old, "->" , final)
    temp[old] = final
    return temp
    
    
def do_moves_linked(cups, num_moves, num_cups, verbose = False):
    temp = initiate_linkedlist(cups, num_cups)
    print(len(temp))
    current = temp[-1]
    for move in range(1, num_moves+1):
        try:
            pickup = [temp[current]]
        except:
            print(current)
            return
        for _ in range(2):
            pickup.append(temp[pickup[-1]])
        final = temp[pickup[-1]]
        dest = next((current - i) % num_cups for i in range(1,5) if ((current - i) % num_cups) not in pickup)
        if verbose:
            print("\n--move " + str(move)+" --")
            print("array:", list(range(len(temp))))
            print("array:", temp)
            print("current:", (current + 1) % num_cups)
            print("pickup:", [i+1 for i in pickup])
            print("destination:", (dest % num_cups) + 1)
        end = temp[dest]
        temp[dest] = pickup[0]
        temp[pickup[-1]] = end
        temp[current] = final
        current = final
    if verbose:
        print("\n--final--")
        print("cups:", cups)
        print("string:", ''.join(map(str, temp)), "\n")
    return temp
        
def print_ans(temp):
    first = temp[0]
    second = temp[temp[0]]
    print(first)
    print(second)
    print((first+1)*(second+1))
    
def puzzle1():
    do_moves_list(cups, 100)

def puzzle2():
    #do_moves_linked(test, 10, len(test), True)
    temp = do_moves_linked(test, 10000000, 1000000)
    print_ans(temp)
    temp = do_moves_linked(cups, 10000000, 1000000)
    print_ans(temp)


#puzzle1()
puzzle2()