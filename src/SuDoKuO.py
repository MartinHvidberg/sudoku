

import logging

import SuDoKuX # Xtra functions, made by others...

# create logger
log = logging.getLogger('sudoku.obj')

class SuDoKu(object):
    
    def __init__(self, str_ini):
        self.m = [['0' for i in range(9)] for j in range(9)] # Empty (0 filled) matrix
        self.p = [[set() for i in range(9)] for j in range(9)] # Empty (empty lists) pencil-matrix
        if len(str_ini) == 0:
            pass # Creating empty sudoku ...
        elif len(str_ini) == 81:
            self.i = str_ini # Backup the original (init) fill, in string form
            try:
                self.m = [[int(str_ini[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)]
            except:
                log.error("#102 > SuDoKu Object can't create, Check that it only contains digits, and '.'")
            self.v = self.validate() # Validate that the fill is legal
            if self.v: # If it's valid, so far, check it it's solvable
                try:
                    self.solution = [[int(SuDoKuX.sudoku99(str_ini)[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)] # Solve using brute force, to see if solution(s) exist
                except:
                    self.solution = self.m # If not solvable, keep the init values to avoid a Null variable.
                    self.v = False # It looked valid, but it's not ...
            if self.v: # If it's valid, and also is solvable
                self.pencil() # Fill in the pencil marks, for the valid, solvable, init matrix
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
    
    def rows(self):
        return self.m 
    
    def cols(self):
        return [self.mycol(1,i) for i in range(9)]
    
    def boxs(self):
        return [self.mybox(i*3,j*3) for i in range(3) for j in range(3)]
        
    def validate(self):
        bol_valid = True # Until proven guilty
        for area in self.rows()+self.cols()+self.boxs(): # check row, col and box duplets
            a = filter(lambda a: a != 0, area)
            if len(a) != len(list(set(a))):
                bol_valid = False
                log.error("#201 > Area seems to have redundant values: "+str(area))
        return bol_valid
            
    def pencil(self):
        for i in range(9):
            for j in range(9):
                marks = set([1,2,3,4,5,6,7,8,9])
                fixed = set(self.mycol(i,j)) | set(self.myrow(i,j)) | set(self.mybox(i,j))
                self.p[i][j] = marks - fixed
                
    #====== SLAP (Solve Like A Person) solver functions ======
    
    def free_gifts(self):
        
        return
                
    #====== Printout functions ======
    
    def show_small(self, matrix):
        def p(i,j):
            return str(matrix[i][j])
        def l(i):
            return ("|"+p(i,0)+p(i,1)+p(i,2)+"|"+p(i,3)+p(i,4)+p(i,5)+"|"+p(i,6)+p(i,7)+p(i,8)+"|\n").replace('0',' ')
        def q():
            v = '+---+---+---+\n'
            return (v+l(0)+l(1)+l(2)+v+l(3)+l(4)+l(5)+v+l(6)+l(7)+l(8)+v).strip()
        return q()
    
    def __str__(self):
        return self.show_current()
    
    def show_current(self):
        return self.show_small(self.m)
    
    def show_solved(self):
        if self.v:
            return self.show_small(self.solution)
        else:
            return "SuDoKu can't be solved, since it's invalid..."
    
    def show_big(self):
        lines = [['0' for i in range(37)] for j in range(37)]
        # Build graticules
        for p in range(37):
            if p in (0,12,24,36):
                lines[p] = "+===========+===========+===========+"
            elif p in (4,8,16,20,28,32,36):
                lines[p] = "|---+---+---|---+---+---|---+---+---|"
            else:
                lines[p] = "|   !   !   |   !   !   |   !   !   |"
        # Fill values # XXX This can be cleaned up - cci and ccj pre-calcs
        for i in range(9):
            for j in range(9):
                cci = i*4+2
                ccj = j*4+2
                if self.m[i][j] != 0: # show solved value
                    lines[cci-1] = lines[cci-1][:ccj-1] +'...'+ lines[cci-1][ccj+2:]
                    lines[cci] = lines[cci][:ccj-1] +'.'+str(self.m[i][j])+'.'+ lines[cci][ccj+2:]
                    lines[cci+1] = lines[cci+1][:ccj-1] +'...'+ lines[cci+1][ccj+2:]
                else: # show pencil marks
                    if 1 in self.p[i][j]:
                        lines[cci-1] = lines[cci-1][:ccj-1] +str(1)+ lines[cci-1][ccj:]
                    if 2 in self.p[i][j]:
                        lines[cci-1] = lines[cci-1][:ccj] +str(2)+ lines[cci-1][ccj+1:]
                    if 3 in self.p[i][j]:
                        lines[cci-1] = lines[cci-1][:ccj+1] +str(3)+ lines[cci-1][ccj+2:]
                    if 4 in self.p[i][j]:
                        lines[cci] = lines[cci][:ccj-1] +str(4)+ lines[cci][ccj:]
                    if 5 in self.p[i][j]:
                        lines[cci] = lines[cci][:ccj] +str(5)+ lines[cci][ccj+1:]
                    if 6 in self.p[i][j]:
                        lines[cci] = lines[cci][:ccj+1] +str(6)+ lines[cci][ccj+2:]
                    if 7 in self.p[i][j]:
                        lines[cci+1] = lines[cci+1][:ccj-1] +str(7)+ lines[cci+1][ccj:]
                    if 8 in self.p[i][j]:
                        lines[cci+1] = lines[cci+1][:ccj] +str(8)+ lines[cci+1][ccj+1:]
                    if 9 in self.p[i][j]:
                        lines[cci+1] = lines[cci+1][:ccj+1] +str(9)+ lines[cci+1][ccj+2:]
                        
        # to strings
        str_ret = ""
        for line in lines:
            for pin in line:
                str_ret += str(pin)
            str_ret += '\n'
        return str_ret
                        
    def show_pencil(self):
        return self.show_big()
        