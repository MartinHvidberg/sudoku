#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" The Permutation Classes of SuDoKu
Here we work with SuDoKu permutations, i.e. SuDoKu's that look different but are the same, but is rotated or mirrored
Focus is only on Permutations and on the so called Normal-permutation:
- Converting any SuDoKu to its normal form
- Generating the SuDoKu ID based on the permutation
- Generating permutations of a SuDoKu

NOT in the Permutation Class is things like Ranking

Note: This module do not extend the SoDuKo class, but works with it
    The Class-hierarchy is, so far, SdkBase >> SdkComs >> SdkHums. """

import logging

import sdk_hums

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


# def flip_h(sdk):  - Old, non-cloning version
#     """ Flip the matrix - horizontally """
#     # lst_t = sdk.get_matrix()
#     # lst_fh = [lst_v[::-1] for lst_v in lst_t]
#     # sdk.set_matrix(lst_fh)
#     sdk.set_matrix([lst_v[::-1] for lst_v in sdk.get_matrix()])
#     return sdk


def flip_h(sdk_in):
    """ Flip the matrix - horizontally
        No return a deep-copy """
    sdk_ou = sdk_hums.SdkHums("")
    sdk_ou.set_matrix([lst_v[::-1] for lst_v in sdk_in.get_matrix()])
    return sdk_ou


# def flip_v(sdk):  - Old, non-cloning version
#     """ Flip the matrix - vertically """
#     # lst_t = sdk.get_matrix()
#     # lst_fv = lst_t[::-1]
#     # sdk.set_matrix(lst_fv)
#     sdk.set_matrix(sdk.get_matrix()[::-1])
#     return sdksdk_ou


def flip_v(sdk_in):
    """ Flip the matrix - vertically
        No return a deep-copy """
    sdk_ou = sdk_hums.SdkHums("")
    sdk_ou.set_matrix(sdk_in.get_matrix()[::-1])
    return sdk_ou


# def turn_r(sdk):  - Old, non-cloning version
#     """ Turn the maxrix 90 degrees - right """
#     # # self.m = [col[::-1] for col in self.cols()]  # old OOP based version
#     lst_tr = [col[::-1] for col in sdk.cols()]
#     sdk.set_matrix(lst_tr)
#     return sdk

def turn_r(sdk_in):
    """ Turn the maxrix 90 degrees - right
        No return a deep-copy """
    sdk_ou = sdk_hums.SdkHums("")
    lst_tr = [col[::-1] for col in sdk_in.cols()]
    sdk_ou.set_matrix(lst_tr)
    return sdk_ou


# def turn_l(sdk):  - Old, non-cloning version
#     """ Turn the maxrix 90 degrees - left """
#     # # self.m = [col for col in self.cols()][::-1]  # old OOP based version
#     lst_tl = [col for col in sdk.cols()][::-1]
#     sdk.set_matrix(lst_tl)
#     return sdk


def turn_l(sdk_in):
    """ Turn the maxrix 90 degrees - left """
    sdk_ou = sdk_hums.SdkHums("")
    lst_tl = [col for col in sdk_in.cols()][::-1]
    sdk_ou.set_matrix(lst_tl)
    return sdk_ou


def permute(self):  # XXX Should rather be called something_normalize... XXX    # old OOP based version
    """ Permute the matrix - so the order become 123456789 """
    str_alpha = "abcdefghi."
    str_numrc = "123456789."

    str_org = self.show_line()
    str_origi = str()
    for str_c in str_org.replace('.', ''):
        if not str_c in str_origi:
            str_origi += str_c
    # print "local order: {}".format(str_origi)
    trantab = str.maketrans(str_origi + '.', str_alpha)
    str_a = str_org.translate(trantab)
    trantab = str.maketrans(str_alpha, str_numrc)
    str_p = str_a.translate(trantab)
    self.m = [[int(str_p[j * 9 + i].replace('.', '0')) for i in range(9)] for j in range(9)]
    self.clean_all_but_m()
    return


def normalize(sdk):
    """ Takes a SoDuKo and calculates its normal form.
        returns the normal form """

