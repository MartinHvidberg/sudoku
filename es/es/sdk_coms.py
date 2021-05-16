#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" The Computer Solving Classes of SuDoKu
Here we define the Computer Solving class that we use to work with SuDoKu
Focus is only on Computer friendly algorithms for solving

Not in this Class are things like human-friendly algorithms for solving, making sudokus, nor permutations or ranking.
"""

import logging

import sdk_base

__version__ = "0.0.1"

# History
# ver. 0.1.0 TBD

# create logger
logging.basicConfig(
    # format="%(asctime)s - %(levelname)s - %(message)s",  # minimum
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",  # verbose
    filename=f"{__file__.rsplit('.',1)[0]}.log",
    filemode="w",
    level=logging.INFO)  # logging.DEBUG
log = logging.getLogger(__name__)
log.info("Start!")


class SDK_coms(sdk_base.SDK_base):
    """ Computer Solving SuDoKu class """

    def __init__(self, str_ini):
        """ initialises a SuDoKu object """
        super().__init__(str_ini)
        # XXX self.p = [set() for n in range(81)] # Pencil-marks: List of set.
        # XXX self.s = list() # list of solutions, i.e. correctly solved matrix(s), format as .m
        # .s = {s=list(), single=None, multi=None}  # Solution space

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
