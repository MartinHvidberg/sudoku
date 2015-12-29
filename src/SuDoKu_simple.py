#http://pythontips.com/2013/09/01/sudoku-solver-in-python/

import sys

def same_row(i,j): return (i/9 == j/9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i/27 == j/27 and i%9/3 == j%9/3)

def r(a):
    i = a.find('0')
    if i == -1:
        print 'SOLVED: ', a
        #sys.exit(a)

    excluded_numbers = set()
    for j in range(81):
        if same_row(i,j) or same_col(i,j) or same_block(i,j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
            r(a[:i]+m+a[i+1:])

if __name__ == '__main__':
    if len(sys.argv) == 2 and len(sys.argv[1]) == 81:
        r(sys.argv[1])
    else:
        print 'Usage: python sudoku.py puzzle'
        print '    where puzzle is an 81 character string representing the puzzle read left-to-right, top-to-bottom, and 0 is a blank'
        #r('13........2...9......8..7..6....48....5.2...........4.....3...27..5.....8........'.replace('.','0'))
        r('.......12........3..23..4....18....5.6..7.8.......9.....85.....9...4.5..47...6...'.replace('.','0')) # Platinum Blonde
        #r('138475269.2...9......8..7..6....48....5.2...........4.....3...27..5.....8........'.replace('.','0'))
        #r('8..6..9.5.............2.31...7318.6.24.....73...........279.1..5...8..36..3......'.replace('.','0')) # This is known to have 5 solutions