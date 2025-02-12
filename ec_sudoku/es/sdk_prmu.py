#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" The Permutation Classes of SuDoKu
Here we work with SuDoKu permutations, i.e. SuDoKu's that look different but are the same, e.g. is rotated or mirrored
Focus is only on Permutations and on the so called Normal-permutation:
- Converting any SuDoKu to its normal form
- Generating the SuDoKu ID based on the permutation
- Generating permutations of a SuDoKu

NOT in the Permutation Class is things like Ranking

ToDo[20] Consider if this should be a class, and where in the hierarchy it would best be placed. Should it follow Base?
Note: This module do not extend the SoDuKo class, but works with it
    The Class-hierarchy is, so far, SdkBase >> SdkComs >> SdkHums. """

import logging

import ec_sudoku.es.sdk_hums as sdk_hums

__version__ = "0.0.1"

# History
# ver. 0.0.1 sdk_prmu & test_sdk_prmu initialised

# create logger
logging.basicConfig(
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",  # verbose
    filename="sdk_prmu.log",
    filemode="w",
    level=logging.INFO)  # logging.DEBUG
logbase = logging.getLogger("sdk_prmu")
logbase.info("sdk_prmu: Start!")


def flip_h(sdk_in):
    """ Flip the matrix - horizontally
        No return a deep-copy """
    sdk_ou = sdk_hums.SdkHums("")
    sdk_ou.set_matrix([lst_v[::-1] for lst_v in sdk_in.get_matrix()])
    return sdk_ou


def flip_v(sdk_in):
    """ Flip the matrix - vertically
        No return a deep-copy """
    sdk_ou = sdk_hums.SdkHums("")
    sdk_ou.set_matrix(sdk_in.get_matrix()[::-1])
    return sdk_ou

def turn_r(sdk_in):
    """ Turn the maxrix 90 degrees - right
        No return a deep-copy """
    sdk_ou = sdk_hums.SdkHums("")
    lst_tr = [col[::-1] for col in sdk_in.cols()]
    sdk_ou.set_matrix(lst_tr)
    return sdk_ou


def turn_l(sdk_in):
    """ Turn the maxrix 90 degrees - left """
    sdk_ou = sdk_hums.SdkHums("")
    lst_tl = [col for col in sdk_in.cols()][::-1]
    sdk_ou.set_matrix(lst_tl)
    return sdk_ou


def permute(sdk_in, str_fr="0123456789", str_to="0123456789"):  # XXX Should rather be called something_normalize... XXX    # old OOP based version
    """ Permute the matrix
        Given the 'from' and 'to' (strings str_fr, str_to), which each holds the digits 0..9
        Any input occurrence of first digit in str_fr is replaced with first digit in str_to, and so forth
        str_fr (and/or str_to) can be skipped if its "0123456789", which is often the case """
    # ToDo[24] Check valisity of str_fr and str_to
    str_t0 = "abcdefghij"  # temporary string that holds 10 unique, no digital, chars...
    dic_t1 = dict(zip(list(str_fr), list(str_t0)))  # defining 1'st translation fr->t0
    dic_t2 = dict(zip(list(str_t0), list(str_to)))  # defining 2'nd translation t0->to
    str_in = sdk_in.dump_str()  # get the input sdk in string format
    str_ab = str_in.translate(str.maketrans(dic_t1))  # 1'st translation
    str_ou = str_ab.translate(str.maketrans(dic_t2))  # 2'nd translation
    sdk_ou = sdk_hums.SdkHums("")  # create a new clone of a SDK
    sdk_ou.load_str(str_ou)  # load the resulting output values
    return sdk_ou


def make8frmu(sdk_in):
    """ From a given SuDoKu
        Create all the 8 possible figure-permutations,
        i.e. all the permutations that can be created with turn- and flip-operations
        Return them in order, as a list, ensuring that the normal-figure is number 0
        """
    set_8 = set()
    set_8.add(sdk_in.dump_str())
    # print(f"\nTopLeft - Vert\n{sdk_in.show_small()}")
    sdk_in = turn_l(sdk_in)
    set_8.add(sdk_in.dump_str())
    # print(f"\nLowerLeft - Hori\n{sdk_in.show_small()}")
    sdk_in = turn_l(sdk_in)
    set_8.add(sdk_in.dump_str())
    # print(f"\nLowerRight - Vert\n{sdk_in.show_small()}")
    sdk_in = turn_l(sdk_in)
    set_8.add(sdk_in.dump_str())
    # print(f"\nTopRight - Hori\n{sdk_in.show_small()}")
    sdk_in = flip_v(sdk_in)
    sdk_in = turn_l(sdk_in)
    set_8.add(sdk_in.dump_str())
    # print(f"\nTopRight - Vert\n{sdk_in.show_small()}")
    sdk_in = turn_r(sdk_in)
    set_8.add(sdk_in.dump_str())
    # print(f"\nLowerRight - Hori\n{sdk_in.show_small()}")
    sdk_in = turn_r(sdk_in)
    set_8.add(sdk_in.dump_str())
    # print(f"\nLowerLeft - Vert\n{sdk_in.show_small()}")
    sdk_in = turn_r(sdk_in)
    set_8.add(sdk_in.dump_str())
    # print(f"\nTopLeft - Hori\n{sdk_in.show_small()}")

    lst_tup = list()
    for perm in set_8:
        str_fig = ''.join([str(int(c != '.')) for c in perm])  # building the 'figure' as 0 and 1 string
        lst_tup.append((str_fig, perm))
    lst_tup = sorted(lst_tup)
    return [tup[1] for tup in lst_tup]  # return only the permutations, but in figure-sorting order
    # return lst_tup  # return both the figures and permutations, in figure-sorting order


def transpose(sdk):
    """

    """


def normalize(sdk):
    """ Takes a SoDuKo and calculates its normal form.
        returns the normal form
        Plan:
        - generate the 8 figures and find the 1'st
        - transpose that permutation to numerical order [01234...9]
        return that (and maybe the name of it, as well as the name of the input?
        """
    sdk_f0 = make8frmu(sdk)[0]
    sdk_f0t0 = transpose(sdk_f0)


