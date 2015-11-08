

import logging

# create logger
log = logging.getLogger('sudoku.obj')

class SuDoKu(object):
    
    def __init__(self, str_ini):
        self.m = [['0' for i in range(9)] for j in range(9)] # Empty (0 filled) matrix
        if len(str_ini) == 0:
            pass
        elif len(str_ini) == 81:
            try:
                self.m = [[int(str_ini[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)]
            except:
                log.error("#102 > SuDoKu Object can't create, Check that it only contains digits, and '.'")
        else:
            log.error("#101 > SuDoKu Object can't create, because ini string do not have length 0 or 81.")
            
    
    def __str__(self):
        def p(j,i):
            return str(self.m[j][i])
        def l(j):
            return ("|"+p(j,0)+p(j,1)+p(j,2)+"|"+p(j,3)+p(j,4)+p(j,5)+"|"+p(j,6)+p(j,7)+p(j,8)+"|\n").replace('0',' ')
        def q():
            v = '-------------\n'
            return (v+l(0)+l(1)+l(2)+v+l(3)+l(4)+l(5)+v+l(6)+l(7)+l(8)+v).strip()
        return q()