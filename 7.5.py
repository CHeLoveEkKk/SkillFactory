board_size = 3
#поле
board = [1,2,3,4,5,6,7,8,9]

# Вывод игрового поля
def game_board():
    print("_" * 12)
    for i in range(3):
        print((" " * 3 + "|") * 3)
        print("", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print(("_" * 3 + "|") * 3)


# Ход в игре
def game_step(index, player):
    if (index > 9 or index < 1 or board[index - 1] in ("x", "O")):
        return False

    board [index - 1] = player
    return True

# Проверка победы
def check():
    win = False
    win_comb = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    for pos in win_comb:
        if (board[pos[0]] ==  board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win

# Запуск игры
def start():
    player_now = "X"
    step = 1
    game_board()

    while (step < 10) and (check() == False):
        index = input("Ходит игрок " + player_now + ". Введите номер поля (0 - выход):")

        if (index == "0"):
            break

        if( game_step(int(index), player_now)):
            print("Ход совершен")

            if (player_now == "X"):
                player_now = "O"
            else:
                player_now = "X"

            game_board()

            step += 1
        else:
            print("Неверный ход!")

    if (step == 10):
        print("Ничья")
    else:
        print("Выиграл " + check())

start()