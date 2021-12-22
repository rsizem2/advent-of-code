from functools import lru_cache

def read_file(test = True):
    if test:
        filename = '../tests/day21.txt'
    else:
        filename = '../input/day21.txt'
    with open(filename) as file:
        for i, line in enumerate(file):
            if i == 0:
                player1 = int(line.strip().split(': ')[1])
            elif i == 1:
                player2 = int(line.strip().split(': ')[1])
    return player1, player2


def naive_puzzle1(test = True):
    player1, player2 = read_file(test)
    score1, score2 = 0,0
    rolls = 0
    dice = 1
    while True:
        for _ in range(3):
            player1 += dice
            dice += 1
            if dice > 100: 
                dice = 1
            player1 = ((player1 - 1) % 10) + 1
        rolls += 3
        score1 += player1
        #print(f'Player 1: {player1 + 1} with score {score1}')
        if score1 >= 1000: 
            print(rolls * score2)
            break
        for _ in range(3):
            player2 += dice
            dice += 1
            if dice > 100: dice = 1
            player2 = ((player2 - 1) % 10) + 1
        rolls += 3
        score2 += player2
        #print(f'Player 2: {player2 + 1} with score {score2}')
        if score2 >= 1000: 
            print(rolls * score1)
            break

def deterministic_play(player1, player2, score1 = 0, score2 = 0, roll = 0):
    if score2 >= 1000: 
        return roll*score1
    player1 = (player1 + 3*roll+1+2+3) % 10 
    if player1 == 0: 
        player1 = 10
    return deterministic_play(player2, player1, score2, score1+player1, roll+3)


def puzzle1(test = True):
    player1, player2 = read_file(test)
    print(deterministic_play(player1, player2, score1 = 0, score2 = 0, roll = 0))

@lru_cache(maxsize=None)
def quantum_play(player1, player2, score1 = 0, score2 = 0):
    if score2 >= 21: return 0, 1

    wins1, wins2 = 0, 0
    for move, n in (3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1):
        player1_ = (player1 + move) % 10 
        if player1_ == 0:
            player1_ = 10
        w2, w1 = quantum_play(player2, player1_, score2, score1 + player1_)
        wins1, wins2 = wins1 + n*w1, wins2 + n*w2
    return wins1, wins2


def puzzle2(test = True):
    player1, player2 = read_file(test)
    print(max(quantum_play(player1, player2)))

puzzle1()
puzzle2(False)