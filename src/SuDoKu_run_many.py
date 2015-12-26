import logging
import SuDoKuO

# Start message, and logging
str_start_message = "Start"
log = logging.getLogger('sudoku')
log.setLevel(logging.DEBUG)
log_fil = logging.FileHandler("sudoku_run_many.log", mode='w')
log_fil.setLevel(logging.INFO)
log_fil.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')) #
log.addHandler(log_fil)
log.info(str_start_message)

count = 0
with open("../data/SolvedLG.txt") as f:
    for line in f:
        count += 1
        str_org_line = line.strip()
        str_sdk_line = line.split()[0]
        s = SuDoKuO.SuDoKu(str_sdk_line)
        s.slap()
        if s.solved():
            print str_org_line + ' # '+s.stats()
        else:
            print str_org_line + ' # !!! '+s.stats()