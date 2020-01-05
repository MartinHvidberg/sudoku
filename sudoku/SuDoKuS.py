
""" Solvers - Computer centric solvers
Functions that solve SuDoKus, like a computer, are located here.
These are used to confirm solvability, solutions, unique solutions, multiple solutions, etc.
"""

import logging

# Initialize logging
log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)
log_fil = logging.FileHandler(f"{__file__.rsplit('.',1)[0]}.log", mode='w')
log_fil.setFormatter(logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)s %(funcName)s] - %(levelname)s - %(message)s'))
log.addHandler(log_fil)
log.info(f"Initialise: {__file__}")

def str2loi(str_in):
    """
    Convert a string form of a SuDoKu to a list of integers
    Accept both '.' or '0' as blank, but always output blank as 0
    :param str_in: an 81 character long text string of '0',..,'9','.'
    :return: an 81 long list of 1-digit integers 0..9. On error return empty list
    """
    lst_legal_chars = list("0123456789.")
    if isinstance(str_in, str):
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


def show_small(lst_sdk):
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


def list_empty_fields_id(sdk_in):
    """ Return a list of id number (positions) for all empty cells """
    return [n for n in range(len(sdk_in)) if sdk_in[n] == 0]


def sudoku_is_solved(lst_in):
    """ Return True if the SuDoKu is full (no 0 left), otherwise False """
    return not any([n==0 for n in lst_in])


def sudoku_is_dead_end(lst_sdk, lst_pnc):
    """  Return True if the SuDoKu is in a dead-lock situation, otherwise False """
    lst_empty_fields = list_empty_fields_id(lst_sdk)
    return any([(lst_sdk[n] == 0 and len(lst_pnc[n] == 9)) for n in lst_empty_fields])


def q_solve(lst_sdk):
    """ Solves the SuDoKu
    Solves the SuDoKu using a minimal algorithm, but using a few tricks that makes it fast - I hope...
    :param lst_sdk: the input SoDuKo as a standard list of integers, length = 81
    :return:
    """

def _r_solver(lst_sdk, lst_pnc, set_sol):
    """ Recursive solver
    Go for the pencil marks... Go for the field with max pencil marks, i.e. minimum possible openings.
    Call this function (recursively) with the (few) options.
    Any branch with 9 pencil-marks to any empty cell is dead...
    :param lst_sdk: The input SoDuKo as a standard list of integers, length = 81
    :param lst_pnc: List of set() containing updated pencil marks, length = 81
    :param lst_sol: List of solutions, found until this point - can be an empty list
    :return: lst_sol. A, potentially updated, list of solutions, found until this point - can be an empty list
    """
    # Check if we have a solved SoDuKo
    if sudoku_is_solved(lst_sdk):
        set_sol.update(set(lst_sdk))
        return set_sol
    # Check if we have an empty field with no remaining options, i.e. an unsolvable situation
    if sudoku_is_dead_end(lst_sdk, lst_pnc):
        return set_sol

if __name__ == "__main__":
    lst_sdk = str2loi(".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..")
    print(show_small(lst_sdk))
    res = q_solve(lst_sdk)

