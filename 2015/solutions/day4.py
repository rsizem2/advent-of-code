from hashlib import md5

def read_file(test = True):
    if test:
        seeds = ['abcdef', 'pqrstuv']
    else:
        seeds = ['ckczppom']
    return seeds

def puzzle1(test = True):
    seeds = read_file(test)
    for seed in seeds:
        num = 0
        while True:
            string = seed + str(num)
            if md5(string.encode('utf-8')).hexdigest()[:5] == '00000':
                break
            num += 1
        print(seed, num)
        
    
def puzzle2(test = True):
    seeds = read_file(test)
    for seed in seeds:
        num = 0
        while True:
            string = seed + str(num)
            if md5(string.encode('utf-8')).hexdigest()[:6] == '000000':
                break
            num += 1
        print(seed, num)
        
puzzle1(False)
puzzle2(False)