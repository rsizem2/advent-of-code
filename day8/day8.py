
def read_file():
    temp = []
    with open('input.txt') as file:
        temp = [tuple(line.strip().split()) for line in file]
        temp = [(x,int(y)) for x,y in temp]
    return temp
            

def puzzle1():
    code = read_file()
    execute(code)

def puzzle2():
    code = read_file()
    for i, (x,y) in enumerate(code):
        if x == "jmp":
            print("Line", i, ":", x , y)
            temp = list(code)
            temp[i] = ("nop", y)
            if execute(temp):
                return
        elif x == "nop":
            print("Line", i, ":", x , y)
            temp = list(code)
            temp[i] = ("jmp", y)
            if execute(temp):
                return
    print("EOF never reached")
            
        

def execute(code):
    visited = {x: False for x in range(len(code))}
    line = 0
    acc = 0
    try:
        while visited[line] == False:
            if code[line][0] == 'nop':
                visited[line] = True
                line += 1
            elif code[line][0] == 'jmp':
                visited[line] = True
                line += code[line][1]
            else:
                visited[line] = True
                acc += code[line][1]
                line += 1
        print("Line executed twice:", line)
        print("Accumulator value:", acc)
        return False
    except:
        print("EOF reached")
        print("Accumulator value:", acc)
        return True
        



puzzle1()
puzzle2()

