import logging

import SuDoKuO
#?#from pyasn1_modules.rfc2459 import CPSuri

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
#s = SuDoKuO.SuDoKu("13.475269527.6941896481273.679154.23.456289712817.35464569371.27.258639489324.657") # Extremely simple
#s = SuDoKuO.SuDoKu("..8...2.4.2.....7...6..7.98..2.......8.96.....15..34...............8.5363.9....8.")
#s = SuDoKuO.SuDoKu("..7.1.8344..378.5.8634....192....3853..2856...81.39..2...56319.1958.7....38...527") # Supposedly very easy
#s = SuDoKuO.SuDoKu("8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..") # Is this really the hardest-ever sudoku?
s = SuDoKuO.SuDoKu("8..317..9.9..2..7.4..8.9..5.39...71...........86..139.3..1.5..6.6..4..5.1..682..7") # Politiken 6. dec 2015, Let, Solved LG
print s
s.slap()
print s
print s.stats()

#===============================================================================
# print s.show_pencil()
# print s.p
# s._set(0,1,1)
# print s.show_pencil()
# print s.p
#===============================================================================

#print s.boxs()
#print s._cps_boxs()

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



