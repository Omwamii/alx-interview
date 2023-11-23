#!/usr/bin/env python3
""" module solving the nqueens problem """
import sys


def diagonals_safe(x, y, board, size):
    """ check +ve and -ve diagonals for threat """
    x_diag = x - 1
    x_c, y_c = x, y  # copy values for neg_diag loop
    while x_diag > 0:
        y_pos_diag = x_diag - x + y
        if y_pos_diag < 0:
            # out of range, diag doesn't exist
            break
        if board[x_diag][y_pos_diag] == 1:
            return False # +ve diagonal not safe
        x, y = x_diag, y_pos_diag
        x_diag -= 1

    x_diag = x_c - 1
    while x_diag > 0:
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


def n_recursive(num_queen, curr_row, board):
    """ recursively set queens on board correctly using backtracking
        num_queen: number of queens
        curr_row: current row on chess board
        board: a list of lists (N X N) representing chess board with queens
    """
    if curr_row >= len(board):
        return  # exit condition

    print(f"+++++ Row {curr_row} ++++++")
    if curr_row == 0:
        first_is_set = False
        for item in board[0]:
            if item == 1:
                first_is_set = True
        if not first_is_set:
            # The first row was never set, first iteration
            board[0][0] = 1 # default first position
            print("Setting [0][0]")
        else:
            # result of backtracking, shift position of first queen
            for index, n in enumerate(board[0]):
                if index == num_queen - 1:
                    # impossible to get soln, exit program
                    return
                if n == 1:
                    new_pos = index + 1 # shift to right
                    board[0][index] = 0  # clear position
                    print(f"Setting [0][{new_pos}]")
                    board[0][new_pos] = 1
                    break
        print()
    else:
        is_set, was_set = False, False
        for index, item in enumerate(board[curr_row]):
            if item == 1:
                was_set = True
                set_index = index
        if was_set:
            # result of backtracking
            board[curr_row][set_index] = 0
            new_y = set_index + 1
            while new_y < num_queen:
                print(f"Checking [{curr_row}][{new_y}] ...")
                if vert_safe(curr_row, new_y, board) and diagonals_safe(curr_row, new_y, board, num_queen):
                    board[curr_row][new_y] = 1
                    is_set = True
                    break
                new_y += 1
        else:
            # first time to set or a re-set (all zeros at the time)
            set_y = 0
            while set_y < num_queen:
                print(f"Checking [{curr_row}][{set_y}] ...")
                if vert_safe(curr_row, set_y, board) and diagonals_safe(curr_row, set_y, board, num_queen):
                    board[curr_row][set_y] = 1
                    is_set = True
                    break
                set_y += 1
        print()
        if not is_set:
            return  # no suitable position found, backtrack
    n_recursive(num_queen, curr_row + 1, board)
    
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
        n_recursive(arg, 0, board)
        print(board)


if __name__ == "__main__":
    nqueens()
