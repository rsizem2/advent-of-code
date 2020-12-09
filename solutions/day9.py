from itertools import combinations

def read_file(path = "../input/day9_input.txt"):
    with open(path) as file:
        temp = [int(line.strip()) for line in file]
    return temp


def test1():
    numbers = read_file("../input/day9_test.txt")
    preamble = 5
    for i, number in enumerate(numbers[preamble:], start = preamble):
        print("Checking", number)
        found = False
        for j, k in combinations(range(i-preamble,i),2):            
            if numbers[j] + numbers[k] == number: 
                found = True
                break
        if not found:
            print(number)
            return True
    return False         
    
    
def puzzle1():
    numbers = read_file()
    preamble = 25
    for i, number in enumerate(numbers[preamble:], start = preamble):
        print("Checking", number)
        found = False
        for j, k in combinations(range(i-preamble,i),2):            
            if numbers[j] + numbers[k] == number: 
                found = True
                break
        if not found:
            print(number)
            return True
    return False         
    
def test2():
    numbers = read_file("../input/day9_test.txt")
    start = 0
    end = 1
    ans = 127
    temp = sum(numbers[start:end])
    try: 
        while(temp != ans):
            if temp > ans:
                start += 1
            else:
                end += 1
            temp = sum(numbers[start:end])
    except:
        print("No such range found.")
    small = min(numbers[start:end])
    large = max(numbers[start:end])
    print(small + large)


def puzzle2():
    numbers = read_file()
    start = 0
    end = 1
    ans = 1398413738
    temp = sum(numbers[start:end])
    try: 
        while(temp != ans):
            if temp > ans:
                start += 1
            else:
                end += 1
            temp = sum(numbers[start:end])
    except:
        print("No such range found.")
    small = min(numbers[start:end])
    large = max(numbers[start:end])
    print(small + large)

puzzle2()

    