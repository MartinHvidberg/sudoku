import logging

import SuDoKuO

# Sample SoDuKos from: http://www2.warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/sudoku

# Start message, and logging
str_start_message = "Start"
log = logging.getLogger('sudoku')
log.setLevel(logging.DEBUG)
log_fil = logging.FileHandler("sudoku.log", mode='w')
log_fil.setLevel(logging.INFO)
log_fil.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')) #
log.addHandler(log_fil)
log.info(str_start_message)

s = SuDoKuO.SuDoKu("131.......2...9......8..7..6....48....5.2...........4.....3...27..5.....8........")
print s
print "rows"
for r in s.rows():
    print r
print "cols"
for c in s.cols():
    print c
print "boxs"
for b in s.boxs():
    print b
print s.show_solved()
print "=== pencil ==="
#print s.show_pencil()
