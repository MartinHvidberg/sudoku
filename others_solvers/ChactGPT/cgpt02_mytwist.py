### Changing it so it actually wotks.
# introducing deepcopy()

import copy


def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return [board[:]]  # All cells are filled, puzzle is solved

    solutions = []
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            solutions.extend(solve_sudoku(board))

            board[row][col] = 0  # Backtrack

    return solutions



def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def print_sudoku(board):
    for row in board:
        print(' '.join(map(str, row)))


# Example Sudoku puzzle (0 represents empty cells)

puzzle=[
    [2, 9, 5, 7, 4, 3, 8, 6, 1],
    [4, 3, 1, 8, 6, 5, 9, 0, 0],
    [8, 7, 9, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 2, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [1, 5, 4, 9, 3, 8, 6, 0, 0]
]


solutions = solve_sudoku(puzzle)
print(f"sol: {solutions}")

if solutions:
    print(f"Total solutions: {len(solutions)}")
    for idx, solution in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        print_sudoku(solution)
        print()
else:
    print("No solution exists.")
