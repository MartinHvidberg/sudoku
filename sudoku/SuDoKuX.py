
""" External (X-ternal) code
Small and big pieces of code, copied from the internet or elsewhere
This may be called from the other modules for test or to confirm solvability etc.
"""

import sys

# #https://github.com/attractivechaos/plb/blob/master/sudoku/incoming/sudoku-bb.py
#
# # Boris Borcic 2006
# # Quick and concise Python 2.5 sudoku solver - ported to py3 with the 2to3 tool
# #
#
# w2q = [[n/9,n/81*9+n%9+81,n%81+162,n%9*9+n/243*3+n/27%3+243] for n in range(729)]
# q2w = (z[1] for z in sorted((x,y) for y,s in enumerate(w2q) for x in s))
# q2w = list(map(set,list(zip(*9*[q2w]))))
# w2q2w = [set(w for q in qL for w in q2w[q]) for qL in w2q]
#
# class Completed(Exception) : pass
#
# def sudoku99(problem) :
#     givens = list(9*j+int(k)-1 for j,k in enumerate(problem[:81]) if '0'<k)
#     try :
#         search(givens,[9]*len(q2w),set(),set())
#     except Completed as ws :
#         return ''.join(str(w%9+1) for w in sorted(ws.message))
#
# def search(w0s,q2nw,takens,ws) :
#     while 1 :
#         while w0s:
#             w0 = w0s.pop()
#             takens.add(w0)
#             ws.add(w0)
#             for q in w2q[w0] : q2nw[q]+=100
#             for w in w2q2w[w0] - takens :
#                 takens.add(w)
#                 for q in w2q[w] :
#                     n = q2nw[q] = q2nw[q]-1
#                     if n<2 :
#                         w0s.append((q2w[q]-takens).pop())
#         if len(ws)>80 :
#             raise Completed(ws)
#         w1,w0 = q2w[q2nw.index(2)]-takens
#         try : search([w1],q2nw[:],takens.copy(),ws.copy())
#         except KeyError :
#             w0s.append(w0)


###################################################################################################

# ''' Andrew Henshaw
#     based on
#        Boris Borcic 2006
#        Quick and concise Python 2.5 sudoku solver
#     but faster
# '''
# import sys
#
# w2q = [[n / 9, n / 81 * 9 + n % 9 + 81, n % 81 + 162, n % 9 * 9 + n / 243 * 3 + n / 27 % 3 + 243] for n in xrange(729)]
# q2w = []
# for y, (s0, s1, s2, s3) in enumerate(w2q):
#     q2w += [(s0, y), (s1, y), (s2, y), (s3, y)]
# q2w = (z[1] for z in sorted(q2w))
# q2w = map(set, zip(*9 * [q2w]))
# w2q2w = [(q2w[q0] | q2w[q1] | q2w[q2] | q2w[q3]) for q0, q1, q2, q3 in w2q]
#
#
# def search(w0s, q2nw, takens, ws):
#     w0s_app = w0s.append
#     w0s_pop = w0s.pop
#     t_add = takens.add
#     ws_add = ws.add
#     q2nw_index = q2nw.index
#     while True:
#         while w0s:
#             w0 = w0s_pop()
#             t_add(w0)
#             ws_add(w0)
#             q0, q1, q2, q3 = w2q[w0]
#             q2nw[q0] += 100
#             q2nw[q1] += 100
#             q2nw[q2] += 100
#             q2nw[q3] += 100
#
#             for w in w2q2w[w0] - takens:
#                 t_add(w)
#                 q0, q1, q2, q3 = w2q[w]
#
#                 n = q2nw[q0] = q2nw[q0] - 1
#                 if n < 2:
#                     w0s_app((q2w[q0] - takens).pop())
#
#                 n = q2nw[q1] = q2nw[q1] - 1
#                 if n < 2:
#                     w0s_app((q2w[q1] - takens).pop())
#
#                 n = q2nw[q2] = q2nw[q2] - 1
#                 if n < 2:
#                     w0s_app((q2w[q2] - takens).pop())
#
#                 n = q2nw[q3] = q2nw[q3] - 1
#                 if n < 2:
#                     w0s_app((q2w[q3] - takens).pop())
#         if len(ws) == 81:
#             raise Exception(ws)
#         w1, w0 = q2w[q2nw_index(2)] - takens
#         try:
#             search([w1], q2nw[:], takens.copy(), ws.copy())
#         except KeyError:
#             w0s_app(w0)
#
#
# givens = [9 * j + int(k) - 1 for j, k in enumerate(sys.argv[1]) if '0' < k]
# try:
#     search(givens, [9] * len(q2w), set(), set())
# except Exception as e:
#     print
#     ''.join(str(w % 9 + 1) for w in sorted(e.message))

###################################################################################################

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


if __name__ == '__main__' :
    #print(sudoku99('13........2...9......8..7..6....48....5.2...........4.....3...27..5.....8........'.replace('.','0')))

    print((r('8..5.9..67..3.1..2..3...8....12.34..9...6...3..68.47....4...5..2..4.5..76..9.2..4'.replace('.','0'))))
