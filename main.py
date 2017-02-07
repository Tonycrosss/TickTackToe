import random


squares_number = 9
win_moves = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8))

# player_moves_list = []
# comp_moves_list = []

def new_board():
    board = []
    for square in range(squares_number):
        board.append(square)
    return board


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")


def player_move(board):
    pl_move = input('Выбери число, куда вкатить крест\n')

    if board[int(pl_move)] != 'O' and board[int(pl_move)] != 'X':
        board[int(pl_move)] = 'X'
        # player_moves_list.append(pl_move)

    else:
        print('Это поле уже занято, слепой ?')
        player_move(board)


def computer_move(board):
    comp_move = random.choice(range(9))
    if board[int(comp_move)] != 'X' and board[int(comp_move)] != 'O':
        board[int(comp_move)] = 'O'
        # comp_moves_list.append(comp_move)
    else:
        computer_move(board)


def win_check(board):
    for moves in win_moves:
        if board[moves[0]] == board[moves[1]] == board[moves[2]]:
            global winner
            winner = board[moves[0]]
            return True
        else:
            winner = 0
    return False


def main():
    counter = 0
    board = new_board()
    while not win_check(board):
        display_board(board)
        player_move(board)
        counter += 1
        if counter != 5:
            computer_move(board)
        else:
            print('Ничья!!!')
            break
    display_board(board)
    if winner == 'X':
        print('Ты победил!!!')
    elif winner == 'O':
        print('Победил компьютер!!!')
    print('Игра закончена!')


if __name__ == '__main__':
    main()


# TODO: recode win_moves to FOR IN!!
