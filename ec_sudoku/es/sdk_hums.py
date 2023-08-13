#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" The Human Solving Classes of SuDoKu
Here we define the Human Solving class that we use to work with SuDoKu
Focus is only on Human friendly algorithms for solving

NOT in this Class are things like computer-friendly algorithms for solving, making sudokus, nor permutations or ranking.

Note: The Class-hierarchy is, so far, SdkBase >> SdkComs >> SdkHums. """

import logging

import ec_sudoku.es.sdk_coms as sdk_coms

__version__ = "0.0.1"

# History
# ver. 0.0.1 TBD

# create logger
logging.basicConfig(
    # format="%(asctime)s - %(levelname)s - %(message)s",  # minimum
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",  # verbose
    filename="sdk_hums.log",
    filemode="w",
    level=logging.INFO)  # logging.DEBUG
logcoms = logging.getLogger("sdk_hums")
logcoms.info("sdk_hums: Start!")


class SdkHums(sdk_coms.SdkComs):
    """ Human Solving SuDoKu class """

    def __init__(self, str_ini):
        """ initialises a SuDoKu object """
        super().__init__(str_ini)