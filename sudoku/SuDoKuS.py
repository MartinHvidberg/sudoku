
""" Solvers - Computer centric solvers
Functions that solve SuDoKus, like a computer, are located here.
These are used to confirm solvability, solutions, unique solutions, multiple solutions, etc.
Nomenclature:
lst_sdk = The SoDuKo. List of 81 integers [0..9] where 0 means empty
lst_pcm = Pencil-marks. List of 81 set of int [1..9]
sdk     = The SuDoKu with pencil-marks and other meta-data. {s: lst_sdk, p: lst_pcm, ...}
i_... functions operate directly on the 'inner' variables, e.g. lst_pcm
n: Number of the cell in a 81 count of cells [0..80]
i: number of col (all cells on same vertical line) [0..8]
j: number of row (all cells on same horizontal line) [0..8]
"""

import logging

# Initialize logging
log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)
log_fil = logging.FileHandler(f"{__file__.rsplit('.',1)[0]}.log", mode='w')
log_fil.setFormatter(logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)s %(funcName)s] - %(levelname)s - %(message)s'))
log.addHandler(log_fil)
log.info(f"Initialise: {__file__}")

def same_row(n,m): return (n//9 == m//9)

def same_col(n,m): return (n-m) % 9 == 0

def same_box(n,m): return (n//27 == m//27 and n%9//3 == m%9//3)

def n2ij(n):
    return

def ij2n(i, j):
    return

def str2loi(str_in):
    """ Convert a string form of a SuDoKu to a list of integers
    Accept both '.' or '0' as blank, but always output blank as 0
    delet any [,|-_] etc before processing
    :param str_in: an 81 character long text string of '0',..,'9','.'
    :return: an 81 long list of 1-digit integers 0..9. On error return empty list
    """
    lst_legal_chars = list("0123456789.")
    if isinstance(str_in, str):
        for c in [',','|','-','_']:
            str_in = str_in.replace(c, '')
        if len(str_in) == 81:
            if all([c in lst_legal_chars for c in str_in]):
                str_in = str_in.replace('.', '0')
                return [int(c) for c in str_in]
            else:
                log.error(f"illegal char in SuDoKu input string: {str_in}")
        else:
            log.error(f"illegal length (!= 81) of SuDoKu input string: {len(str_in)}")
    else:
        log.error(f"illegal data type (not str) of SuDoKu input string: {str(type(str_in))}")
    return []  # On error return empty list

def loi2sdk(loi_in):
    """ Make a sdk (dic of lst_sdk and lst_pcm) from a loi_sdk """
    dic_ret = dict()
    dic_ret['s'] = loi_in  # The actual SuDoKu (81x integers)
    dic_ret['p'] = i_make_pcm(loi_in)  # Pencil marks
    dic_ret['sol'] = set()  # Set of solutions found, so far
    dic_ret['bum'] = False  # True if we hit a dead end
    return dic_ret

def valid_sdk(obj):
    if not isinstance(obj, dict):
        return False
    if not all([k in obj.keys() for k in ['s', 'p', 'sol', 'bum']]):
        return False
    return True

def i_show_small(lst_sdk):
    """ Show the SoDuKo in 2D
    Return a string version for print, with a minimalistic design, of the SoDuKo in the lst_sdk
    :param lst_sdk: the input SoDuKo as a standard list of integers, length = 81
    :return: a (multi-line) string with the SoDuKo in 2D design
    """
    def p(i,j):
        return str(lst_sdk[(i*9)+j])
    def l(i):
        return ("|"+p(i,0)+p(i,1)+p(i,2)+"|"+p(i,3)+p(i,4)+p(i,5)+"|"+p(i,6)+p(i,7)+p(i,8)+"|\n").replace('0',' ')
    def q():
        v = '+---+---+---+\n'
        return (v+l(0)+l(1)+l(2)+v+l(3)+l(4)+l(5)+v+l(6)+l(7)+l(8)+v).strip()
    return q()

def show_small(sdk_l):
    if not valid_sdk(sdk_l) : raise RuntimeError("Not a valid sdk in: show_small()")
    return i_show_small(sdk_l['s'])

def set_cell(n, v, lst_sdk_l):
    """ Set cell number n to value v """
    lst_sdk_l[n] = v
    return lst_sdk_l

def upd_pncl(num_cell, num_valu, lst_pnc_l):
    """ Update all pencil-marks, as if num_cell is given num_valu
    return updated list """
    for m in range(81):  # update pencil-marks
        if same_col(m, num_cell) or same_row(m, num_cell) or same_box(m, num_cell):
            lst_pnc_l[m].discard(num_valu)
    return lst_pnc_l

def place(num_valu, num_cell, sdk_l):
    """ Place value num_valu in cell num_cell, and update all pencil-marks """
    if not valid_sdk(sdk_l) : raise RuntimeError("Not a valid sdk in: place()")
    sdk_l['s'] = set_cell(num_cell, num_valu, sdk_l['s'])
    sdk_l['p'] = upd_pncl(num_cell, num_valu, sdk_l['p'])
    return sdk_l

def list_empty_fields_id(sdk_l):
    """ Return a list of id number (positions) for all empty cells """
    if not valid_sdk(sdk_l) : raise RuntimeError("Not a valid sdk in: list_empty_fields_id()")
    return [n for n in range(len(sdk_l)) if sdk_l[n] == 0]

def i_make_pcm(lst_s):
    """ From a SuDoKu (list of int) make PenCilMarks (list of set of int)
    A pencil mark indicates that this value is 'possible' in this cell """
    lst_p = list()
    for n in range(81):  # for each cell in the SuDoKu
        if lst_s[n] == 0:
            set_n = set(range(1, 10))  # all is possible
            for num_m in [k for k in range(81) if
                      k != n and (same_col(k, n) or same_row(k, n) or same_box(k, n))]:
                set_n.discard(lst_s[num_m])
        else:
            set_n = set()
        lst_p.append(set_n)
    return lst_p

def sudoku_is_solved(sdk_l):
    """ Return True if the SuDoKu is full (no 0 left), otherwise False """
    if not valid_sdk(sdk_l): raise RuntimeError("Not a valid sdk in: sudoku_is_solved()")
    lst_sdk = sdk_l['s']
    return not any([n==0 for n in lst_sdk])

def sudoku_is_dead_end(sdk_l):
    """  Return True if the SuDoKu is in a dead-lock situation, otherwise False
     A dead situation is if a field is empty (0) but has 9 pencil-marks. """
    if not valid_sdk(sdk_l): raise RuntimeError("Not a valid sdk in: sudoku_is_dead_end()")
    lst_empty_fields = list_empty_fields_id(sdk_l['s'])
    return any([len(sdk_l['p'][n]) == 9 for n in lst_empty_fields])

def brute(loi_in):
    """ Brute force - slow solve, all solutions
    Simply check all possible solutions
    :param loi_in:
    :return:
    """

def q_solve(lst_sdk):
    """ Solves the SuDoKu
    Solves the SuDoKu using a minimal algorithm, but using a few tricks that makes it fast - I hope...
    :param lst_sdk: the input SoDuKo as a standard list of integers, length = 81
    :return:
    """

def r_solver(sdk_l, roll_back=False):
    """ Recursive solver
    Go for the pencil marks... Go for the field with max pencil marks, i.e. minimum possible openings.
    Call this function (recursively) with the (few) options.
    Any branch with 9 pencil-marks to an empty cell is dead...
    :param lst_sdk: The input SoDuKo as a standard list of integers, length = 81
    :param lst_pnc: List of set() containing updated pencil marks, length = 81
    :param lst_sol: List of solutions, found until this point - can be an empty list
    :return: lst_sol. A, potentially updated, list of solutions - can be an empty list
    """
    if not valid_sdk(sdk_l) : raise RuntimeError("Not a valid sdk in: r_solver()")
    log.info(f"r_solver(): {len([n for n in sdk_l['s'] if n != 0])}")
    # Check if we have a solved SoDuKo
    if sudoku_is_solved(sdk_l):
        set_sol.add(''.join(str(i) for i in lst_sdk))  # add as string
        print("Solution...")
        return lst_sdk, lst_pnc, set_sol
    # Check if we have an empty field with no remaining options, i.e. an unsolvable situation
    if sudoku_is_dead_end(sdk_l):
        print("bum")
        return lst_sdk, lst_pnc, set_sol, True
    # Pick cell with most pencil-marks, and guess a vacant value
    lst_empty = list_empty_fields_id(lst_sdk)
    num_most_pcm = max([len(lst_pnc[n]) for n in lst_empty])
    num_here = [n for n in lst_empty if len(lst_pnc[n]) == num_most_pcm][0]
    num_guess = [n for n in range(1, 10) if n not in lst_pnc[num_here]][0]
    lst_sdk_n, lst_pnc_n, set_sol_n, bol_rb = _r_solver(set_cell(num_here, num_guess, lst_sdk), upd_pncl(num_here, num_guess, lst_pnc), set_sol)
    # if roll-back, undo last guess
    if bol_rb:  # We hit a problem, and need to roll-back
        pass
    return lst_sdk, lst_pnc, set_sol

if __name__ == "__main__":
    lst_sdk = str2loi(".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..")
    #lst_sdk = str2loi("305790081,000008000,010200739,200060890,001000200,008502000,500047003,603005900,009603000")  # 1
    #lst_sdk = str2loi("000390500,908000603,000000009,000063200,070020006,600010800,000000700,300007000,009100300")  # 2
    #lst_sdk = str2loi("")  # 3
    #lst_sdk = str2loi("")  # 4
    #lst_sdk = str2loi("")  # 5
    print("Start")
    sdk = loi2sdk(lst_sdk)
    print(show_small(sdk))
    print(sdk)
    sdk = r_solver(sdk)
    print("Done...")

