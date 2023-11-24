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


def n_recursive(num_queen, curr_row, lead, board):
    """ recursively set queens on board correctly using backtracking
        num_queen: number of queens
        curr_row: current row on chess board
        board: a list of lists (N X N) representing chess board with queens
    """
    if curr_row >= len(board):  # exit condition
        # all queens are set, print the soln
        soln = list()
        for idx, row in enumerate(board):
            for pos, col in enumerate(row):
                if col == 1:
                    soln.append([idx, pos])
        print(soln)
        return True

    if curr_row == 0:
        board[0][lead] = 1  # default first position
        # print(f"Iteration of [0][{lead}]")
        return n_recursive(num_queen, curr_row + 1, lead, board)

    else:
        is_set = False
        try:
            set_index = board[curr_row].index(1)
        except ValueError:
            was_set = False
        else:
            was_set = True
        if was_set:
            # result of backtracking
            # print(f"Row: {curr_row} A backtrack {board}")
            board[curr_row][set_index] = 0  # clear the current position
            new_y = set_index + 1
            while new_y < num_queen:
                if vert_safe(curr_row, new_y, board) and\
                        diagonals_safe(curr_row, new_y, board, num_queen):
                    board[curr_row][new_y] = 1
                    # print(f"Set [{curr_row}][{new_y}]")
                    is_set = True
                    break
                new_y += 1
        else:
            # first time to set or a re-set (all zeros at the time)
            # print(f"Row {curr_row} A set or re-set (all 0) {board}")
            set_y = 0
            while set_y < num_queen:
                if vert_safe(curr_row, set_y, board) and\
                        diagonals_safe(curr_row, set_y, board, num_queen):
                    board[curr_row][set_y] = 1
                    # print(f"Set [{curr_row}][{set_y}]")
                    is_set = True
                    break
                set_y += 1
        if not is_set:
            # no position was found, backtrack
            if curr_row - 1 == 0:
                return False
            return n_recursive(num_queen, curr_row - 1, lead, board)
        return n_recursive(num_queen, curr_row + 1, lead, board)


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
        for i in range(0, arg):
            while n_recursive(arg, 0, i, board):
                pass
            clear_board(board)  # clear the board for new soln


if __name__ == "__main__":
    nqueens()
