
import logging

import SuDoKuX # Xtra functions, made by others...

# create logger
log = logging.getLogger('sudoku.obj')

class SuDoKu(object):
    
    def __init__(self, str_ini):
        self.m = [['0' for i in range(9)] for j in range(9)] # Empty (0 filled) matrix
        self.p = [[set() for i in range(9)] for j in range(9)] # Empty (empty lists) pencil-matrix
        self.rec = list() # Track record of solving tactics steps
        if len(str_ini) == 0:
            pass # Creating empty sudoku ...
        elif len(str_ini) == 81:
            log.info("Input: "+str_ini)
            self.i = str_ini # Backup the original (init) fill, in string form
            try:
                self.m = [[int(str_ini[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)]
            except:
                log.error("#102 > SuDoKu Object can't create, Check that it only contains digits, and '.'")
            self.v = self.validate() # Validate that the fill is legal
            if self.v: # If it's valid, so far, check it it's solvable
                try:
                    self.solution = [[int(SuDoKuX.sudoku99(str_ini)[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)] # Solve using brute force, to see if solution(s) exist
                    log.info("Input is Solvable, but was not checked for uniqueness...")
                except:
                    self.solution = self.m # If not solvable, keep the init values to avoid a Null variable.
                    self.v = False # It looked valid, but it's not ...
                    log.warning("Input is NOT Solvable...")
            if self.v: # If it's valid, and also is solvable
                self.pencil() # Fill in the pencil marks, for the valid, solvable, init matrix
        else:
            log.error("#101 > SuDoKu Object can't create, because ini string do not have length 0 or 81.")
            
    # Basic functions (get, set)
            
    def get(self,k,l):
        """ Return SuDoKu value in cell k,l """
        return self.m[k][l]
                
    def _set(self, k, l, v):
        """ Set cell k,l in .m to value, and clear relevant pencil marks. """
        self.m[k][l] = v
        self.p[k][l] = set() # its own pencil marks
        for c in range(9): # row, and col pencil marks
            self.p[k][c].discard(v)
            self.p[c][l].discard(v)
        kk = (k//3)*3 # box pencil marks
        ll = (l//3)*3
        for i in range(3):
            for j in range(3):
                self.p[kk+i][ll+j].discard(v)
        return
    
    # this functions
    # returns lists of cps or values, representing the row, col or box of 'this' cell
    
    def _cps_this_row(self,k,l):
        """ Return list of cps (coordinate pairs), representing the row that (k,l) belongs to """
        return [(k,i) for i in range(9)]
    
    def this_row(self,k,l):
        """ Return list of digits, representing the row that (k,l) belongs to """
        return self.m[k] # Not using ._cps_ since this is simpler and faster
    
    def _cps_this_col(self,k,l):
        """ Return list of cps (coordinate pairs), representing the col that (k,l) belongs to """
        return [(i,l) for i in range(9)]

    def this_col(self,k,l):
        """ Return list of digits, representing the col that (k,l) belongs to """
        return [self.m[i][l] for i in range(9)] # Not using ._cps_ since this is simpler and faster
    
    def _cps_this_box(self,k,l):
        """ Return list of cps (coordinate pairs), representing the box that (k,l) belongs to """
        kk = (k//3)*3
        ll = (l//3)*3
        return [(kk+i,ll+j) for i in range(3) for j in range(3)]
    
    def this_box(self,k,l):
        """ Return list of digits, representing the box that (k,l) belongs to """
        return [self.get(i,j) for i,j in self._cps_this_box(k,l)]
    
    # all-rows, -cols and -box functions
    # return lists of cps or value, representing all rows, etc in the sudoku   
    
    def _cps_rows(self):
        """ Return list of lists of cps (coordinate pairs), representing all rows in the SuDoKu """
        return [[(i,j) for j in range(9)] for i in range(9)]

    def rows(self):
        """ Return a list of lists of digits, representing all rows in the SuDoKu """
        return self.m  # Not using ._cps_ since this is simpler and faster
    
    def _cps_cols(self):
        """ Return list of lists of cps (coordinate pairs), representing all cols in the SuDoKu """
        return [[(i,j) for i in range(9)] for j in range(9)]
    
    def cols(self):
        """ Return a list of lists of digits, representing all cols in the SuDoKu """
        return [self.this_col(1,i) for i in range(9)]
    
    def _cps_boxs(self):
        """ Return list of lists of cps (coordinate pairs), representing all boxs in the SuDoKu """
        return [self._cps_this_box(i*3,j*3) for i in range(3) for j in range(3)]
    
    def boxs(self):
        """ Return a list of lists of digits, representing all boxs in the SuDoKu """
        return [self.this_box(i*3,j*3) for i in range(3) for j in range(3)]
    
    def _cps_areas(self):
        return self._cps_rows() + self._cps_cols() + self._cps_boxs()
    
    # only_ functiones
    # take a list of cps, and returns that list. But only returns elements that meet the criteria
    # the returned list can be empty
    
    def only_free_cells(self,lst_cps):
        return [cps for cps in lst_cps if self.m[cps[0]][cps[1]]==0]
    
    def only_taken_cells(self,lst_cps):
        return [cps for cps in lst_cps if self.m[cps[0]][cps[1]]!=0]
    
    def only_n_notin_row(self,lst_cps,n):
        return [cps for cps in lst_cps if n not in self.this_row(cps[0],cps[1])]
    
    def only_n_notin_col(self,lst_cps,n):
        return [cps for cps in lst_cps if n not in self.this_col(cps[0],cps[1])]
    
    # more functions
    
    def solved(self):
        empty = 0
        for row in self.rows():
            empty += len(filter(lambda x: x==0, row))
        return empty == 0
    
    def validate(self):
        bol_valid = True # Until proven guilty
        for area in self.rows()+self.cols()+self.boxs(): # check row, col and box duplets
            a = filter(lambda a: a != 0, area)
            if len(a) != len(list(set(a))):
                bol_valid = False
                log.error("#201 > Area seems to have redundant values: "+str(area))
        log.info("validate() = "+str(bol_valid))
        return bol_valid
            
    def pencil(self):
        # Exclude digits occupied elsewhere in row, col or box.
        for i in range(9):
            for j in range(9):
                if self.get(i, j) != 0:
                    self.p[i][j] = set()
                else:
                    marks = set([1,2,3,4,5,6,7,8,9])
                    fixed = set(self.this_col(i,j)) | set(self.this_row(i,j)) | set(self.this_box(i,j))
                    self.p[i][j] = marks - fixed      
        log.info("pencile() marks: "+str(self.pencils_as_string()))
        return
    
    def _cps_to_val(self,obj_in):
        if isinstance(obj_in, list):
            obj_ret = list()
            for num_item in range(len(obj_in)):
                obj_ret.append(self._cps_to_val(obj_in[num_item]))
        elif isinstance(obj_in, tuple):
            return self.get(obj_in[0],obj_in[1])
        return obj_ret
                
    #====== SLAP (Solve Like A Person) solver functions ======
    
    def record(self, dic_hit):
        """ Adds a solving-move to the track record """
        
        return
    
    def free_gifts(self):
        track = Track('Free gifts') 
        for area in self._cps_areas():
            av = self._cps_to_val(area)
            if av.count(0) == 1:
                i,j =  area[av.index(0)]
                val = (set([1,2,3,4,5,6,7,8,9]) - set(av)).pop()
                self._set(i,j,val)
                track.set(i,j,val)
        log.info(track.show())
        self.record(track)
        return track.goods()
    
    def crosshatching(self):
        track = Track('Crosshatching') 
        for box in self._cps_boxs():
            boxf = self.only_free_cells(box)
            set_taken_values = set(self._cps_to_val(box))
            for n in range(9):
                boxc = boxf # get a fresh copy
                if not n in set_taken_values: # skip values all ready in box
                    boxc = self.only_n_notin_row(boxc,n)
                    boxc = self.only_n_notin_col(boxc,n)
                    if len(boxc) == 1:
                        self._set(boxc[0][0],boxc[0][1],n)
                        track.set(boxc[0][0],boxc[0][1],n)
        log.info(track.show())
        self.record(track)
        return track.goods()
    
    def naked_singles(self):
        track = Track('Naked singles') 
        for i in range(9):
            for j in range(9):
                if len(self.p[i][j])==1:
                    val = self.p[i][j].pop()
                    self._set(i,j,val)
                    track.set(i,j,val)
        log.info(track.show())
        self.record(track)
        return track.goods()

    def slap(self):
        """ The main thing you would call ...
        The 'Solve Like A Person' function.
        This will try to solve the SuDoKu, by intelligently calling a sequence of the SLAP functions above. """
        
        while not self.solved():
            if not self.free_gifts():
                if not self.crosshatching():
                    if not self.naked_singles():
                        log.info('Seem to have exhausted all solving strategies ...')
                        return -1
        log.info('Seem to have solved the SuDoKu. Thanks for using SLAP :-)')
        return 0
            
                
    #====== Printout functions ======
    
    def __str__(self):
        return self.show_current()
    
    def show_small(self, matrix):
        def p(i,j):
            return str(matrix[i][j])
        def l(i):
            return ("|"+p(i,0)+p(i,1)+p(i,2)+"|"+p(i,3)+p(i,4)+p(i,5)+"|"+p(i,6)+p(i,7)+p(i,8)+"|\n").replace('0',' ')
        def q():
            v = '+---+---+---+\n'
            return (v+l(0)+l(1)+l(2)+v+l(3)+l(4)+l(5)+v+l(6)+l(7)+l(8)+v).strip()
        return q()
    
    def pencils_as_lol(self):
        return [[list(self.p[i][j]) for j in range(9)] for i in range(9)]
    
    def pencils_as_string(self):
        lst_ret = self.pencils_as_lol()
        str_ret = "("
        for lst_r in lst_ret:
            for lst_p in lst_r:
                lst_p.sort()
                str_ret += str(lst_p).replace('[','').replace(']','').replace(',','').replace(' ','')+','
            str_ret += ';'
        return str_ret.strip(';')+')'
    
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
    
class Track(object):
    
    def __init__(self, caller='anonymous'):
        self.tactic = caller
        self.sets = 0
        self.pencils = 0
        self.hits = list()
        
    def goods(self):
        return self.sets + self.pencils
        
    def show(self):
        t = self.tactic.ljust(16)
        s = str(self.sets)
        p = str(self.pencils)
        h = ""
        for hit in self.hits:
            h += hit+','
        h = h.rstrip(',')
        return t+' : set:'+s+' pen:'+p+' ['+h+']'
        
    def set(self,i,j,v):
        self.sets += 1
        self.hits.append('s('+str(i)+','+str(j)+'='+str(v)+')')
        return
        
    def pencil(self):
        self.pencils += 1
        return
        
    def hit(self, hit_a):
        self.hits.append(hit_a)
        return
    

if __name__ == "__main__":
    
    print "\n   *** This module can't be run - it should be called from another program ***"
    
        