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

#s = SuDoKuO.SuDoKu("13........2...9......8..7..6....48....5.2...........4.....3...27..5.....8........")
#s = SuDoKuO.SuDoKu("13.475269527.6941896481273.679154.23.456289712817.35464569371.27.258639489324.657")
s = SuDoKuO.SuDoKu("8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..") # Is this really the hardest-ever sudoku?
print s
print s.boxs()
print s._cps_boxs()
#print s.show_solved()

#===============================================================================
# print " a row (horizontal)"
# for i,j in s._cps_this_row(4,6):
#     print s.get(i,j),
# print s.this_row(4,6)
# print " a col (vertical)"
# for i,j in s._cps_this_col(4, 6):
#     print s.get(i,j),
# print s.this_col(4,6)
# print " a box (you know)"
# for i,j in s._cps_this_box(4,6):
#     print s.get(i,j),
# print s.this_box(4,6)
#===============================================================================



