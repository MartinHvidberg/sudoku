

import logging

import SuDoKuX

# create logger
log = logging.getLogger('sudoku.obj')

class SuDoKu(object):
    
    def __init__(self, str_ini):
        self.m = [['0' for i in range(9)] for j in range(9)] # Empty (0 filled) matrix
        self.p = [[list() for i in range(9)] for j in range(9)] # Empty (empty lists) pencil-matrix
        if len(str_ini) == 0:
            pass # Creating empty sudoku ...
        elif len(str_ini) == 81:
            try:
                self.m = [[int(str_ini[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)]
                self.v = self.validate() # Validate that the fill is legal
                if self.v:
                    self.i = str_ini # Backup the original (init) fill, in string form
                    self.o = self.m # Backup the original (init) fill, in matrix form
                    self.pencil() # Fill in the pencil marks, for the init matrix
                    self.solution = [[int(SuDoKuX.sudoku99(str_ini)[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)] # Solve using brute force, to see if solution(s) exist
            except:
                log.error("#102 > SuDoKu Object can't create, Check that it only contains digits, and '.'")
        else:
            log.error("#101 > SuDoKu Object can't create, because ini string do not have length 0 or 81.")
            
    def mycol(self,k,l):
        return [self.m[i][l] for i in range(9)]
    
    def myrow(self,k,l):
        return self.m[k]
    
    def mybox(self,k,l):
        kk = (k//3)*3
        ll = (l//3)*3
        return [self.m[kk+i][ll+j] for i in range(3) for j in range(3)]
        #=======================================================================
        # lst_ret = list()
        # for i in range(3):
        #     for j in range(3):
        #         lst_ret.append(self.m[kk+i][ll+j])
        # return lst_ret
        #=======================================================================
    
    def validate(self):
        return True
            
    def pencil(self):
        pass
    
    #====== Printout functions ======
    
    def show_small(self, matrix):
        def p(i,j):
            return str(matrix[i][j])
        def l(i):
            return ("|"+p(i,0)+p(i,1)+p(i,2)+"|"+p(i,3)+p(i,4)+p(i,5)+"|"+p(i,6)+p(i,7)+p(i,8)+"|\n").replace('0',' ')
        def q():
            v = '-------------\n'
            return (v+l(0)+l(1)+l(2)+v+l(3)+l(4)+l(5)+v+l(6)+l(7)+l(8)+v).strip()
        return q()
    
    def __str__(self):
        return self.show_current()
    
    def show_current(self):
        return self.show_small(self.m)
    
    def show_solved(self):
        return self.show_small(self.solution)