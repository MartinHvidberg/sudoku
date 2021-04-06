
import sys

""" A non-OOP form of working 
This module exercises a simpler (non-OOP) way of working with SuDoKus
Mainly used to quickly test algorithms/code from other writers.
"""

# ToDo []: Use pencil positively, and not negatively


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


def valid(str_sdk):
    """ Return True if the SuDoKu correctly filled, i.e. no repeated values in row, col nor box.
        otherwise returns False """
    for n in range(81):
        if str_sdk[n] != '0':
            for m in range(81):
                if str_sdk[m] != '0':
                    if m > n:
                        if (same_row(n, m) and str_sdk[n] == str_sdk[m]) \
                                or (same_col(n, m) and str_sdk[n] == str_sdk[m]) \
                                or (same_box(n, m) and str_sdk[n] == str_sdk[m]):
                            return False
    return True


def done(str_sdk):
    """ Return True if no more blanks, othervise returns False """
    return '0' not in str_sdk and valid(str_sdk)


def col_pcl(str_sdk, i, j):
    """ The (new) pencil marks, indicating 'possible' values for this cell """

    def col_pencil(str_sdk, i, j):
        """ The (old) pencil marks, indicating 'im-possible' values for this cell """
        lst_pnc = list()
        m = (i*9) + j
        for n in range(81):
            if same_col(m, n):
                lst_pnc.append(str_sdk[n])
        set_pnc = set(lst_pnc)
        set_pnc.discard('0')
        return set_pnc

    return {'1','2','3','4','5','6','7','8','9'} - col_pencil(str_sdk, i, j)


def row_pcl(str_sdk, i, j):
    """ The (new) pencil marks, indicating 'possible' values for this cell """

    def row_pencil(str_sdk, i, j):
        lst_pnc = list()
        m = (i*9) + j
        for n in range(81):
            if same_row(m, n):
                lst_pnc.append(str_sdk[n])
        set_pnc = set(lst_pnc)
        set_pnc.discard('0')
        return set_pnc

    return {'1','2','3','4','5','6','7','8','9'} - row_pencil(str_sdk, i, j)


def box_pcl(str_sdk, i, j):
    """ The (new) pencil marks, indicating 'possible' values for this cell """

    def box_pencil(str_sdk, i, j):
        lst_pnc = list()
        m = (i * 9) + j
        for n in range(81):
            if same_box(n, m):
                lst_pnc.append(str_sdk[n])
        set_pnc = set(lst_pnc)
        set_pnc.discard('0')
        return set_pnc

    return {'1','2','3','4','5','6','7','8','9'} - box_pencil(str_sdk, i, j)


def pcl(str_sdk, i, j):
    """ The (new) pencil marks, indicating 'possible' values for this cell """
    return col_pcl(str_sdk, i, j) & row_pcl(str_sdk, i, j) & box_pcl(str_sdk, i, j)


def m(str_sdk, lst_pnc, set_solutions):
    """
    Go for the pencil marks... Go for the field with minimum pencil marks, i.e. minimum possible openings.
    Call this function (recursively) with the (few) options.
    Any branch with 0 pencil-marks to any empty cell is dead...
    :param str_sdk: string of digits, 81 long, 0 = empty
    :param lst_pnc: list of sets of pencil-mark digits, 81 long
    :return: list of solutions, so far
    """
    str_sdk = str_sdk.replace('.', '0')  # Because we allow . as 0 in input
    ##print(f"input sdk: {str_sdk}")
    ##print(f"input pnc: {lst_pnc}")
    ##print(f"input sol: {set_solutions}")
    if done(str_sdk):
        print(f"Solved: {str_sdk}")
        #print(show_small(str_sdk))
        set_solutions.update(str_sdk)
        return set_solutions
    if lst_pnc == []:  # Pencil marks is empty, we must be just started ..
        for n in range(81):
            lst_pnc.append(pcl(str_sdk, n // 9, n % 9))
    ##print(f"pencil marks: {lst_pnc}")
    lst_openings = [n for n in range(81) if str_sdk[n] == '0']
    num_min_pencmarks = min([len(lst_pnc[n]) for n in lst_openings])  # minimum pencil-marks in any open cell
    ##print(f"num min() pencil marks: {num_min_pencmarks}")
    if num_min_pencmarks == 0:  # No solution possible
        return set_solutions
    num_next_move = [n for n in lst_openings if len(lst_pnc[n]) == num_min_pencmarks][0]  # first cell to have min pencil-marks
    ##print(f"Next move: {num_next_move}")
    for num_option in [n for n in range(1,10) if str(n) in lst_pnc[num_next_move]]:
        #print(f"Trying cell: {num_next_move} = {num_option}")
        # update the cells and pencil marks
        str_sdk = str_sdk[:num_next_move] + str(num_option) + str_sdk[num_next_move+1:]
        ##print(f"New sdk: {str_sdk}")
        lst_pnc_to_update = list()
        for n in range(81):
            if (str_sdk[n] == '0') and (same_row(n, num_next_move) or same_col(n, num_next_move) or same_box(n, num_next_move)):
                lst_pnc_to_update.append(n)  # these are the n in [0..80] we need to re-pencil
        ##print(f"pncs to update: {lst_pnc_to_update}")
        ##print(f"in {str(type(lst_pnc))} length {len(lst_pnc)} > {lst_pnc}")
        for n in lst_pnc_to_update:
            set_pnc = lst_pnc[n]
            #print(f"2update: {n} = {set_pnc}")
            set_pnc.discard(num_option)  # fjern '4', i vores tilfælde ...
            lst_pnc[n] = set_pnc
        set_solutions.update(m(str_sdk, lst_pnc, set_solutions))
    return set_solutions


if __name__ == '__main__':
    if len(sys.argv) == 2 and len(sys.argv[1]) == 81:
        m(sys.argv[1])
    else:
        print('Usage: python sudoku.py puzzle')
        print('    where puzzle is an 81 character string representing the puzzle read left-to-right, top-to-bottom, and 0 is a blank')

        str_sdk = '.......12........3..23..4....18....5.6..7.8.......9.....85.....9...4.5..47...6...'.replace('.','0') # Platinum Blonde - Seems to have a HUGE number of solutions ...
        str_sdk = '9265714833514862798749235165823671941492583677631..8252387..651617835942495612738'  # double-solution
        print(show_small(str_sdk))
        set_solved = m(str_sdk, list(), set())
        print(f"Solutions: {set_solved}")

        # NOTE r() have moved ...
        #r('13........2...9......8..7..6....48....5.2...........4.....3...27..5.....8........'.replace('.','0'))
        #r('138475269.2...9......8..7..6....48....5.2...........4.....3...27..5.....8........'.replace('.','0'))
        #r('8..6..9.5.............2.31...7318.6.24.....73...........279.1..5...8..36..3......'.replace('.','0')) # This is known to have 5 solutions