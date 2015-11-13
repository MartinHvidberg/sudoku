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
print s.show_solved()
print "col 4.4",s.mycol(4,4)
print "row 4.4",s.myrow(4,4)
print "box 0,0",s.mybox(0,0)
print "box 4,4",s.mybox(4,4)
print "box 8,3",s.mybox(8,3)