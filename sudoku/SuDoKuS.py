
""" Solvers - Computer centric solvers
Functions that solve SuDoKus, like a computer, are located here.
These are used to confirm solvability, solutions, unique solutions, multiple solutions, etc.
Nomenclature:
lst_sdk = The SoDuKo. List of 81 integers [0..9] where 0 means empty
lst_pcm = Pencil-marks. List of 81 set of int [1..9]
sdk     = The SuDoKu with pencil-marks and other meta-data. {s: lst_sdk, p: lst_pcm, ...}
_i functions operate directly on the 'inner' variables, e.g. lst_pcm
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

# def n2ij(n):
#     return
#
# def ij2n(i, j):
#     return

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
    dic_ret['p'] = pncl_make_i(loi_in)  # Pencil marks
    dic_ret['sol'] = set()  # Set of solutions found, so far
    dic_ret['bum'] = False  # True if we hit a dead end
    return dic_ret

def is_valid(obj):
    if not isinstance(obj, dict):
        return False
    if not all([k in obj.keys() for k in ['s', 'p', 'sol', 'bum']]):
        return False
    return True

def show_small_i(lst_sdk):
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
    if not is_valid(sdk_l) : raise RuntimeError("Not a valid sdk in: show_small()")
    return show_small_i(sdk_l['s'])

def set_cell_i(n, v, lst_sdk_l):
    """ Set cell number n to value v """
    lst_sdk_l[n] = v
    return lst_sdk_l

def set_cell(n, v, sdk_l):
    sdk_l['s'] = set_cell_i(n, v, sdk_l['s'])
    return sdk_l

def place(num_valu, num_cell, sdk_l):
    """ Place value num_valu in cell num_cell,
    and update all pencil-marks """
    if not is_valid(sdk_l) : raise RuntimeError("Not a valid sdk in: place()")
    sdk_l['s'] = set_cell_i(num_cell, num_valu, sdk_l['s'])
    sdk_l['p'] = pncl_rem(num_cell, num_valu, sdk_l['p'])  # SSS This can be speeded up
    sdk_l['p'][num_cell] = set()  # and clear all own pencil-marks
    return sdk_l

def un_place(num_cell, sdk_l):
    """ Un-Place (return to 0) value in cell num_cell,
    and update all pencil-marks """
    if not is_valid(sdk_l) : raise RuntimeError("Not a valid sdk in: place()")
    set_cell(num_cell, 0, sdk_l)  # re-set cell to empty
    sdk_l = pncl_make(sdk_l)  # re-build pencil marks
    return sdk_l

def list_empty_fields_id_i(lst_sdk):
    """ Return a list of id number (positions) for all empty cells """
    return [n for n in range(len(lst_sdk)) if lst_sdk[n] == 0]

def list_empty_fields_id(sdk_l):
    """ Return a list of id number (positions) for all empty cells """
    if not is_valid(sdk_l) : raise RuntimeError("Not a valid sdk in: list_empty_fields_id()")
    return list_empty_fields_id_i(sdk_l['s'])

def pncl_make_i(lst_s):
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

def pncl_make(sdk_l):
    """ Re-do, from scratch, all pencilmarks, based on present SuDoKu values
    Used initially, and after each roll-back. """
    sdk_l['p'] = pncl_make_i(sdk_l['s'])
    return sdk_l

def pncl_rem(num_cell, num_valu, lst_pnc_l):
    """ Remove all pencil-marks, as if num_cell is given num_valu
    return updated list """
    for m in range(81):  # update pencil-marks
        if same_col(m, num_cell) or same_row(m, num_cell) or same_box(m, num_cell):
            lst_pnc_l[m].discard(num_valu)
    return lst_pnc_l

def find_min_p_count(sdk_l):
    lst_empty = list_empty_fields_id(sdk_l)
    return min([len(sdk_l['p'][n]) for n in lst_empty])

def find_min_p_cell(sdk_l):
    lst_empty = list_empty_fields_id(sdk_l)
    num_min_p_count = find_min_p_count(sdk_l)
    for num_cand in lst_empty:
        if len(sdk_l['p'][num_cand]) == num_min_p_count:
            return num_cand
    return None

def guess(num_cell, sdk_l):
    if sdk_l['s'][num_cell] == 0:
        if len(sdk_l['p'][num_cell]) > 0:
            return next(iter(sdk['p'][num_cell]))  # select a value, without remove
        else:
            return None  # Empty cell with no options left, i.e. a dead end...
    else:
        return sdk_l['s'][num_cell]  # cell is all ready filled, no need to guess

def is_solved(sdk_l):
    """ Return True if the SuDoKu is full (no 0 left), otherwise False """
    if not is_valid(sdk_l): raise RuntimeError("Not a valid sdk in: is_solved()")
    lst_sdk = sdk_l['s']
    return not any([n==0 for n in lst_sdk])

def is_dead_end(sdk_l):
    """  Return True if the SuDoKu is in a dead-lock situation, otherwise False
     A dead situation is if a field is empty (0) but has no pencil-marks left. """
    if not is_valid(sdk_l): raise RuntimeError("Not a valid sdk in: is_dead_end()")
    lst_empty_fields = list_empty_fields_id(sdk_l)
    return any([len(sdk_l['p'][n]) == 9 for n in lst_empty_fields])

# def brute(loi_in):
#     """ Brute force - slow solve, all solutions
#     Simply check all possible solutions
#     :param loi_in:
#     :return:
#     """

# def q_solve(lst_sdk):
#     """ Solves the SuDoKu
#     Solves the SuDoKu using a minimal algorithm, but using a few tricks that makes it fast - I hope...
#     :param lst_sdk: the input SoDuKo as a standard list of integers, length = 81
#     :return:
#     """

def r_solver(sdk_l):
    """ Recursive solver
    Go for the pencil marks... Go for the field with max pencil marks, i.e. minimum possible openings.
    Call this function (recursively) with the (few) options.
    Any branch with 9 pencil-marks to an empty cell is dead...
    :param lst_sdk: The input SoDuKo as a standard list of integers, length = 81
    :param lst_pnc: List of set() containing updated pencil marks, length = 81
    :param lst_sol: List of solutions, found until this point - can be an empty list
    :return: lst_sol. A, potentially updated, list of solutions - can be an empty list
    """
    if not is_valid(sdk_l) : raise RuntimeError("Not a valid sdk in: r_solver()")
    log.info(f"r_solver(): {len([n for n in sdk_l['s'] if n != 0])}")
    # if len(list_empty_fields_id(sdk_l)) > 0:
    #     print(f"{len(list_empty_fields_id(sdk_l))} left")
    # Check if we have a solved SoDuKo
    if is_solved(sdk_l):
        sdk_l['sol'].add(''.join(str(i) for i in lst_sdk))  # add as string
        print(f"Solution...")
        return sdk_l, False
    # Check if we have an empty field with no remaining options, i.e. an unsolvable situation
    if is_dead_end(sdk_l):
        print("bum")
        return sdk_l, True
    # Pick cell with minimum pencil-marks, and guess a vacant value
    num_here = find_min_p_cell(sdk_l)
    num_guess = guess(num_here, sdk_l)
    sdk_l = place(num_guess, num_here, sdk_l)
    sdk_l, bol_rb = r_solver(sdk_l)
    # if roll-back, undo last guess
    if bol_rb:  # We hit a problem, and need to roll-back
        log.debug(f"roll-back guess:{num_guess}")
        sdk_l = un_place(num_here, sdk_l)
    return sdk_l, False

if __name__ == "__main__":
    #lst_sdk = str2loi(".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..")
    #lst_sdk = str2loi("305790081,000008000,010200739,200060890,001000200,008502000,500047003,603005900,009603000")  # 1
    lst_sdk = str2loi("000390500,908000603,000000009,000063200,070020006,600010800,000000700,300007000,009100300")  # 2
    #lst_sdk = str2loi("")  # 3
    #lst_sdk = str2loi("")  # 4
    #lst_sdk = str2loi("")  # 5
    #lst_sdk = str2loi("295743861,431865900,876192543,387459216,612387495,549216738,763524189,928671354,154938600")  # multi solution A
    #lst_sdk = str2loi("906070403,000400200,070023010,500000100,040208060,003000005,030700050,007005000,405010708")  # multi solution A (many empty=
    sdk = loi2sdk(lst_sdk)
    print(f"Start\n{show_small(sdk)}")
    sdk, bol = r_solver(sdk)
    print(f"Done\n{show_small(sdk)}")

