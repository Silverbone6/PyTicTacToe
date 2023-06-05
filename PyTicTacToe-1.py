from os import system, name

empty = "#"
key1 = "x"
key2 = "O"
win = False
board = [[empty, empty, empty], [empty, empty, empty], [empty, empty, empty]]
coordinates = {
    "a1": [0, 0],
    "a2": [1, 0],
    "a3": [2, 0],
    "b1": [0, 1],
    "b2": [1, 1],
    "b3": [2, 1],
    "c1": [0, 2],
    "c2": [1, 2],
    "c3": [2, 2],
}


def clear():
    if name == "nt":
        _ = system("cls")


def press_enter():
    input("Press ENTER to continue")


def game_board():
    # El tablero se configura acá
    print("Tic Tac Toe")
    print("  A B C")
    print("1", board[0][0], board[0][1], board[0][2])
    print("2", board[1][0], board[1][1], board[1][2])
    print("3", board[2][0], board[2][1], board[2][2])


def win_check():
    global win
    x = 0
    y = 0
    for i in board:
        if board[x][0] == key1 and board[x][1] == key1 and board[x][2] == key1:
            win = True
            print("Player One wins by row")
        elif board[x][0] == key2 and board[x][1] == key2 and board[x][2] == key2:
            win = True
            print("Player Two wins by row")
        x += 1
    for i in board:
        if board[0][y] == key1 and board[1][y] == key1 and board[2][y] == key1:
            win = True
            print("Player One wins by column")
        elif board[0][y] == key2 and board[1][y] == key2 and board[2][y] == key2:
            win = True
            print("Player Two wins by column")
        y += 1
    if board[0][0] == key1 and board[1][1] == key1 and board[2][2] == key1:
        win = True
        print("Player One wins by y=-x")
    elif board[0][0] == key2 and board[1][1] == key2 and board[2][2] == key2:
        win = True
        print("Player Two wins by y=-x")
    elif board[0][2] == key1 and board[1][1] == key1 and board[2][0] == key1:
        win = True
        print("Player One wins by y=x")
    elif board[0][2] == key2 and board[1][1] == key2 and board[2][0] == key2:
        win = True
        print("Player Two wins by y=x")


def game_instance():
    clear()
    while win == False:
        move1_done = False
        move2_done = False
        while move1_done == False:
            game_board()
            # player 1 instance
            print("Please insert a coordinate between a1 and c3")
            p = input("Player One>")
            c = coordinates[p]
            if board[c[0]][c[1]] == empty:
                board[c[0]][c[1]] = key1
                move1_done = True
            elif board[c[0]][c[1]] == key2:
                print("The selected coordinate is already taken")
                press_enter()
                clear()
                continue
            else:
                print("Please insert a valid coordinate")
                press_enter()
                clear()
        clear()
        win_check()
        if win == False:
            while move2_done == False:
                game_board()
                # player 2 instance
                print("Please insert a coordinate between a1 and c3")
                p = input("Player Two>")
                c = coordinates[p]
                if board[c[0]][c[1]] == empty:
                    board[c[0]][c[1]] = key2
                    move2_done = True
                elif board[c[0]][c[1]] == key1:
                    print("The selected coordinate is already taken")
                    press_enter()
                    clear()
                    continue
                else:
                    print("Please insert a valid coordinate")
                    press_enter()
                    clear()
                clear()
                win_check()


game_instance()
game_board()
