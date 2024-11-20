
*** Dont use this, use /ec_sudoku/* instead ***

#!/usr/bin/env python
# -*- coding: utf-8; -*-

""" DaPr - Data Preparation
Small and big pieces of code, to prepare data from wherever, to enter the EC-software SuDoKu universe
"""

import json
import os


def txt2ecs(s_sdktxt):
    """
    Converts on line (string) with one SuDoKu in 'raw' text form
    to one d_ecs (dictionary with an EC-software SuDoKu)
    An d_ecs is essentially a dic, but with mandatory and optional fields, 
    that all have specific format rules ...
    """
    s_sdktxt = s_sdktxt.strip()
    if '#' in s_sdktxt:  # Separate in SuDoKu and Comments, the only accepted main parts
        s_sdk, s_com = [t.strip() for t in s_sdktxt.split('#', 1)]
    else:
        s_sdk, s_com = s_sdktxt.strip(), ''
    if ',' in s_sdk:  # Separate Givens from Solution, the only accepted sub-parts
        s_gvn, s_sol = [t.strip() for t in s_sdk.split(',', 1)]
    else:
        s_gvn, s_sol = s_sdk.strip(), ''
    if isinstance(s_gvn, str) and len(s_gvn) == 81:  # Make a ecs
        d_sdk = dict()
        d_sdk['gvn'] = s_gvn.replace('0', '.')
        if isinstance(s_sol, str) and len(s_sol) == 81:  # There is a solution
            d_sdk['sol'] = [s_sol]
        if isinstance(s_com, str):  # There is a comment
            d_sdk['com'] = s_com
        j_sdk = json.dumps(d_sdk)
    else:
        print(f"  Warning: Can't make sensible SuDoKu from: {s_sdktxt}")
        j_sdk = '{}'  # return empty
    ##print(f"  j: {j_sdk}")
    return j_sdk
    
    
def fileconv_txt2ecs(s_fnin, s_fnou):
    """
    Reads a 'raw' text SudoKu file, and
    writes a .ecs file
    Calls txt2ecs for the actual conversion
    """
    with open(s_fnin) as f_in:
        with open(s_fnou, 'w') as f_ou:
            for row in f_in:
                f_ou.write(str(txt2ecs(row.strip())) + '\n')


def main():
    """
    Walk a dir and convert all relevant (.txt) files to .ecs files
    """
    for root, dirs, files in os.walk("../data"):
        for name in files:
            if name.endswith('.txt'):
                s_fnin = os.path.join(root, name)
                print(s_fnin)
                s_fnou = s_fnin.replace('.txt', '.ecs')
                fileconv_txt2ecs(s_fnin, s_fnou)
            else:
                pass  # print(f"wtf: {os.path.join(root, name)}")

if __name__ == '__main__':
    main()