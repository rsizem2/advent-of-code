from collections import defaultdict, deque

INPUT = [0,1,4,13,15,12,16]
TESTS = [[0,3,6],
         [1,3,2],
         [2,1,3],
         [1,2,3],
         [2,3,1],
         [3,2,1],
         [3,1,2]]

# slow, brute force-ish solution, takes a few minutes for second puzzle
def play_game(starting_numbers, end = 2020):
    temp = defaultdict(deque, maxlen=2)
    for i, x in enumerate(starting_numbers, start = 1):
        temp[x].append(i)
    prev = x
    for j in range(i+1, end+1):
        if len(temp[prev]) == 1:
            temp[0].append(j)
            prev = 0
        else:
            diff = temp[prev][-1] - temp[prev][-2]
            temp[diff].append(j)
            prev = diff
    print(prev)

def test(end = 2020):
    for test in TESTS:
        play_game(test, end)


play_game(INPUT, 30000000)
