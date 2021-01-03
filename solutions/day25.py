
def transform(subject_number, loop_size):
    val = 1
    for _ in range(loop_size):
        val *= subject_number
        val %= 20201227
    return val

def get_loop_size(public_key):
    subject_number = 7
    val = 1
    loop_size = 0
    while val != public_key:
        val *= subject_number
        val %= 20201227
        loop_size += 1
    try:
        assert val == public_key
    except:
        print(val, public_key)
    print("Loop Size:", loop_size)
    return loop_size

def puzzle1():
    card, door = 5764801, 17807724
    card_loop, door_loop = get_loop_size(card), get_loop_size(door)
    assert transform(door, card_loop) == transform(card, door_loop)
    print(transform(door, card_loop), transform(card, door_loop))
    
    card, door  = 8421034, 15993936
    card_loop, door_loop = get_loop_size(card), get_loop_size(door)
    assert transform(door, card_loop) == transform(card, door_loop)
    print(transform(door, card_loop), transform(card, door_loop))



def puzzle2():
    pass



puzzle1()
puzzle2()