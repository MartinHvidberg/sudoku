

import logging

# create logger
log = logging.getLogger('sudoku.obj')

class SuDoKu(object):
    
    def __init__(self, str_ini):
        self.m = [['0' for i in range(9)] for j in range(9)] # Empty (0 filled) matrix
        self.p = [[list() for i in range(9)] for j in range(9)] # Empty (empty lists) pencil-matrix
        if len(str_ini) == 0:
            pass
        elif len(str_ini) == 81:
            try:
                self.m = [[int(str_ini[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)]
                self.pencil()
            except:
                log.error("#102 > SuDoKu Object can't create, Check that it only contains digits, and '.'")
        else:
            log.error("#101 > SuDoKu Object can't create, because ini string do not have length 0 or 81.")
            
    def mycol(self,k,l):
        return [self.m[i][l] for i in range(9)]
    
    def myrow(self,k,l):
        return self.m[k]
    
    
            
    #def pencil(self):
    #    self
    
    def __str__(self):
        def p(i,j):
            return str(self.m[i][j])
        def l(i):
            return ("|"+p(i,0)+p(i,1)+p(i,2)+"|"+p(i,3)+p(i,4)+p(i,5)+"|"+p(i,6)+p(i,7)+p(i,8)+"|\n").replace('0',' ')
        def q():
            v = '-------------\n'
            return (v+l(0)+l(1)+l(2)+v+l(3)+l(4)+l(5)+v+l(6)+l(7)+l(8)+v).strip()
        return q()