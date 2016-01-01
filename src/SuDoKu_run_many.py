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

count = 0 # Total
cnt_s = 0 # Solved
cnt_u = 0 # Unsloved
#with open("../data/SolvedLG.txt") as f:
with open("../data/top95.txt") as f:    
#with open("../data/1000sudoku_plain.txt") as f:    
    for line in f:
        count += 1
        str_org_line = line.strip()
        str_sdk_line = line.split()[0]
        if len(str_sdk_line) != 81:
            break # It's likely an empty line, comment ore the likes ...
        s = SuDoKuO.Slap(str_sdk_line)
        s.slap()
        if s.solved():
            cnt_s += 1
            print "4 "+s.stats()+" ("+str(count)+") "+str_org_line
        else:
            cnt_u += 1
            print "0 "+s.stats()+" ("+str(count)+") "+str_org_line

cnt_p = cnt_s*100.0/count
print "Total {0} (solved {1} unsolved {2}) = {3}%".format(count,cnt_s,cnt_u,cnt_p)