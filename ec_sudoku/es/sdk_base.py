#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" The Base Classes of SuDoKu
Here we define the basic class that we use to work with SuDoKu
Focus is only on cells and their values:
- Getting and setting values in cells.
- Include validation of the SuDoKu, like is it valid, is it completed?
- Extract lists of cell-references (cps) and/or cell-values for rows and cols,
- and relatively like: all other cells in this col., etc.

NOT in the Base Class is things like pencil-marks, solving and solubility, permutations and ranking.
"""

import logging
# import string

__version__ = "0.1.1"

# History
# ver. 0.1.0 sdk_base & test_sdk_base implemented
# ver. 0.1.1 fixed bug in is_complete()

# create logger
logging.basicConfig(
    # format="%(asctime)s - %(levelname)s - %(message)s",  # minimum
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",  # verbose
    filename="sdk_base.log",
    filemode="w",
    level=logging.INFO)  # logging.DEBUG
logbase = logging.getLogger("sdk_base")
logbase.info("sdk_base: Start!")


class SdkBase(object):
    """ Base SuDoKu class

    Note: The Class-hierarchy is, so far, SdkBase >> SdkComs >> SdkHums. """

    def __init__(self, str_ini):
        """ initialises a SuDoKu object """
        self.g = ''.join([81*'0'])  # Givens: Text string of 81 chr. The original input, saved for reference
        self.m = [[0 for k in range(9)] for l in range(9)]  #  Matrix: list of 9 lists of 9 int = 9x9 matrix of [l][k]
        self.v = True  # Valid: Boolean - The SuDoKu is valid (empty is also valid)
        # Fill the .g and .m if input data is provided
        if len(str_ini) == 0:
            pass  # leaving the sudoku empty ...
        elif len(str_ini) == 81:
            self.load_str(str_ini)
        else:
            logbase.error("#101 > SuDoKu Object can't create, because ini string do not have length 0 or 81.")

    # transform between n (all 81 in one [0..80] order), and k, l (the array 9x9 matrix order)

    def n2kl(self, n):
        k, l = n % 9, n // 9
        # print(f"n: {n} => k,l: {k},{l}")
        return k, l

    # ToDo [] Do we also need an kl2n()

    # Validity and completeness function(s)

    def is_valid(self):
        self.validate()
        return self.v

    def validate(self):
        # Check if Valid
        bol_val_1 = all([[(isinstance(itm, int) and 0 <= itm <= 9) for itm in line] for line in self.m])  # all single digit int
        bol_val_2 = all([len(area) == len(list(set(area))) for area in self.areas()])  # no duplicates
        self.v = all([bol_val_1, bol_val_2])

    def is_complete(self):
        if self.is_valid():
            for l in range(9):
                for k in range(9):
                    if self.m[l][k] == 0:
                        return False
            return True  # It's valid, and holds no more zeros
        else:
            return False

    # Basic functions (get, set, get_matrix, set_matrix, load_str, dump_str, ...)

    def get_matrix(self):
        """ returns the entire SoDuKo as a LOL
            primarily to avoid other functions to access self.m directly """
        return self.m

    def set_matrix(self, lol_m):
        """ Inserts (overwrites) the self.m SoDuKo with the given LOL
            primarily to avoid other functions to access self.m directly """
        # ToDo[] There should be some serious testing here...
        self.m = lol_m

    def get(self, k=None, l=None):
        """ get a cell or a column (k) or a line (l) or all 81 values in the matrix """
        if k is not None and l is not None:
            return self.m[l][k]
        elif l is not None:
            return self.m[l]
        elif k is not None:
            return 'k'
        else:
            return self.m

    def set(self, k, l, value):
        """ set (insert) the value at position coll=k, line=l, if it is legal
        Return true on successful insertion, otherwise False, """
        # Convert v from str to int, if needed ...
        if isinstance(value, str) and len(value) == 1 and '0123456789'.find(value) >= 0:
            value = int(value)
        logbase.info(f"set(); set({k},{l}, {value})")
        if all([isinstance(itm, int) for itm in [k, l, value]]):
            if all([0 <= itm <= 9 for itm in [k, l, value]]):
                if value == 0 or value not in self.this_row(k, l):
                    if value == 0 or value not in self.this_col(k, l):
                        if value == 0 or value not in self.this_box(k, l):
                            self.m[l][k] = value  # Yes the raw m has index order [l][k]
                            # logbase.info(f"------ k,l: {k},{l}, v: {value}")
                            # logbase.info(f"\n{self.show_small()}")
                            return True
                        else:
                            # ToDo: Change these to non-terminating actions, like return False, this is too destructive.
                            # raise UserWarning(f"Trying to set() value: {value}, all ready in Box: {self.m}")
                            return False
                    else:
                        # raise UserWarning(f"Trying to set() value: {value}, all ready in Col: {self.m}")
                        return False
                else:
                    # raise UserWarning(f"Trying to set() value: {value} @ k,l = {k, l}, all ready in Row: {self.m}")
                    return False
            else:
                # raise UserWarning(f"Trying to set() value: {value} @ k,l = {k, l}. One of them is not in [0..9]")
                return False
        else:
            # raise UserWarning(f"Trying to set() value: {value} @ k,l = {k, l}. One of them is not an integer")
            return False
        # ToDo: insert validate() here, but remove it before production, for better performance.

    def load_str(self, str_in):
        """ Read a string of 81 digits, and fill the SuDoKu """
        self.g = str_in.replace('.', '0')  # Backup the original (in) givens, in string form
        logbase.info(f"Load SuDoKu from string: {str_in}")  # We allow '.' for empty in the raw input
        for n in range(len(self.g)):
            k, l = self.n2kl(n)
            v = self.g[n]
            self.set(k, l, v)
        return self.is_valid()

    def dump_str(self):
        lst_ret = list()
        for row in self.rows():
            lst_ret.extend([str(c) for c in row])  # ToDo[10] Can this be turned into a 1-liner?
        return "".join(lst_ret)

    # CPS functions - returning various lists of Coordinate PairS

    def cps_this_row(self, k, l):
        """ Return list of cps (coordinate pairs) representing the row that (k,l) belongs to """
        return [(i, l) for i in range(9)]

    def cps_this_col(self, k, l):
        """ Return list of cps (coordinate pairs), representing the col that (k,l) belongs to """
        return [(k, i) for i in range(9)]
    
    def cps_this_box(self, k, l):
        """ Return list of cps (coordinate pairs), representing the box that (k,l) belongs to """
        kk = (k//3)*3
        ll = (l//3)*3
        bx = [(kk+j, ll+i) for i in range(3) for j in range(3)]
        ##print(f"kk: {kk}, ll: {ll}, bx: {bx}")
        return bx

    # Extraction part of the SuDoKu functions (area, col, row, box)

    def this_row(self, k, l):
        """ Return list of digits, representing the row that (k,l) belongs to """
        return self.m[l] # Not using ._cps_ since this is simpler and faster

    def this_col(self, k, l):
        """ Return list of digits, representing the col that (k,l) belongs to """
        cps = self.cps_this_col(k, l)
        ret = [self.get(kk, ll) for kk, ll in cps]
        return ret

    def this_box(self, k, l):
        """ Return list of digits, representing the box that (k,l) belongs to """
        return [self.get(i, j) for i, j in self.cps_this_box(k,l)]

    def rows(self):
        """ Return a list of lists of int, representing all rows in the SuDoKu """
        return self.m  # Not using ._cps_ since this is simpler and faster

    def cols(self):
        """ Return a list of lists of int, representing all cols in the SuDoKu """
        return [self.this_col(k,0) for k in range(9)]

    def boxs(self):
        """ Return a list of lists of int, representing all boxes in the SuDoKu """
        return [self.this_box(k*3, l*3) for l in range(3) for k in range(3)]

    def areas(self):
        """ Return a list of lists of int, representing all rows, cols and boxes in the SuDoKu """
        return self.rows() + self.cols() + self.boxs()

    # Show - convert to print friendly string

    def show_small(self):

        def p(i, j):
            return str(self.m[i][j])

        def l(i):
            return ("|" + p(i, 0) + p(i, 1) + p(i, 2) + "|" + p(i, 3) + p(i, 4) + p(i, 5) + "|" + p(i, 6) + p(i, 7) + p(i, 8) + "|\n").replace('0', ' ')

        def q():
            v = '+---+---+---+\n'
            return (v + l(0) + l(1) + l(2) + v + l(3) + l(4) + l(5) + v + l(6) + l(7) + l(8) + v).strip()

        return q()


if __name__ == '__main__':
    print("  -= This module (sdk_base) can not be run, but must be called =- ")