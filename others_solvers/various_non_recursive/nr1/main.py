from utils import *

if __name__ == '__main__':
    puzzle = [[8, 7, 6, 9, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 6, 0, 0, 0],
              [0, 4, 0, 3, 0, 5, 8, 0, 0],
              [4, 0, 0, 0, 0, 0, 2, 1, 0],
              [0, 9, 0, 5, 0, 0, 0, 0, 0],
              [0, 5, 0, 0, 4, 0, 3, 0, 6],
              [0, 2, 9, 0, 0, 0, 0, 0, 8],
              [0, 0, 4, 6, 9, 0, 1, 7, 3],
              [0, 0, 0, 0, 0, 1, 0, 0, 4]]

    print_board(puzzle)
    for itrations in range(0, 3):
        zones = extract_zones(puzzle)
        for zone in zones:
            if zone["type"] == "row":
                row = zone["coord"]
                for col in range(0, 9):
                    insert_possibilities(puzzle, row, col)
            elif zone["type"] == "col":
                col = zone["coord"]
                for row in range(0, 9):
                    insert_possibilities(puzzle, row, col)
            else:
                row_begin = zone["coord"][0]
                row_end = zone["coord"][1]
                col_begin = zone["coord"][2]
                col_end = zone["coord"][3]
                for row in range(row_begin, row_end + 1):
                    for col in range(col_begin, col_end + 1):
                        insert_possibilities(puzzle, row, col)

    print("=" * 50)
    print_board(puzzle)

