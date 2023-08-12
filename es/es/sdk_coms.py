#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" The Computer Solving Classes of SuDoKu
Here we define the Computer Solving class that we use to work with SuDoKu
Focus is only on Computer friendly algorithms for solving

NOT in this Class are things like human-friendly algorithms for solving, making sudokus, nor permutations or ranking.
"""

import logging
import sys
import datetime

import sdk_base

__version__ = "0.0.1"

# History
# ver. 0.1.0 TBD

# create logger
logging.basicConfig(
    # format="%(asctime)s - %(levelname)s - %(message)s",  # minimum
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",  # verbose
    filename="sdk_coms.log",
    filemode="w",
    level=logging.INFO)  # logging.DEBUG
logcoms = logging.getLogger("sdk_coms")
logcoms.info("sdk_coms: Start!")


# THIS BLOODY WORKS SO DON'T MESS IT UP - Though it's a shitty implementation that doesn't return anything meaningful.

def same_row(i_l, j_l):
    return i_l // 9 == j_l // 9


def same_col(i_l, j_l):
    return (i_l - j_l) % 9 == 0


def same_block(i_l, j_l):
    return i_l // 27 == j_l // 27 and i_l % 9 // 3 == j_l % 9 // 3


def r(a, find_all=False):
    i_l = a.find('0')
    if i_l == -1:
        if find_all:
            print(f"solution: {a}")
            return True
        else:
            print(f"solution: {a}")
            sys.exit(999)

    excluded_numbers = set()
    for j in range(81):
        if same_row(i_l, j) or same_col(i_l, j) or same_block(i_l, j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
            # At this point, m is not excluded by any row, column, or block, so let's place it and recurse
            r(a[:i_l] + m + a[i_l + 1:], find_all)

# ----------------------------------------------------------------------------------------------------------------------


class SDK_coms(sdk_base.SdkBase):
    """ Computer Solving SuDoKu class """

    def __init__(self, str_ini):
        """ initialises a SuDoKu object """
        super().__init__(str_ini)
        # XXX self.p = [set() for n in range(81)] # Pencil-marks: List of set.
        # self.s = list() # list of solutions, i.e. correctly solved matrix(s), format as .m
        self.s = {'solu': list(), 'uniq': None}  # Solution space

        # # ToDo: Move this part to sdk_coms, where we have a solver.
        # if self.v: # If it's valid, so far, check if it's solvable
        #     try:
        #         # ToDo: This is doubtful - do the solver run x81 times? and what exactly do we prove here?
        #         self.solution = [[int(SuDoKuX.sudoku99_NEW_XXX_(str_ini)[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)] # Solve using brute force, to see if solution(s) exist
        #         log.info("Input is Solvable, but was not checked for uniqueness...")
        #     except:
        #         self.solution = self.m # If not solvable, keep the init values to avoid a Null variable.
        #         self.v = False # It looked valid, but it's not ...
        #         log.warning("Input is NOT Solvable...")
        # if self.v: # If it's valid, and also is solvable
        #     self.pencil() # Fill in the pencil marks, for the valid, solvable, init matrix

    def solver_a(self):
        pass

    def solver_b(self):
        pass

    def is_solvable(self):
        pass

    def is_uniquesolution(self):
        pass


if __name__ == '__main__':
    i = '13........2...9......8..7..6....48....5.2...........4.....3...27..5.....8........'.replace('.', '0') # from99 - very slow to solve (All=True: 0:02:08)
    #  i = '8..5.9..67..3.1..2..3...8....12.34..9...6...3..68.47....4...5..2..4.5..76..9.2..4'.replace('.','0')  # Classic - ultra quickly solved (All=True: 0:00:00.01)
    #  i = '9265714833514862798749235165823671941492583677631..8252387..651617835942495612738'.replace('.','0')  # double-solution (All=True: 0:00:00.0002)
    print(f"input ->: {i}")
    print("\nTrue")
    dtt_beg = datetime.datetime.now()
    o = r(i, True)
    print(f"o: {o} duration: {datetime.datetime.now() - dtt_beg}")
    print("\nFalse")
    o = r(i, False)
    print(f"o: {o} duration: {datetime.datetime.now() - dtt_beg}")  # Newer executes because r() uses bloody sys.exit()
