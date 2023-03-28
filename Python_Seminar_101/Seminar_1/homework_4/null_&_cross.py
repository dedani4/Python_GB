def input_size():
    return int(input('input size of field'))


def print_field(matrix, size):
    print("\033[H\033[J")
    for i in range(-1, size):
        if i == -1:
            print('   ', end=" ")
        else:
            print(f'{chr(i + 65)} |', end=" ")
        for j in range(size):
            if i == -1:
                print(f'{j + 1}  ', end=" ")
            else:
                print(f'{matrix[i][j] if matrix[i][j] != 0 else " "} |', end=" ")
        print()
        print('  |' + '-' * (size * 4 -1) + '|')


def check_result(matrix, size):
    x = [0, 0, 0, 0]
    o = [0, 0, 0, 0]
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'X':
                x[0] += 1
            elif matrix[i][j] == 'O':
                o[0] += 1
            if matrix[j][i] == 'X':
                x[1] += 1
            elif matrix[j][i] == 'O':
                o[1] += 1
        if matrix[i][i] == 'X':
            x[2] += 1
        elif matrix[i][i] == 'O':
            o[2] += 1
        if matrix[i][size - i - 1] == 'X':
            x[3] += 1
        elif matrix[i][size - i - 1] == 'O':
            o[3] += 1
    if size in x:
        return 'X'
    elif size in o:
        return 'O'
    else:
        return 0


#
def make_move(matrix, side):
    input_move = input(f'input {"X" if side else "O"} as \'A1\': ')
    matrix[ord(input_move[0].upper()) - 65][int(input_move[1]) - 1] = "X" if side else "O"


size = input_size()
matrix = [[0 for _ in range(size)] for i in range(size)]
side = 1

while not check_result(matrix, size):
    print_field(matrix, size)
    make_move(matrix, side)
    side = 1 - side

if 'X' in check_result(matrix, size):
    print('X wins')
elif 'O' in check_result(matrix, size):
    print('O wins')
