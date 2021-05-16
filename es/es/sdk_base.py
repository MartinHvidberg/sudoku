#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" The Base Classes of SuDoKu
Here we define the basic class that we use to work with SuDoKu
Focus in on cells and their values - only, like
getting and setting values in cells.
Include validation of the SuDoKu, like is it valid, is it completed?
Extract lists of cell-references (CXS) and/or cell-values for rows and cols,
and relatively like: all other cells in this col., etc.

Not in the Base Class is things like pencil-marks, solving and solubility, permutations and ranking.
"""

import logging
import string

__version__ = "0.0.1"

# create logger
logging.basicConfig(
    # format="%(asctime)s - %(levelname)s - %(message)s",  # minimum
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",  # verbose
    filename=f"{__file__.rsplit('.',1)[0]}.log",
    filemode="w",
    level=logging.INFO)  # logging.DEBUG
log = logging.getLogger(__name__)
log.info("Start!")


class SDK_base(object):
    """ Base SuDoKu class """

    def __init__(self, str_ini):
        """ initialises a SuDoKu object """
        self.g = ''.join([81*'0'])  # Givens: Text string of 81 chr. The original input, saved for reference
        self.m = [[0 for k in range(9)] for l in range(9)]  #  Matrix: list of 9 lists of 9 int = 9x9 matrix of [l][k]
        # OLD self.m = [int(itm) for itm in self.g]  # Matrix: list of int - To be gradually manipulated towards solutions
        # XXX self.p = [set() for n in range(81)] # Pencil-marks: List of set.
        # XXX self.s = list() # list of solutions, i.e. correctly solved matrix(s), format as .m
        # .s = {s=list(), single=None, multi=None}  # Solution space
        self.v = True  # Valid: Boolean - The SuDoKu is valid (empty is also valid)
        # Fill the .g and .m if input data is provided
        if len(str_ini) == 0:
            pass # leaving the sudoku empty ...
        elif len(str_ini) == 81:
            self.g = str_ini.replace('.', '0') # Backup the original (init) givens, in string form
            log.info(f"Input: {str_ini}")  # We allow '.' for empty in the raw input
            for n in range(len(self.g)):
                k, l = self.n2kl(n)
                v = self.g[n]
                self.set(k, l, v)
            # XXX self.validate() # Validate that the fill is legal

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

        else:
            log.error("#101 > SuDoKu Object can't create, because ini string do not have length 0 or 81.")

    # transform between n (all 81 in one [0..80] order), and k, l (the array 9x9 matrix order)

    def n2kl(self, n):
        k, l = n % 9, n // 9
        # print(f"n: {n} => k,l: {k},{l}")
        return k, l

    # Validity function(s)

    def is_valid(self):
        self.validate()
        return self.v

    def validate(self):
        # Check if Valid
        bol_val_1 = all([(isinstance(itm, int) and 0 <= itm <= 9) for itm in self.m])  # all single digit int
        bol_val_2 = all([len(area) == len(list(set(area))) for area in self.areas()])  # no duplicates
        self.v = all([bol_val_1, bol_val_2])

    # Basic functions (get, set)

    def get(self, k=None, l=None):
        """ get a cell or a column (k) or a line (l) or all 81 values in the matrix """
        if k != None and l != None:
            return self.m[l][k]
        elif l != None:
            return self.m[l]
        elif k != None:
            return 'k'
        else:
            return self.m

    def set(self, k, l, value):
        """ set (insert) the value at position coll=k, line=l, if it is legal
        Return true on successful insertion, otherwise False, """
        # Convert v from str to int, if needed ...
        if isinstance(value, str) and len(value) == 1 and '0123456789'.find(value) >= 0:
            value = int(value)
        log.info(f"set(); set({k},{l}, {value})")
        if all([isinstance(itm, int) for itm in [k, l, value]]):
            if all([0 <= itm <= 9 for itm in [k, l, value]]):
                if value == 0 or value not in self.this_row(k, l):
                    if value == 0 or value not in self.this_col(k, l):
                        if value == 0 or value not in self.this_box(k, l):
                            self.m[l][k] = value  # Yes the raw m has index order [l][k]
                            # log.info(f"------ k,l: {k},{l}, v: {value}")
                            # log.info(f"\n{self.show_small()}")
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

    # CPS functions - returning various listes of Coordinate PairS

    def cps_this_row(self,k,l):
        """ Return list of cps representing the row that (k,l) belongs to """
        return [(i, l) for i in range(9)]

    def cps_this_col(self,k,l):
        """ Return list of cps (coordinate pairs), representing the col that (k,l) belongs to """
        return [(k, i) for i in range(9)]
    
    def cps_this_box(self,k,l):
        """ Return list of cps (coordinate pairs), representing the box that (k,l) belongs to """
        kk = (k//3)*3
        ll = (l//3)*3
        bx = [(kk+j, ll+i) for i in range(3) for j in range(3)]
        ##print(f"kk: {kk}, ll: {ll}, bx: {bx}")
        return bx


    # Extraction part of the SuDoKu functions (area, col, row, box)

    def this_row(self,k,l):
        """ Return list of digits, representing the row that (k,l) belongs to """
        return self.m[l] # Not using ._cps_ since this is simpler and faster

    def this_col(self,k,l):
        """ Return list of digits, representing the col that (k,l) belongs to """
        #ret = [itm[k] for itm in self.m] # Not using .cps_ ???
        cps = self.cps_this_col(k, l)
        ret = [self.get(kk, ll) for kk, ll in cps]
        ##print(f"this_col(); k: {k}, l: {l}, cps: {cps}, ret: {ret}")
        return ret

    def this_box(self,k,l):
        """ Return list of digits, representing the box that (k,l) belongs to """
        return [self.get(i,j) for i,j in self.cps_this_box(k,l)]

    def rows(self):
        """ Return a list of lists of int, representing all rows in the SuDoKu """
        return self.m  # Not using ._cps_ since this is simpler and faster

    def cols(self):
        """ Return a list of lists of int, representing all cols in the SuDoKu """
        return [self.this_col(1,i) for i in range(9)]

    def boxs(self):
        """ Return a list of lists of int, representing all boxes in the SuDoKu """
        return [self.this_box(i*3,j*3) for i in range(3) for j in range(3)]

    def areas(self):
        """ Return a list of lists of int, representing all rows, cols and boxes in the SuDoKu """
        return self.rows()+self.cols()+self.boxs()

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
    print("  -= This module can not be run, but must be called =- ")