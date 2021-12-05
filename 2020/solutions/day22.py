from collections import deque

def read_file():
    deck1, deck2 = deque(), deque()
    player = 1
    with open('../input/day22_input.txt') as file:
        for line in file:
            if ":" in line:
                continue
            elif line.strip():
                if player == 1:
                    deck1.append(int(line.strip()))
                else:
                    deck2.append(int(line.strip()))
            else:
                player += 1
    return deck1, deck2

def score(deck):
    temp = 0
    for i, x in enumerate(reversed(deck), start = 1):
        temp += x*i
    return temp

def state(deck1, deck2):
    return ''.join(list(map(str,deck1))),''.join(list(map(str,deck2)))

def puzzle1():
    deck1, deck2 = read_file()
    while deck1 and deck2:
        card1, card2 = deck1.popleft(), deck2.popleft()
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    if deck1:
        print(score(deck1))
    elif deck2:
        print(score(deck2))

def play_game(deck1, deck2, verbose = False):
    temp1, temp2 = deck1.copy(), deck2.copy()
    states = set()
    while temp1 and temp2:
        states.add(state(temp1, temp2))
        if verbose:
            print("Player 1's deck:", temp1)
            print("Player 2's deck:", temp2)
        card1, card2 = temp1.popleft(), temp2.popleft()
        if verbose:
            print("Player 1 plays:", card1)
            print("Player 2 plays:", card2)
        if card1 <= len(temp1) and card2 <= len(temp2):
            if verbose: print("Playing sub-game to determine the winner...\n")
            winner, junk1, junk2 = play_game(deque(temp1[i] for i in range(card1)), deque(temp2[i] for i in range(card2)))
        elif card1 > card2:
            winner = 1
        else:
            winner = 2
        if verbose: print("Player "+str(winner)+" wins.\n")
        if winner == 1:
            temp1.append(card1)
            temp1.append(card2)
        elif winner == 2:
            temp2.append(card2)
            temp2.append(card1)
        if state(temp1, temp2) in states:
            if verbose: print("Previous state detected. Player 1 wins game.\n")
            return 1, temp1, temp2
    if temp1:
        if verbose: print("Player 1 wins round.\n")
        return 1, temp1, temp2
    else:
        if verbose: print("Player 2 wins round.\n")
        return 2, temp1, temp2

def puzzle2():
    states = set()
    deck1, deck2 = read_file()
    winner, temp1, temp2 = play_game(deck1, deck2)
    if winner == 1:
        print(score(temp1))
    else:
        print(score(temp2))



#puzzle1()
puzzle2()
