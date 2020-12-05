
def read_file():
    with open('input.txt') as file:
        temp = [line.strip() for line in file]
    return temp

def find_row(string):
    min_row = 0
    max_row = 127
    for x in string:
        if x in 'F':
            max_row = min_row + (max_row - min_row) // 2
        else:
            min_row = min_row + (max_row - min_row + 1) // 2
    assert min_row == max_row
    return min_row

def find_col(string):
    min_col = 0
    max_col = 7
    for x in string:
        if x in 'L':
            max_col = min_col + (max_col - min_col) // 2
        else:
            min_col = min_col + (max_col - min_col + 1) // 2
    assert min_col == max_col
    return min_col

def puzzle1():
    passes = read_file()
    ids = []
    for string in passes:
        row = find_row(string[:7])
        col = find_col(string[7:])
        ids.append(row * 8 + col)
    return max(ids)

def puzzle2():
    passes = read_file()
    seats = []
    ids = []
    for string in passes:
        row = find_row(string[:7])
        col = find_col(string[7:])
        seat_id = row * 8 + col
        seats.append((row, col, seat_id))
        ids.append(seat_id)
    min_seat = min(ids)
    max_seat = max(ids)
    all_seats = set(range(min_seat, max_seat + 1))
    taken_seats = set(ids)
    return all_seats - taken_seats
    
print(puzzle1())
print(puzzle2())