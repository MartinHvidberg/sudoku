
import os
import datetime
import logging

import various_recusive.r1_my
import various_recusive.r2_my

logging.basicConfig(
    # format="%(asctime)s - %(levelname)s - %(message)s",  # minimum
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",  # verbose
    filename="speed_comp_others.log",
    filemode="w",
    level=logging.DEBUG)
log = logging.getLogger(__name__)

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

def aoi2loc(aoi_in):
    """ Array of integer 2 list of char """
    str_ret = str()
    for r in aoi_in:
        for c in r:
            str_ret += str(c)
    return str_ret

def run_r1(lst_s_l):
    for str_sdk in lst_s_l:
        # format input
        aoi_sdk = loc2aoi(str_sdk)
        # run SuDoKu
        dtm_start = datetime.datetime.now()  # ---->
        aoi_ret = various_recusive.r1_my.main(aoi_sdk)
        dur_sol = datetime.datetime.now() - dtm_start  # <----
        # format output
        loc_res = aoi2loc(aoi_ret)
        str_report = f"\n# r1 >> {str_sdk.replace('0','.')} << {loc_res} : in {round(dur_sol.total_seconds()*1000)} ms "
        log.info(str_report)

def run_r2(lst_s_l):
    for str_sdk in lst_s_l:
        # run SuDoKu
        dtm_start = datetime.datetime.now()  # ---->
        aoi_ret = various_recusive.r2_my.main(str_sdk)
        dur_sol = datetime.datetime.now() - dtm_start  # <----
        # format output
        # format output
        loc_res = aoi2loc(aoi_ret)
        str_report = f"\n# r2 >> {str_sdk.replace('0','.')} << {loc_res} : in {round(dur_sol.total_seconds()*1000)} ms "
        log.info(str_report)

def run_all_solvers(lst_s):
    log.info("run_all_solvers(lst_s)")
    run_r1(lst_s)
    run_r2(lst_s)

if __name__ == "__main__":
    lst_sudokus = load_sudokus(r"../data/speed")
    #print(lst_sudokus)
    run_all_solvers(lst_sudokus)