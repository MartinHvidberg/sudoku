import sys

def same_row(i,j): return (i/9 == j/9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i/27 == j/27 and i%9/3 == j%9/3)


def r(a):
    i = a.find('0')
    if i == -1:
        sys.exit(a)

    excluded_numbers = set()
    for j in range(81):
        if same_row(i,j) or same_col(i,j) or same_block(i,j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
            # At this point, m is not excluded by any row, column, or block, so let's place it and recurse
            r(a[:i]+m+a[i+1:])

if __name__ == '__main__':
    str_in = ".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..".replace('.', '0')
    str_in = ".....6....59.....82....8....45........3........6..3.54...325..6..................".replace('.', '0')  BAD RESULT
    if len(str_in) == 81:
        r(str_in)
    else:
        print('Usage: python sudoku.py puzzle')
        print('  where puzzle is an 81 character string representing the puzzle read left-to-right, top-to-bottom, and 0 is a blank')

