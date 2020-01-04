
import sys

def show_small(str_sdk):
    def p(i,j):
        return str(str_sdk[(i*9)+j])
    def l(i):
        return ("|"+p(i,0)+p(i,1)+p(i,2)+"|"+p(i,3)+p(i,4)+p(i,5)+"|"+p(i,6)+p(i,7)+p(i,8)+"|\n").replace('0',' ')
    def q():
        v = '+---+---+---+\n'
        return (v+l(0)+l(1)+l(2)+v+l(3)+l(4)+l(5)+v+l(6)+l(7)+l(8)+v).strip()
    return q()

def same_row(i,j): return (i//9 == j//9)
def same_col(i,j): return (i%9 == j%9)
def same_box(i,j): return (i//27 == j//27 and i%9//3 == j%9//3)


def col_pencil(str_sdk, i, j):
    lst_pnc = list()
    m = (i*9) + j
    for n in range(81):
        if same_col(m, n):
            lst_pnc.append(str_sdk[n])
    set_pnc = set(lst_pnc)
    set_pnc.discard('0')
    return list(set_pnc)


def row_pencil(str_sdk, i, j):
    lst_pnc = list()
    m = (i*9) + j
    for n in range(81):
        if same_row(m, n):
            lst_pnc.append(str_sdk[n])
    set_pnc = set(lst_pnc)
    set_pnc.discard('0')
    return list(set_pnc)


def box_pencil(str_sdk, i, j):
    lst_pnc = list()
    m = (i*9) + j
    for n in range(81):
        if same_box(n, m):
            lst_pnc.append(str_sdk[n])
    set_pnc = set(lst_pnc)
    set_pnc.discard('0')
    return list(set_pnc)


def pencil(str_sdk, i, j):
    lst_col_pencil = col_pencil(str_sdk, i, j)
    lst_row_pencil = row_pencil(str_sdk, i, j)
    lst_box_pencil = box_pencil(str_sdk, i, j)
    return set(lst_col_pencil + lst_row_pencil + lst_box_pencil)


def m(str_sdk, lst_pnc, set_solutions):
    """
    Go for the pencil marks... Go for the field with max pencil marks, i.e. minimum possible openings.
    Call this function (recursively) with the (few) options.
    Any branch with 9 pencil-marks to any empty cell is dead...
    :param str_sdk: string of digits, 81 long, 0 = empty
    :param lst_pnc: list of sets of pencil-mark digits, 81 long
    :return: list of solutions, so far
    """
    ##print(f"input sdk: {str_sdk}")
    ##print(f"input pnc: {lst_pnc}")
    ##print(f"input sol: {set_solutions}")
    if not '0' in str_sdk:
        print(f"Solved: {str_sdk}")
        #print(show_small(str_sdk))
        set_solutions.update(str_sdk)
        return set_solutions
    if lst_pnc == []:  # Pencil marks is empty
        for n in range(81):
            lst_pnc.append(pencil(str_sdk, n // 9, n % 9))
    ##print(f"pencil marks: {lst_pnc}")
    lst_openings = [n for n in range(81) if str_sdk[n] == '0']
    num_max_pencmarks = max([len(lst_pnc[n]) for n in lst_openings])  # max pencil-marks in any open cell
    ##print(f"num max() pencil marks: {num_max_pencmarks}")
    if num_max_pencmarks == 9:  # No solution possible
        return set_solutions
    num_next_move = [n for n in lst_openings if len(lst_pnc[n]) == num_max_pencmarks][0]  # first cell to have max pencil-marks
    ##print(f"Next move: {num_next_move}")
    for num_option in [n for n in range(1,10) if str(n) not in lst_pnc[num_next_move]]:
        #print(f"Trying cell: {num_next_move} = {num_option}")
        # update the cells and pencil marks
        str_sdk = str_sdk[:num_next_move] + str(num_option) + str_sdk[num_next_move+1:]
        ##print(f"New sdk: {str_sdk}")
        lst_pnc_to_update = list()
        for n in range(81):
            if (str_sdk[n] == '0') and (same_row(n, num_next_move) or same_col(n, num_next_move) or same_box(n, num_next_move)):
                lst_pnc_to_update.append(n)
        ##print(f"pncs to update: {lst_pnc_to_update}")
        ##print(f"in {str(type(lst_pnc))} length {len(lst_pnc)} > {lst_pnc}")
        for n in lst_pnc_to_update:
            set_pnc = lst_pnc[n]
            #print(f"2update: {n} = {set_pnc}")
            set_pnc.update()
            lst_pnc[n] = set_pnc
        set_solutions.update(m(str_sdk, lst_pnc, set_solutions))
    return set_solutions


if __name__ == '__main__':
    if len(sys.argv) == 2 and len(sys.argv[1]) == 81:
        m(sys.argv[1])
    else:
        print('Usage: python sudoku.py puzzle')
        print('    where puzzle is an 81 character string representing the puzzle read left-to-right, top-to-bottom, and 0 is a blank')
        #r('13........2...9......8..7..6....48....5.2...........4.....3...27..5.....8........'.replace('.','0'))
        str_sdk = '.......12........3..23..4....18....5.6..7.8.......9.....85.....9...4.5..47...6...'.replace('.','0') # Platinum Blonde
        print(show_small(str_sdk))
        set_solved = m(str_sdk, list(), set())
        print(f"Solutions: {set_solved}")
        #r('138475269.2...9......8..7..6....48....5.2...........4.....3...27..5.....8........'.replace('.','0'))
        #r('8..6..9.5.............2.31...7318.6.24.....73...........279.1..5...8..36..3......'.replace('.','0')) # This is known to have 5 solutions