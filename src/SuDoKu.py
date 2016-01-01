import logging

import SuDoKuO
#?#from pyasn1_modules.rfc2459 import CPSuri

# Sample SoDuKos from: http://www2.warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/sudoku

# Start message, and logging
str_start_message = "Start"
log = logging.getLogger('sudoku')
log.setLevel(logging.DEBUG)
log_fil = logging.FileHandler("sudoku.log", mode='w')
#log_fil.setLevel(logging.INFO)
log_fil.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')) #
log.addHandler(log_fil)
log.info(str_start_message)

### Cat 1
#s = SuDoKuO.SuDoKu("13.475269527.6941896481273.679154.23.456289712817.35464569371.27.258639489324.657") # Extremely simple

### Cat 2
#s = SuDoKuO.SuDoKu(".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..") # Suposed Easy
#s = SuDoKuO.SuDoKu("..7.1.8344..378.5.8634....192....3853..2856...81.39..2...56319.1958.7....38...527") # Supposedly very easy
#s = SuDoKuO.SuDoKu("8..317..9.9..2..7.4..8.9..5.39...71...........86..139.3..1.5..6.6..4..5.1..682..7") # Politiken 6. dec 2015, Let, Solved LG
#s = SuDoKuO.SuDoKu("3..4....2.51..7.9...9...83..9.7.8..5.........8..2.4.6..42...1...7.1..32.5....6..9") # Pol. 20. dec. '15. Let. LG

### Cat 3
#s = SuDoKuO.SuDoKu("..........65.138..21....54.....86....57.....46.......3........9....3.7..9..87.3.2")  # {Naked singles:28,Crosshatching:20,Free gifts:9}

### Cat ?
#s = SuDoKuO.SuDoKu("..46...8..39....4.81..37..6..7..4....2.....3....3..6..7..51..28.8....31..9...34..") # MX 17. dec. '15. Let. LG
#s = SuDoKuO.SuDoKu("5......1..3.5.9.......2.4....1..4...9.......8...6..2....4.8.......1.7.9..2......6") # Claimed to be simple, yet chaligsing computers

### Cat Higher
s = SuDoKuO.Slap("6.....7.3.4.8.................5.4.8.7..2.....1.3.......2.....5.....7.9......1....")
#s = SuDoKuO.SuDoKu("..8...2.4.2.....7...6..7.98..2.......8.96.....15..34...............8.5363.9....8.")
#s = SuDoKuO.SuDoKu("4.....5.8.3..........7......2.....6.....5.8......1.......6.3.7.5..2.....1.8......") # from top95
#s = SuDoKuO.SuDoKu("8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..") # Is this really the hardest-ever sudoku?
#s = SuDoKuO.SuDoKu(".......12........3..23..4....18....5.6..7.8.......9.....85.....9...4.5..47...6...") # "Platinum Blonde"
#s = SuDoKuO.SuDoKu(".....3.17.15..9..8.6.......1....7.....9...2.....5....4.......2.5..6..34.34.2.....") # 49of50
#s = SuDoKuO.SuDoKu("........8.76..8....9.....6...4..2..6..1....74.8...72..1.2..3...9...4..21..8..6.3.") # ver 0.4.0 Solves or not? 

print "Pre\n",s.show_big()
s.slap()
print "Post\n",s.show_big()
print s.stats()
log.info('Stats: '+str(s.stats()))


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
