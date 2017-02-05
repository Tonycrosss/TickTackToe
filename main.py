squares_number = 9


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


board = new_board()
display_board(board)
