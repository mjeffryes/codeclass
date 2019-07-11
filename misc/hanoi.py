# hanoi.py
# A solver for the "Towers of Hanoi problem"

def init_towers(disks):
    A = list(range(0, disks+1))
    B = [0] * (disks + 1)
    C = [0] * (disks + 1)
    return [A, B, B]

def one_disk_str(width, disk):
    if disk == 0:
        return '|' + (' ' * (width-1))
    else:
        return ('-' * disk) + (' ' * (width - disk))

def one_tower_strings(width, tower):
    if tower == []:
        return []
    else:
        return [one_disk_str(width, tower[0])] + one_tower_strings(width, tower[1:])

def print_towers_strings(A, B, C):
    if A != []:
        print(A[0], B[0], C[0])
        print_towers_strings(A[1:], B[1:], C[1:])

def print_towers(towers):
    width = len(towers[0])
    A = one_tower_strings(width, towers[0])
    B = one_tower_strings(width, towers[1])
    C = one_tower_strings(width, towers[2])
    print_towers_strings(A, B, C)





def hanoi(disks, source, middle, target):
    if disks == 1:
        return [[1, source, target]]
 
    return hanoi(disks - 1, source, target, middle) \
        + [[disks, source, target]] \
        + hanoi(disks - 1, middle, source, target)



































def print_moves(moves):
    """ Accepts a list containing [disk_number, source_tower, destination_tower]
        And prints a string explaining the move
    """
    if moves != []:
        move = moves[0]
        print('Move disk', move[0], 'from tower', move[1], 'to tower', move[2])
        print_moves(moves[1:])
 
def hanoi(disks, source, middle, target):
    """ Accepts the number of disks to move (disks), and the names of the source, middle and target towers
        Returns a list of moves in the form [disk_number, source_tower, destination_tower]
        that move the specified number of disks from the source tower to the target tower
    """
    # base case
    if disks == 1:
        return [[1, source, target]]
    # recursive step
    else:
        return hanoi(disks - 1, source, target, middle) + \
        [[disks, source, target]] + \
        hanoi(disks - 1, middle, source, target)

 
disks = int(input('Enter number of disks: '))
moves = hanoi(disks, 'A', 'B', 'C')
print_moves(moves)


































#towers = init_towers(disks)
#print_towers(towers)
