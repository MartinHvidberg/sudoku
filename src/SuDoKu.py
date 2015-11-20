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

s = SuDoKuO.SuDoKu("13........2...9......8..7..6....48....5.2...........4.....3...27..5.....8........")
print s
for i,j in s._cps_myrow(4,6):
    print s.get(i,j),
print s.myrow(4,6)
for i,j in s._cps_mycol(4, 6):
    print s.get(i,j),
print s.mycol(4,6)
for i,j in s._cps_mybox(4,6):
    print s.get(i,j),
print s.mybox(4,6)

#print s.show_solved()
print "=== pencil ==="
s._setm(3, 3, 1)
#print s.show_pencil()