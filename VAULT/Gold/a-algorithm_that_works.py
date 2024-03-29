import sys

###### THIS BLOODY WORKS SO DON'T MESS IT UP ###########################################################################

def same_row(i,j): return (i//9 == j//9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i//27 == j//27 and i%9//3 == j%9//3)

def r(a, find_all=False):
    i = a.find('0')
    if i == -1:
        if find_all:
            print(f"solution: {a}")
            return
        else:
            print(f"solution: {a}")
            sys.exit(999)

    excluded_numbers = set()
    for j in range(81):
        if same_row(i,j) or same_col(i,j) or same_block(i,j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
            # At this point, m is not excluded by any row, column, or block, so let's place it and recurse
            r(a[:i]+m+a[i+1:], find_all)


if __name__ == '__main__' :
    #i = '8..5.9..67..3.1..2..3...8....12.34..9...6...3..68.47....4...5..2..4.5..76..9.2..4'.replace('.','0')  # Classic
    i = '9265714833514862798749235165823671941492583677631..8252387..651617835942495612738'.replace('.','0')  # double-solution

    print(f"input ->: {i}")
    print("\nTrue")
    o = r(i, True)
    print(f"o: {o}")
    print("\nFalse")
    o = r(i, False)
    print(f"o: {o}")

