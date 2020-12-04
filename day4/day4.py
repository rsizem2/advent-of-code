
FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def read_file():
    with open('input.txt') as file:
        passport = {}
        passports = []
        for line in file:
            current = line.strip()
            if len(current) == 0:
                passports.append(passport)
                passport = {}
            else:
                temp = current.split()
                for string in temp:
                    key, value = string.split(":")
                    passport[key] = value
        passports.append(passport)
    return passports

def puzzle1():
    passports = read_file()
    count = 0
    for passport in passports:
        keys = set(passport.keys())
        print(keys)
        if FIELDS <= keys:
            print("Valid")
            count += 1
    return count
        

def puzzle2():
    passports = read_file()
    count = 0
    for passport in passports:
        keys = set(passport.keys())
        if not FIELDS <= keys:
            continue
        else: 
            try:
                # valid birth year
                assert(len(passport['byr']) == 4 and set(passport['byr']) <= set('0123456789'))
                assert(1920 <= int(passport['byr']) <= 2002)
                # valid issue year
                assert(len(passport['iyr']) == 4 and set(passport['iyr']) <= set('0123456789'))
                assert(2010 <= int(passport['iyr']) <= 2020)
                # valid exp year
                assert(len(passport['eyr']) == 4 and set(passport['eyr']) <= set('0123456789'))
                assert(2020 <= int(passport['eyr']) <= 2030)
                # valid height
                height = passport['hgt']
                assert(height[-2:] in ['in','cm'] and set(height[:-2]) <= set('0123456789'))
                if height[-2:] == 'in':
                    assert(59 <= int(height[:-2]) <= 76)
                else:
                    assert(150 <= int(height[:-2]) <= 193)
                # valid hair color
                assert(passport['hcl'][0] == '#' and len(passport['hcl'][1:]) == 6)
                assert(set(passport['hcl'][1:]) <= set('0123456789abcdef'))
                # valid eye color
                assert(len(passport['ecl']) == 3 and passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'])
                # valid passport id
                assert(len(passport['pid']) == 9 and set(passport['pid']) <= set('0123456789'))
            except:
                continue
        count += 1
    return count

puzzle2()