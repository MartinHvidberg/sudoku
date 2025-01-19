""" Chact GPT-3.5
    url: https://chat.openai.com/
    on question: Please find all the solutions, not just one. Follow up on cgpt01
    date: 2023-08-12
    """


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
        return [board.copy()]  # All cells are filled, the puzzle is solved

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
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solutions = solve_sudoku(puzzle)

if solutions:
    print(f"Total solutions: {len(solutions)}")
    for idx, solution in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        print_sudoku(solution)
        print()
else:
    print("No solution exists.")
