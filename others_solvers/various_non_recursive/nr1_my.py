
def extract_zones(board):
    """Read the board and extract the number of elements
    in all the squares (3x3),
    rows and columns. Add them in an array sorted desc
    by how many elements they have"""
    zones = []
    # extract lines info
    for row in range(0, len(board)):
        zone = {}
        zone["type"] = "row"
        zone["len"] = len(board[row]) - board[row].count(0)
        zone["coord"] = row
        insert_sorted(zone, zones)
    # extract columns info
    for col in range(0, 9):
        nr_elements = 0
        for row in range(0, 9):
            if board[row][col] != 0:
                nr_elements += 1
        zone = {}
        zone["type"] = "col"
        zone["len"] = nr_elements
        zone["coord"] = col
        insert_sorted(zone, zones)
    # extract squares info
    for square in generate_square_coords():
        nr_elements = 0
        for row in range(square["row_begin"], square["row_end"] + 1):
            for col in range(square["col_begin"], square["col_end"] + 1):
                if board[row][col] != 0:
                    nr_elements += 1
        zone = {}
        zone["type"] = "square"
        zone["len"] = nr_elements
        zone["coord"] = tuple(square.values())
        insert_sorted(zone, zones)

    return zones


def insert_sorted(zone, zones):
    """Take a dictionary describing a zone
    and inserted in the list of zones based
    on the len field"""
    if len(zones) == 0:
        zones.append(zone)
    else:
        inserted = False
        for i in range(0, len(zones)):
            if zone["len"] > zones[i]["len"]:
                zones.insert(i, zone)
                inserted = True
                break
            else:
                continue
        if not inserted:  # it was smaller than all of them
            zones.append(zone)


def insert_possibilities(puzzle, row, col):
    """Eliminate possibilities for the position
    and insert if left with only one"""
    if puzzle[row][col] == 0:
        row_elements = get_zone_elements("row", row, col, puzzle)
        col_elements = get_zone_elements("col", row, col, puzzle)
        square_elements = get_zone_elements("square", row, col, puzzle)
        numbers = [number for number in range(1, 10)]
        possibilities = [i for i in range(1, 10)]
        for possibility in numbers:
            if (possibility in row_elements) or (
                    possibility in col_elements) or (
                    possibility in square_elements):
                possibilities.remove(possibility)
        if len(possibilities) == 1:
            puzzle[row][col] = possibilities[0]


def get_zone_elements(zone_type, coord1, coord2, board):
    """Get all non-zero elements from a col, row or square
    zone_type (str): col / row / square
    coord1, coord2 (int): coordinates of the element we're at
    coord1 = row
    coord2 = col"""
    elements = []
    if zone_type == "col":
        for row in range(0, 9):
            if board[row][coord2] != 0:
                elements.append(board[row][coord2])
    elif zone_type == "row":
        for col in range(0, 9):
            if board[coord1][col] != 0:
                elements.append(board[coord1][col])
    else:
        square_coords = generate_square_coords()
        for square in square_coords:
            if (square["row_begin"] <= coord1 <= square["row_end"]) and (
                    square["col_begin"] <= coord2 <= square["col_end"]):
                for row in range(square["row_begin"], square["row_end"] + 1):
                    for col in range(square["col_begin"],
                                     square["col_end"] + 1):
                        if board[row][col] != 0:
                            elements.append(board[row][col])
                break

    return elements


def generate_square_coords():
    """Build a tuple of disctionaries with square coords"""
    square_coordinates = []
    row_begin = 0
    row_end = 2
    col_begin = 0
    col_end = 2

    while len(square_coordinates) < 9:
        square_coordinates.append({
            "row_begin": row_begin,
            "row_end": row_end,
            "col_begin": col_begin,
            "col_end": col_end
        })
        if col_begin < 6 and col_end < 8:
            col_begin += 3
            col_end += 3
        else:
            col_begin = 0
            col_end = 2
            row_begin += 3
            row_end += 3

    return tuple(square_coordinates)

def print_board(board):
    """Take the board and print it in a readable way in the console"""
    print("-\t" * 13)
    for row in range(0, len(board)):
        formatted_str = "|" + "\t"
        for col in range(0, len(board[row])):
            if col in [3, 6]:
                formatted_str += "|\t"
            formatted_str += str(board[row][col]) + "\t"
        formatted_str += "|"
        print(formatted_str)
        if row in [2, 5]:
            print("-\t" * 13)
    print("-\t" * 13)

def main(puzzle):
    #print_board(puzzle)
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
    return puzzle


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
    puz_ret = main(puzzle)
    #print("=" * 50)
    print_board(puz_ret)