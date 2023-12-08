#!/usr/bin/python3
""" module solving the nqueens problem """
import sys


def clear_board(board):
    """ clear board for a new solution to be generated """
    for x in range(0, len(board)):
        for y in range(0, len(board[x])):
            board[x][y] = 0


def diagonals_safe(x, y, board, size):
    """ check +ve and -ve diagonals for threat """
    x_diag = x - 1
    x_c, y_c = x, y  # copy values for -ve diagonal loop
    while x_diag >= 0:
        y_pos_diag = x_diag - x + y
        if y_pos_diag < 0:
            # out of range, diagonal doesn't exist
            break
        if board[x_diag][y_pos_diag] == 1:
            return False  # +ve diagonal not safe
        x, y = x_diag, y_pos_diag
        x_diag -= 1

    x_diag = x_c - 1
    while x_diag >= 0:
        y_neg_diag = x_c - x_diag + y_c
        if y_neg_diag >= size:
            break
        if board[x_diag][y_neg_diag] == 1:
            return False  # -ve diagonal not safe
        x_c, y_c = x_diag, y_neg_diag
        x_diag -= 1
    return True


def vert_safe(x, y, board):
    """ check y axis for any threat """
    for v in range(0, x):
        if board[v][y] == 1:
            return False
    return True


def n_recursive(num_queen, x_val, y_val, board):
    """ recursively set queens on board correctly using backtracking
        num_queen: number of queens
        curr_row: current row on chess board
        board: a list of lists (N X N) representing chess board with queens
    """
    if x_val >= len(board):  # exit condition
        # all queens are set, print the soln
        soln = list()
        for idx, row in enumerate(board):
            for pos, col in enumerate(row):
                if col == 1:
                    soln.append([idx, pos])
        print(soln)
        return True

    is_set, is_first = False, False
    try:
        set_y_prev = board[x_val].index(1)
    except ValueError:
        set_y_prev = 0  # first position as default
        is_first = True if x_val == 0 else 0
    finally:
        board[x_val][set_y_prev] = 0  # clear current position if set
        set_y = set_y_prev + 1 if not is_first else 0
        while set_y < num_queen:
            if (vert_safe(x_val, y_val, board) and
        diagonals_safe(x_val, y_val, board, num_queen)):
                board[x_val][set_y] = 1
                while n_recursive(num_queen, x_val + 1, y_val, board):
                    print(f"checking {x_val}")
                    pass
                print(f"Set [{x_val}][{set_y}]")
                is_set = True
                break
        set_y += 1
    if not is_set:
        if x_val - 1 <= 0:
            return False
        return n_recursive(num_queen, x_val - 1, y_val, board)
    return n_recursive(num_queen, x_val + 1, y_val, board)


def nqueens():
    """ solve nqueens """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    arg = sys.argv[1]
    try:
        arg = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    else:
        if arg < 4:
            print("N must be at least 4")
            sys.exit(1)
        board = list()  # create chess board
        for n in range(0, arg):
            row = list()
            for r in range(0, arg):
                row.append(0)  # initialize each position to '0'
            board.append(row)
        n_recursive(arg, 0, 0, board)
        #for i in range(0, arg):
        #    while n_recursive(arg, 0, i, board):
        #        pass
        #    clear_board(board)  # clear the board for new soln


if __name__ == "__main__":
    nqueens()
