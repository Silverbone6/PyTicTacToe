from os import system, name

x = 0
win = 0
board = [
    ['#', '#', '#'],
    ['#', '#', '#'],
    ['#', '#', '#']
]


def clear():
    if name == 'nt':
        _ = system('cls')


def game_board():
    # El tablero se configura acá
    print('Tic Tac Toe')
    print('  1 2 3')
    print('A', board[0][0], board[0][1], board[0][2])
    print('B', board[1][0], board[1][1], board[1][2])
    print('C', board[2][0], board[2][1], board[2][2])
    print('Please insert a coordinate between a1 and c3')


def game_instance():
    global win
    rep1 = True
    game_board()
    p = input('PLAYER ONE>')
    key = 'x'
    if p == 'a1' and board[0][0] == '#':
        board[0][0] = key
    elif p == 'a2' and board[0][1] == '#':
        board[0][1] = key
    elif p == 'a3' and board[0][2] == '#':
        board[0][2] = key
    elif p == 'b1' and board[1][0] == '#':
        board[1][0] = key
    elif p == 'b2' and board[1][1] == '#':
        board[1][1] = key
    elif p == 'b3' and board[1][2] == '#':
        board[1][2] = key
    elif p == 'c1' and board[2][0] == '#':
        board[2][0] = key
    elif p == 'c2' and board[2][1] == '#':
        board[2][1] = key
    elif p == 'c3' and board[2][2] == '#':
        board[2][2] = key
    elif p == 'dou':
        board[0][0] = key
        board[0][1] = key
        board[0][2] = key
    else:
        clear()
        print('''
Please insert a valid coordinate between a1 - c3
Press ENTER to continue''')
        input()
    # Verificar si gana
    if board[0][0] == board[0][1] == board[0][2] == key:
        win = 1
        rep1 = False
    if board[1][0] == board[1][1] == board[1][2] == key:
        win = 1
        rep1 = False
    if board[2][2] == board[2][1] == board[2][2] == key:
        win = 1
        rep1 = False
    if board[0][0] == board[1][0] == board[2][0] == key:
        win = 1
        rep1 = False
    if board[0][1] == board[1][1] == board[2][1] == key:
        win = 1
        rep1 = False
    if board[0][2] == board[1][2] == board[2][2] == key:
        win = 1
        rep1 = False
    if board[0][0] == board[1][1] == board[2][2] == key:
        win = 1
        rep1 = False
    if board[2][0] == board[1][1] == board[0][2] == key:
        win = 1
        rep1 = False

    # Sección del segundo jugador
    if win == 0:
        game_board()
        p = input('PLAYER TWO>')
        key = 'o'
        if p == 'a1' and board[0][0] == '#':
            board[0][0] = key
        elif p == 'a2' and board[0][1] == '#':
            board[0][1] = key
        elif p == 'a3' and board[0][2] == '#':
            board[0][2] = key
        elif p == 'b1' and board[1][0] == '#':
            board[1][0] = key
        elif p == 'b2' and board[1][1] == '#':
            board[1][1] = key
        elif p == 'b3' and board[1][2] == '#':
            board[1][2] = key
        elif p == 'c1' and board[2][0] == '#':
            board[2][0] = key
        elif p == 'c2' and board[2][1] == '#':
            board[2][1] = key
        elif p == 'c3' and board[2][2] == '#':
            board[2][2] = key
        elif p == 'dou':
            board[0][0] = key
            board[0][1] = key
            board[0][2] = key
        else:
            clear()
            print('''
        Please insert a valid coordinate between a1 - c3
        Press ENTER to continue''')
            rep1 = True
            input()
        # Verificar si gana
        key = 'o'
        if board[0][0] == board[0][1] == board[0][2] == key:
            win = 1
            rep1 = False
        elif board[1][0] == board[1][1] == board[1][2] == key:
            win = 1
            rep1 = False
        elif board[2][2] == board[2][1] == board[2][2] == key:
            win = 1
            rep1 = False
        elif board[0][0] == board[1][0] == board[2][0] == key:
            win = 1
            rep1 = False
        elif board[0][1] == board[1][1] == board[2][1] == key:
            win = 1
            rep1 = False
        elif board[0][2] == board[1][2] == board[2][2] == key:
            win = 1
            rep1 = False
        elif board[0][0] == board[1][1] == board[2][2] == key:
            win = 1
            rep1 = False
        elif board[2][0] == board[1][1] == board[0][2] == key:
            win = 1
            rep1 = False
        else:
            game_instance()
        if win == 1:
            clear()
            print('Player Two Wins')
    else:
        clear()
        print('Player One Wins')


def main():
    rep = True
    clear()
    print("Welcome to the Console-based Tic Tac Toe!")
    print("Ready to win? type 1 to begin, type 0 to exit")
    act = input('>')
    if int(act) == 1:
        game_instance()
        main()
    elif int(act) == 0:
        rep = False
    else:
        clear()
        print('Insert a valid number, 0 or 1')


main()
print('''
Thanks for playing Tic Tac Toe
Developed by Marcos Villena
Press ENTER to exit
''')
input()
