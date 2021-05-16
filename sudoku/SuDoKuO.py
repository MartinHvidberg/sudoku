#!/usr/bin/env python
# -*- coding: utf-8; -*-

#  - ported to py3 with the 2to3 tool

import copy
import logging

import SuDoKuX # xtra functions, made by others, but collected by me ...

""" The Classes of SuDoKu
Here we define the classes that we use to work with SuDoKu
This is the big one - where all the coding is implemented!
"""

__version__ = "0.4.0"

# ToDo []: Many calls of type (csp[0],cps[1]) should be replaced by cps
# ToDo []: Reduce to basic functionality, then make child object with SLAM and grandchild with SLAP !?!

# create logger
log = logging.getLogger('sudoku.obj')


class CustomException(Exception):  # Extended exception handling
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)


class SuDoKu(object):
    """ My SuDoKu class """
    
    DIGS = tuple([n+1 for n in range(9)])
    STPS = ['Free gifts', 'Crosshatching', 'Naked singles', 'Locked Cand.']  # ToDo []: Consider tuple, or do we need to change it?
    
    def __init__(self, str_ini, lst_hardess = STPS):
        """ initialises a SuDoKu object """
        # ToDo: Overview of intended meaning og .m .v .p .rec, etc.
        self.hardness = lst_hardess
        self.m = [['0' for i in range(9)] for j in range(9)] # Empty (0 filled) matrix
        self.p = [[set() for i in range(9)] for j in range(9)] # Empty (empty sets) pencil-matrix
        self.rec = list() # Track record of solving tactics steps
        if len(str_ini) == 0:
            pass # Creating empty sudoku ...
        elif len(str_ini) == 81:
            log.info(f"Input: {str_ini}")
            self.i = str_ini # Backup the original (init) fill, in string form
            try:
                self.m = [[int(str_ini[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)]
            except:
                log.error("#102 > SuDoKu Object can't create, Check that it only contains digits, and '.'")
            self.v = self.validate() # Validate that the fill is legal
            if self.v: # If it's valid, so far, check if it's solvable
                try:
                    # ToDo: This is doubtful - do the solver run x81 times? and what exacely do we proove here?
                    self.solution = [[int(SuDoKuX.sudoku99_NEW_XXX_(str_ini)[j*9+i].replace('.','0')) for i in range(9)] for j in range(9)] # Solve using brute force, to see if solution(s) exist
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
        """ Return SuDoKu value in cell k,l 
        ret: integer """
        return self.m[k][l]
                
    def _set(self, k, l, v):
        """ Set cell k,l in .m to v, and clear relevant pencil marks."""
        for inp in [k,l,v-1]:
            if not isinstance(inp,int) or inp < 0 or inp > 8:
                raise CustomException("_set() takes three integers k, l and v: k and l must all be in [0..8], v must be in [1..9]. Recieved: "+str(k)+", "+str(l)+", "+str(v))
        self.m[k][l] = v
        self.p[k][l] = set() # the k,l cell's own pencil marks. The cell now has a value, all other values are excluded.
        for c in range(9): # row, and col pencil marks
            self.p[k][c].discard(v)
            self.p[c][l].discard(v)
        kk = (k//3)*3 # box pencil marks
        ll = (l//3)*3
        for i in range(3):
            for j in range(3):
                self.p[kk+i][ll+j].discard(v)
    
    #------ this functions -----------------------------------------------------
    # returns lists of cps (coordinate pairs), or values, representing the row, col or box of 'this' cell
    
    def _cps_this_row(self,k,l):
        """ Return list of cps representing the row that (k,l) belongs to """
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
    
    #------ all-rows, -cols and -box functions ---------------------------------
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
        """ Return list of lists of cps (coordinate pairs), representing all rows and all cols and all boxs in the SuDoKu """
        return self._cps_rows() + self._cps_cols() + self._cps_boxs()
    
    def areas(self):
        """ Return a list of lists of digits, representing all rows, cols and boxes in the SuDoKu """
        return self.rows()+self.cols()+self.boxs()
    
    #------ only_ functiones ---------------------------------------------------
    # take a list of cps, and returns that list. But only returns elements that meet the criteria
    # the returned list can be empty
    
    def only_free_cells(self,lst_cps):
        """ Return the cps list, but only cells with value 0 (free cells) """
        return [cps for cps in lst_cps if self.m[cps[0]][cps[1]]==0]
    
    def only_taken_cells(self,lst_cps):
        """ Return the cps list, but only cells with value not 0 (taken cells) """
        return [cps for cps in lst_cps if self.m[cps[0]][cps[1]]!=0]
    
    def only_n_in_row(self,lst_cps,n):
        """ Return the cps list, but only cells where value n is in the same row """
        return [cps for cps in lst_cps if n in self.this_row(cps[0],cps[1])]
    
    def only_n_in_col(self,lst_cps,n):
        """ Return the cps list, but only cells  where value n is in the same col """
        return [cps for cps in lst_cps if n in self.this_col(cps[0],cps[1])]
    
    def only_n_notin_row(self,lst_cps,n):
        """ Return the cps list, but only cells where value n is NOT in the same row """
        return [cps for cps in lst_cps if n not in self.this_row(cps[0],cps[1])]
    
    def only_n_notin_col(self,lst_cps,n):
        """ Return the cps list, but only cells  where value n is NOT in the same col """
        return [cps for cps in lst_cps if n not in self.this_col(cps[0],cps[1])]

    # ToDo []: For completeness, why only x_in_row(), x_in_col() but not x_in_box()?
    
    def only_cps_in_cps(self,lst_cpsa,lst_cpsb):
        """ Return the cps-a list, but only cells that are Also in the cps-b list """
        return list(set(lst_cpsa) & set(lst_cpsb))
    
    def only_cps_notin_cps(self,lst_cpsa,lst_cpsb):
        """ Return the cps-a list, but only cells that are Not in the cps-b list """
        return list(set(lst_cpsa) - set(lst_cpsb))
    
    def only_pen_n_in_cell(self,n,lst_cps):
        """ Return the cps list, but only cells that have n among its pencil marks """
        return [cps for cps in lst_cps if n in self.p[cps[0]][cps[1]]]
    
    #------ Subdeviding functions ----------------------------------------------
    # take a list of cps, and returns that list. But subdivided into pieces.
    # takes list, but returns list of lists.
    
    def rows_in_box(self, lst_in):
        """ Takes one list. Return three lists of lists, having sliced the box into three parts (it's rows). """
        return self._slice9in3_vert(lst_in)
    
    def _slice9in3_vert(self, lst_in):
        """ Generic Vertical slicer. Part list of 9 elements into 3 lists of 3 elements, by Vertical slicing """
        if len(lst_in) == 9:
            return [[lst_in[0],lst_in[3],lst_in[6]],[lst_in[1],lst_in[4],lst_in[7]],[lst_in[2],lst_in[5],lst_in[8]]]
        else:
            return []
    
    def _slice9in3_hori(self, lst_in): 
        """ Generic Horizontal slicer. Part list of 9 elements into 3 lists of 3 elements, by Horizontal slicing """
        return [lst_in[n*3:n*3+3] for n in range(3)]
    
    def area_cross(self, lst_cpsa, lst_cpsb):
        """ Make a crossing of two lists a and b. Return a list of three lists.
        1: Elements exclusively in a. 2: Elements in both a and b. 3. Elements exclusively in b.
        ret: list"""        
        if not isinstance(lst_cpsa, list):
            raise CustomException("area_cross() takes two lists: First parameter given is not a list.")
        if not isinstance(lst_cpsb, list):
            raise CustomException("area_cross() takes two lists: First parameter given is not a list.")
        # XXX re-code, using set() and s-t, s&t, t-s
        if len(lst_cpsa)>0 and len(lst_cpsb)>0:
            lst_cpsa = list(set(lst_cpsa))
            lst_cpsb = list(set(lst_cpsb))
            lst_cpsc = copy.deepcopy(lst_cpsa)
            lst_cpsx = list()
            for itm_n in lst_cpsc:
                if itm_n in lst_cpsb:
                    lst_cpsx.append(itm_n)
                    lst_cpsa.remove(itm_n)
                    lst_cpsb.remove(itm_n)
            return [lst_cpsa,lst_cpsx,lst_cpsb]
        else:
            return[lst_cpsa,list(),lst_cpsb]
            
    #------ locical functions (returning booleans) -----------------------------
    
    def cps_allinone_row(self, lst_cps):
        coor = [i for i,j in lst_cps]
        if len(set(coor)) == 1:
            return True
        else:
            return False
    
    def cps_allinone_col(self, lst_cps):
        coor = [j for i,j in lst_cps]
        if len(set(coor)) == 1:
            return True
        else:
            return False
    
    def cps_allinone_box(self, lst_cps):
        cps_box = self._cps_this_box(lst_cps[0][0],lst_cps[0][1])
        cps_jnt = self.only_cps_in_cps(lst_cps,cps_box)
        return len(cps_jnt) == len(lst_cps)
    
    #------ pencil functions ---------------------------------------------------
            
    def pencil(self):
        """ Fill pencil-marks, simply based on the filled cells. Intended for initial pencil-marking. """
        for i in range(9):
            for j in range(9):
                if self.get(i,j) != 0:
                    self.p[i][j] = set()
                else:
                    # marks = set([1,2,3,4,5,6,7,8,9]) Performance can be improved using literal.
                    marks = {1,2,3,4,5,6,7,8,9}
                    fixed = set(self.this_col(i,j)) | set(self.this_row(i,j)) | set(self.this_box(i,j))
                    self.p[i][j] = marks - fixed      
        log.info("pencile() marks: "+str(self.pencils_as_string()))
    
    def ps_in_cps(self, lst_cps):
        """ Return list of values of pencil-marks, represented in cells in cps """
        if not isinstance(lst_cps, list):
            raise CustomException(" ps_in_cps() takes list of coordinate pairs. Input parameter is not type list.")
        if len(lst_cps)>0:
            set_ps = set()
            for cps in lst_cps:
                set_ps = set_ps | self.p[cps[0]][cps[1]]
            return set_ps
        else:
            return list()
        
    def _p_count_in_cps(self, n, lst_cps):
        """ Count number of occurrences of value n in pencil-marks in cells in cps """
        lst_ps = [self.p[i][j] for i,j in lst_cps]
        cnt = 0
        for pset in lst_ps:
            if n in pset:
                cnt += 1
        return cnt
    
    #def p_for_cpsXXX(self, lst_cps): Function persumed deprevated... Better check that...
    #    return [self.p[cps[0]][cps[1]] for cps in lst_cps]
    
    def p_wipe_n_in_cps(self,num_n,lst_cps):
        """ Remove (wipe) the number n from the Pencil-marks in all cells, in a list of coordinate pairs """
        if len(lst_cps)>0:
            for cps in lst_cps:
                self.p[cps[0]][cps[1]] = self.p[cps[0]][cps[1]]-set([num_n])
    
    # more functions
    def _cps_to_val(self, obj_in):
        """ Takes a coordinate pair (a tuple) or a list of them. Returns the value in that cell, or a list of them """
        if isinstance(obj_in, tuple):
            return self.get(obj_in[0],obj_in[1])
        elif isinstance(obj_in, list):
            obj_ret = list()
            for num_item in range(len(obj_in)):
                obj_ret.append(self._cps_to_val(obj_in[num_item]))
            return obj_ret
        else:
            raise CustomException(" _cps_to_val() takes a tuple or a list, this input was neither ...")
        
    def solved(self):
        """ Returns True if the SuDoKu is solved, otherwise returns False. """
        empty = 0
        for row in self.rows():
            empty += len([x for x in row if x==0])
        return empty == 0
    
    def validate(self):
        """ Return True if the SuDoKu is valid, otherwise returns False """
        bol_valid = True # Until proven guilty
        # XXX Consider checking for values not being single digit numbers
        for area in self.areas(): # check row, col and box doublets
            # a = filter(lambda a: a != 0, area)
            a = [val for val in area if val != 0]
            if len(a) != len(list(set(a))):
                bol_valid = False
                log.error("#201 > Area seems to have redundant values: "+str(area))
        log.info("validate() = "+str(bol_valid))
        return bol_valid
    
    def stats(self):
        dic_stat = dict()
        str_ret = ""
        if self.validate():
            if not self.solved():
                str_ret += 'Not solved by SLAP... '
            if len(self.rec) > 0:
                for track in self.rec:
                    if track.tactic not in list(dic_stat.keys()):
                        dic_stat[track.tactic] = track.goods()
                    else:
                        dic_stat[track.tactic] = dic_stat[track.tactic] + track.goods()
                # Present the dic_stat in difficulty-sorted order
                lst_keys = list(dic_stat.keys())
                lst_keys = sorted(lst_keys, key=self.hardness.index, reverse=True)
                str_ret += "{"
                for k in lst_keys:
                    str_ret += str(k) + ':' + str(dic_stat[k]) + ','
                str_ret = str_ret.rstrip(',')
                return str_ret+'}' 
            else:
                raise CustomException(" stats() No track record found - this is really strange :-(")
        else:
            raise CustomException(" stats() takes a valid SuDoKu. This is Not valid: " + str(self.m))
                
    #====== SLAP (Solve Like A Person) solver functions ======
    
    def record(self, dic_hit):
        """ Adds a solving-move to the track record """
        self.rec.append(dic_hit)
    
    #------ Singles ------------------------------------------------------------
    
    def free_gifts(self):
        """ Solving technique: Free Gifts.
        A Col, Row or Box only have 1 unfilled cell left """
        track = Track('Free gifts') 
        for area in self._cps_areas():
            av = self._cps_to_val(area)
            if av.count(0) == 1:
                i,j =  area[av.index(0)]
                # val = (set([1,2,3,4,5,6,7,8,9]) - set(av)).pop() Better performance with literal
                val = ({1,2,3,4,5,6,7,8,9} - set(av)).pop()
                self._set(i,j,val)
                track.set(i,j,val)
        log.info(track.show())
        self.record(track)
        return track.goods()
    
    def crosshatching(self):
        """ Solving technique: Crosshatching. """
        track = Track('Crosshatching') 
        for box in self._cps_boxs():
            boxf = self.only_free_cells(box)
            set_taken_values = set(self._cps_to_val(box))
            for n in self.DIGS:
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
        """ Solving technique: Naked singles.
        Some thing like: 'Only one pencil mark left in this cell'?. Check up on that..."""
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
    
    # def hidden_single(self): # Equal to Crosshaching
    #     track = Track('Hidden Single')
    #     
    #     log.info(track.show())
    #     self.record(track)
    #     return track.goods()
    
    #------ Intersections ------------------------------------------------------
    
    def locked_candidates(self):
        """ Solving technique: Locked Candidates. """
        track = Track('Locked Cand.')
        for box in self._cps_boxs():
            for n in self.DIGS:
                cps_box_n = self.only_pen_n_in_cell(n,box) # reduce to cps with pencil n
                if self.cps_allinone_row(cps_box_n): # Check for Row uniqueness
                    cps_rest = self.only_cps_notin_cps(self._cps_this_row(cps_box_n[0][0],cps_box_n[0][1]),box)
                    cps_wipe = self.only_pen_n_in_cell(n,cps_rest) # Only wipe if there is something to wipe
                    if len(cps_wipe) > 0:
                        self.p_wipe_n_in_cps(n,cps_rest) 
                        track.erase(n,cps_wipe)
                if self.cps_allinone_col(cps_box_n): # Check for Col uniqueness
                    cps_rest = self.only_cps_notin_cps(self._cps_this_col(cps_box_n[0][0],cps_box_n[0][1]),box)
                    cps_wipe = self.only_pen_n_in_cell(n,cps_rest) # Only wipe if there is something to wipe
                    if len(cps_wipe) > 0:
                        self.p_wipe_n_in_cps(n,cps_rest) 
                        track.erase(n,cps_wipe)
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
                        if not self.locked_candidates():
                            log.info('Seem to have exhausted all solving strategies ...')
                            return
        log.info('Seem to have solved the SuDoKu. Thanks for using SLAP :-)')
            
    #====== Printout functions ======
    
    def __str__(self):
        return self.show_current()

    def show_line(self):
        str_r = str()
        for lst_l in self.m:
            for int_n in lst_l:
                str_r += (str(int_n))
        return str_r.replace('0','.')
    
    def show_small(self, matrix):
        def p(i,j):
            return str(matrix[i][j])
        def l(i):
            return ("|"+p(i,0)+p(i,1)+p(i,2)+"|"+p(i,3)+p(i,4)+p(i,5)+"|"+p(i,6)+p(i,7)+p(i,8)+"|\n").replace('0',' ')
        def q():
            v = '+---+---+---+\n'
            return (v+l(0)+l(1)+l(2)+v+l(3)+l(4)+l(5)+v+l(6)+l(7)+l(8)+v).strip()
        return q()

    def show_medium(self, matrix):
        def p(i,j):
            return str(matrix[i][j])
        def l(i):
            return ("| "+p(i,0)+" "+p(i,1)+" "+p(i,2)
                    +" | "+p(i,3)+" "+p(i,4)+" "+p(i,5)
                    +" | "+p(i,6)+" "+p(i,7)+" "+p(i,8)+" |\n").replace('0',' ')
        def q():
            v = '+ - - - + - - - + - - - +\n'
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
        return self.show_medium(self.m)
    
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
        """ Initialise the track record """
        self.tactic = caller # The 'Tactic' that did this
        self.sets = 0 # Number of successful Set operations
        self.pencils = 0 # Number of successful Pencil operations
        self.hits = list()
        
    def goods(self):
        """ Return total count of Good operations """
        return self.sets + self.pencils
        
    def show(self):
        """ Return the summed track record """ 
        t = self.tactic.ljust(16)
        s = str(self.sets)
        p = str(self.pencils)
        h = ""
        for hit in self.hits:
            h += hit+','
        h = h.rstrip(',')
        return t+' : set:'+s+' pen:'+p+' ['+h+']'
        
    def set(self,i,j,v):
        """ Note a set() operation """
        self.sets += 1
        self.hits.append('s('+str(i)+','+str(j)+'='+str(v)+')')
        
    def erase(self,n,lst_cps):
        """ Note a erase() operation """
        self.pencils += 1
        self.hits.append('pe('+str(n)+'@'+str(lst_cps).replace(' ','')+')')
        
    def hit(self, hit_a):
        """ Append a hit to the track record """
        self.hits.append(hit_a)    

if __name__ == "__main__":
    
    raise CustomException("*** This module can't be run - it should be called from another program ***")
