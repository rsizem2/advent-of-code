from collections import Counter

def read_file():
    ingredients = list()
    allergens = list()
    with open('../input/day21_input.txt') as file:
        for line in file:
            line = line.strip()[:-1]
            first, second = line.split("(contains ")
            if "," not in second:
                allergens.append([second])
            else:
                allergens.append(second.split(", "))
            ingredients.append(first.split())
    return allergens, ingredients

def puzzle1():
    allergens, ingredients = read_file()
    temp = dict()
    ans = dict()
    for i, (ingred,aller) in enumerate(zip(ingredients, allergens)):
        for food in aller:
            if food not in temp:
                temp[food] = set(ingred)
            else:
                temp[food] &= set(ingred)
    while temp:
        key, val = min(temp.items(), key = lambda x: len(x[1]))
        food = val.pop()
        for allergen in temp:
            if food in temp[allergen]:
                temp[allergen].remove(food)
        ans[food] = key
        del temp[key]
    counts = Counter([])
    for foods in ingredients:
        counts.update(foods)
    count = 0
    for food in counts:
        if food not in ans:
            count += counts[food]
    print(count)
    return ans
    
    
def puzzle2(temp):
    print(','.join(sorted(temp.keys(), key = lambda x: temp[x])))

temp = puzzle1()
puzzle2(temp)