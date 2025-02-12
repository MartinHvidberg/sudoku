#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" The Computer Solving Classes of SuDoKu
Here we define the Computer Solving class that we use to work with SuDoKu
Focus is only on Computer friendly algorithms for solving

NOT in this Class are things like human-friendly algorithms for solving, making sudokus, nor permutations or ranking.

Note: The Class-hierarchy is, so far, SdkBase >> SdkComs >> SdkHums. """

import logging
import sys
import datetime

import ec_sudoku.es.sdk_base as sdk_base

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


class SdkComs(sdk_base.SdkBase):
    """ Computer Solving SuDoKu class """

    def __init__(self, str_ini):
        """ initialises a SuDoKu object """
        super().__init__(str_ini)
        # XXX self.p = [set() for n in range(81)] # Pencil-marks: List of set.
        # self.s = list() # list of solutions, i.e. correctly solved matrix(s), format as .m
        self.s = {'solu': list(), 'uniq': None}  # Solution space

    # ToDo[40] get code from cgpt02_mytwist.py over here, and make it work !!

    def solver_a(self):
        pass

    def solver_b(self):
        pass

    def is_solvable(self):
        pass

    def is_uniquesolution(self):
        pass


if __name__ == '__main__':
    #  i = '13........2...9......8..7..6....48....5.2...........4.....3...27..5.....8........'.replace('.', '0') # from99 - very slow to solve (All=True: ca. 2 min)
    #  i = '8..5.9..67..3.1..2..3...8....12.34..9...6...3..68.47....4...5..2..4.5..76..9.2..4'.replace('.','0')  # Classic - ultra quickly solved (All=True: 0:00:00.01)
    i = '9265714833514862798749235165823671941492583677631..8252387..651617835942495612738'.replace('.','0')  # double-solution (All=True: 0:00:00.0002)
    print(f"input ->: {i}")
    print("\nSolving with find all = True  (please wait...)")
    dtt_beg = datetime.datetime.now()
    o = r(i, True)
    print(f"Done: returned: {o} duration: {datetime.datetime.now() - dtt_beg}")
    print("\nSolving with find all = False")
    o = r(i, False)
    print(f"Done: returned: {o} duration: {datetime.datetime.now() - dtt_beg}")  # Newer executes because r() uses bloody sys.exit()
