
*** Dont use this, use /ec_sudoku/* instead ***

#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" SuDoKu Common - Part of ECsoftware SuDoKu
    Contains common functions, that can be called from several other modules
    So far mainly som printing functions, e.i., some sdk to text functions

    Assuming that a sdk is simply an 81 char long list of int, and empty cells are 0 """


def sdk_lst2str(lst_in):
    """ Converts a sdk from its list to its string format """
    return "".join(lst_in)


def sdk_str2lst(str_in):
    """ Converts a sdk from its string to its list format """
    return list(str_in)


def set_empty_to_zero(lst_in):
    """ Set any char that is not [1..9] to 0 """
    set_valid_char = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    return [c if c in set_valid_char else "0" for c in lst_in]


def show_small_i(lst_sdk):
    """ Show the SoDuKo in 2D
    Return a string version for print, with a minimalistic design, of the SoDuKo in the lst_sdk
    :param lst_sdk: the input SoDuKo as a standard list of integers, length = 81
    :return: a (multi-line) string with the SoDuKo in 2D design
    """

    def p(i, j):
        return str(lst_sdk[(i * 9) + j])

    def l(i):
        return f"|{p(i, 0)}{p(i, 1)}{p(i, 2)}|{p(i, 3)}{p(i, 4)}{p(i, 5)}|{p(i, 6)}{p(i, 7)}{p(i, 8)}|\n"

    def q():
        v = '+---+---+---+\n'
        return f"{v}{l(0)}{l(1)}{l(2)}{v}{l(3)}{l(4)}{l(5)}{v}{l(7)}{l(8)}{v}"

    return q()
