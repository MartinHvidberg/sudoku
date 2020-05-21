
import os
import datetime

import various_recusive.r1_my

def load_sudokus(str_dir):
    lst_ret = list()
    for root,dirs,files in os.walk(str_dir):
        for file in files:
            if file.endswith(".txt"):
                with open(root+os.sep+file, 'r') as fil_in:
                    for line in fil_in:
                        str_l = line.strip().split('#')[0].strip().replace('.','0')
                        if len(str_l) == 81:
                            try:
                                int_line = int(str_l)
                            except ValueError:
                                print(f"WAR: Non-integer in: {line}")
                            lst_ret.append(str_l)
                        else:
                            print(f"WAR: Wrong length {len(str_l)} in {line}")
    print(f"Found {len(lst_ret)} good lines")
    return lst_ret

def loc2aoi(str_sudoku):
    """ List of char 2 array of integer """
    #print(f"loc2aoi sdk: {type(str_sudoku)}: {str_sudoku}")
    lst_ou = list()
    for r in range(9):
        lst_in = list()
        for c in range(9):
            try:
                int_n = int(str_sudoku[r*9+c])
                lst_in.append(int_n)
            except ValueError:
                return list()  # On error, return empty list
        lst_ou.append(lst_in)
    return lst_ou

def run_r1(lst_s_l):
    for str_sdk in lst_s_l:
        aoi_sdk = loc2aoi(str_sdk)
        dtm_start = datetime.datetime.now()
        bol_sol = various_recusive.r1_my.main(aoi_sdk)
        dur_sol = datetime.datetime.now() - dtm_start
        print(f"r1: {str_sdk.replace('0','.')} sol: {bol_sol} in {round(dur_sol.total_seconds()*1000)} ms")


def run_all_solvers(lst_s):
    #print(f"all sudokus: {type(lst_s)}: {lst_s}")
    run_r1(lst_s)

if __name__ == "__main__":
    lst_sudokus = load_sudokus(r"../data/speed")
    #print(lst_sudokus)
    run_all_solvers(lst_sudokus)