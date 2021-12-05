from collections import defaultdict


def read_file():
    rules = defaultdict(list)
    messages = list()
    with open('../input/day19_input.txt') as file:
        for line in file:
            if ":" in line:
                number, rule = line.strip().split(":")
                if '"' in line:
                    rules[int(number)] = rule.strip().strip('"')
                else:
                    rule = rule.strip().split("|")
                    for nums in rule:
                        rules[int(number)].append(list(map(int, nums.split())))
            elif len(line.strip()):
                messages.append(line.strip())
    return  rules, messages

def remove_prefix(text, prefix):
    if not text.startswith(prefix):
        return False, text
    else:
        return True, text[len(prefix):]

def check_rule(number, rules, message, verbose = False):
    if type(rules[number]) is str:
        if verbose: print("Print Checking for Character:", rules[number])
        return remove_prefix(message, rules[number])
    for nums in rules[number]:
        if verbose: print("Checking Sequence:", nums)
        temp_msg = message
        for temp_num in nums:
            if verbose: print("Checking if", temp_msg, "matches", temp_num)
            matches_rule, temp_msg = check_rule(temp_num, rules, temp_msg, verbose)
            if not matches_rule:
                if verbose: print(temp_msg, "does not match", nums)
                break
        if matches_rule:
            return True, temp_msg
    return False, ""
            

def puzzle1(verbose = False):
    rules, messages = read_file()
    count = 0
    for message in messages:
        match, temp = check_rule(0, rules, message, False)
        if verbose: 
            print("Checking Message:", message)
            print(message, match)
            print()
        if match and len(temp) == 0: 
            count += 1
    print(count)
    print()


def check_rules(number, rules, message):
    if type(rules[number]) is list:
        yield from check_alternatives(rules[number], rules, message)
    else:
        if message and message.startswith(rules[number]):
            yield message[len(rules[number]):]
    
def check_alternatives(alternative, rules, message):
    for nums in alternative:
        yield from check_sequence(nums, rules, message)
        
def check_sequence(numbers, rules, message):
    if numbers:
        number, *numbers = numbers
        for temp_msg in check_rules(number, rules, message):
            yield from check_sequence(numbers, rules, temp_msg)
    else:
        yield message
    

def puzzle2(verbose = False):
    rules, messages = read_file()
    rules[8] = [[42],[42,8]]
    rules[11] = [[42,31],[42,11,31]]
    count = 0
    for message in messages:
        if any(x == "" for x in check_rules(0, rules, message)):
            count += 1
    print(count)
    print()

puzzle1(True)
puzzle2(True)