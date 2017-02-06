import random



squares_number = 9
win_moves = [(0, 1, 2)]
player_moves_list = []


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
    pl_move = input('выбери число, куда вкатить крест\n')
    if board[int(pl_move)] != 'O':
        board[int(pl_move)] = 'X'
        player_moves_list.append(pl_move)

    else:
        print('Это поле уже занято, ты пропускаешь ход')


def computer_move(board):
    comp_move = random.choice(range(9))
    print(comp_move)
    board[int(comp_move)] = 'O'
    




def win_check():
    pass


def main():
    board = new_board()
    while 1:
        display_board(board)
        player_move(board)
        computer_move(board)



if __name__ == '__main__':
    main()



