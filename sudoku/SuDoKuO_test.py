
*** Dont use this, use /ec_sudoku/* instead ***


""" The OLD unit test """

# SuDoKuO_ut.PY

# sumo:
# +---+---+---+
# |8  |   |   |
# |  3|6  |   |
# | 7 | 9 |2  |
# +---+---+---+
# | 5 |  7|   |
# |   | 45|7  |
# |   |1  | 3 |
# +---+---+---+
# |  1|   | 68|
# |  8|5  | 1 |
# | 9 |   |4  |
# +---+---+---+
#
# +===========+===========+===========+
# |...!12 ! 2 | 23!123!123|1 3!   !1 3|
# |.8.!4 6!456|4  ! 5 !4  | 56!45 !456|
# |...!   !  9|7  !7  !   |  9!7 9!7 9|
# |---+---+---|---+---+---|---+---+---|
# |12 !12 !...|...!12 !12 |1  !   !1  |
# |45 !4  !.3.|.6.! 5 !4  | 5 !45 !45 |
# |  9!   !...|...!78 ! 8 | 89!789!7 9|
# |---+---+---|---+---+---|---+---+---|
# |1  !...!   |  3!...!1 3|...!   !1 3|
# |456!.7.!456|4  !.9.!4  |.2.!45 !456|
# |   !...!   | 8 !...! 8 |...! 8 !   |
# +===========+===========+===========+
# |123!...! 2 | 23! 23!...|1  ! 2 !12 |
# |4 6!.5.!4 6|   !  6!.7.|  6!4  !4 6|
# |  9!...!  9| 89! 8 !...| 89! 89!  9|
# |---+---+---|---+---+---|---+---+---|
# |123!123! 2 | 23!...!...|...! 2 !12 |
# |  6!  6!  6|   !.4.!.5.|.7.!   !  6|
# |  9! 8 !  9| 89!...!...|...! 89!  9|
# |---+---+---|---+---+---|---+---+---|
# | 2 ! 2 ! 2 |...! 2 ! 2 |   !...! 2 |
# |4 6!4 6!4 6|.1.!  6!  6| 56!.3.!456|
# |7 9! 8 !7 9|...! 8 ! 89| 89!...!  9|
# +===========+===========+===========+
# | 23! 23!...| 23! 23! 23|  3!...!...|
# |45 !4  !.1.|4  !   !4  | 5 !.6.!.8.|
# |7  !   !...|7 9!7  !  9|  9!...!...|
# |---+---+---|---+---+---|---+---+---|
# | 23! 23!...|...! 23! 23|  3!...! 23|
# |4 6!4 6!.8.|.5.!  6!4 6|   !.1.!   |
# |7  !   !...|...!7  !  9|  9!...!7 9|
# |---+---+---|---+---+---|---+---+---|
# | 23!...! 2 | 23!123!123|...! 2 ! 23|
# | 56!.9.! 56|   !  6!  6|.4.! 5 ! 5 |
# |7  !...!7  |78 !78 ! 8 |...!7  !7  |
# +===========+===========+===========+


import unittest
import SuDoKuO
    
class SoDuKo_test(unittest.TestCase):
    
    # Invoked before each test method
    def setUp(self):
        self.sumo = SuDoKuO.SuDoKu("8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..")
        self.inva = SuDoKuO.SuDoKu("8....8.....36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..")
        
    def test_CONSTANTS_1(self):
        self.assertEqual(self.sumo.DIGS,(1,2,3,4,5,6,7,8,9))
    
    def test_get_1(self):
        self.assertEqual(self.sumo.get(0,0),8)
    
    def test_get_2(self):
        self.assertEqual(self.sumo.get(4,5),5)
    
    def test_get_3(self):
        self.assertEqual(self.sumo.get(8,6),4)
        
    def test_valid_1(self):
        self.assertTrue(self.sumo.v)
        
    def test_valid_2(self):
        self.assertFalse(self.inva.v)
        
    # 'This' functions
        
    def test_cps_this_row_1(self):
        self.assertEqual(self.sumo._cps_this_row(6,4),[(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8)])
        
    def test_cps_this_col_1(self):
        self.assertEqual(self.sumo._cps_this_col(6,4),[(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4)])
        
    def test_cps_this_box_1(self):
        self.assertEqual(self.sumo._cps_this_box(1,8),[(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)])
        
    def test_this_row_1(self):
        self.assertEqual(self.sumo.this_row(7,8),[0,0,8,5,0,0,0,1,0])
        
    def test_this_col_1(self):
        self.assertEqual(self.sumo.this_col(0,7),[0,0,0,0,0,3,6,1,0])
        
    def test_this_box_1(self):
        self.assertEqual(self.sumo.this_box(3,5),[0,0,7,0,4,5,1,0,0])
        
    # 'All' functions
    
    def test__cps_rows_1(self):
        self.assertEqual(self.sumo._cps_rows(),[[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8)],
                                                [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)],
                                                [(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8)],
                                                [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8)],
                                                [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8)],
                                                [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8)],
                                                [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8)],
                                                [(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8)],
                                                [(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8)]])
        
    def test__cps_cols_1(self):
        self.assertEqual(self.sumo._cps_cols(),[[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0)],        
                                                [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1)],
                                                [(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)],
                                                [(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3)],
                                                [(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4)],
                                                [(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5)],
                                                [(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6)],
                                                [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7)],
                                                [(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8)]])
        
    def test__cps_boxs_1(self):
        self.assertEqual(self.sumo._cps_boxs(),[[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],
                                                [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
                                                [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
                                                [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
                                                [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
                                                [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
                                                [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
                                                [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
                                                [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]])
        
    def test__cps_ares_1(self):
        self.assertEqual(self.sumo._cps_areas(),[[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8)],
                                                [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)],
                                                [(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8)],
                                                [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8)],
                                                [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8)],
                                                [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8)],
                                                [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8)],
                                                [(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8)],
                                                [(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8)],
                                                [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0)],
                                                [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1)],
                                                [(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)],
                                                [(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3)],
                                                [(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4)],
                                                [(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5)],
                                                [(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6)],
                                                [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7)],
                                                [(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8)],
                                                [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],
                                                [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
                                                [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
                                                [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
                                                [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
                                                [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
                                                [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
                                                [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
                                                [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]])
    
    # _cps_to_val()
        
    def test_csp_to_val_1(self):
        self.assertEqual(self.sumo.this_row(7,3), self.sumo._cps_to_val(self.sumo._cps_this_row(7,3)))
        
    def test_csp_to_val_2(self):
        self.assertEqual(self.sumo.this_col(7,3), self.sumo._cps_to_val(self.sumo._cps_this_col(7,3)))
        
    def test_csp_to_val_3(self):
        self.assertEqual(self.sumo.this_box(7,3), self.sumo._cps_to_val(self.sumo._cps_this_box(7,3)))
        
    def test_csp_to_val_4(self):
        self.assertEqual(self.sumo.rows(), self.sumo._cps_to_val(self.sumo._cps_rows()))
        
    def test_csp_to_val_5(self):
        self.assertEqual(self.sumo.cols(), self.sumo._cps_to_val(self.sumo._cps_cols()))
        
    def test_csp_to_val_6(self):
        self.assertEqual(self.sumo.boxs(), self.sumo._cps_to_val(self.sumo._cps_boxs()))
        
    # Subdeviding functions
    
    def test_slice9in3_hori_1(self):
        self.assertEqual(self.sumo._slice9in3_hori([1,2,3,4,5,6,7,8,9]), [[1,2,3],[4,5,6],[7,8,9]])
        
    def test_slice9in3_vert_1(self):
        self.assertEqual(self.sumo._slice9in3_vert([1,2,3,4,5,6,7,8,9]), [[1,4,7],[2,5,8],[3,6,9]])
        
    def test_area_cross_1(self):
        self.assertEqual(self.sumo.area_cross([1,2,3,4,3],[3,4,5,6]),[[1,2],[3,4],[5,6]])

    #------ locical functions (returning booleans) -----------------------------

    def test_cps_allinone_row_1(self):
        self.assertTrue(self.sumo.cps_allinone_row(self.sumo._cps_rows()[1]))

    def test_cps_allinone_row_2(self):
        self.assertFalse(self.sumo.cps_allinone_row(self.sumo._cps_cols()[2]))
        
    def test_cps_allinone_col_1(self):
        self.assertTrue(self.sumo.cps_allinone_col(self.sumo._cps_cols()[3]))
        
    def test_cps_allinone_col_2(self):
        self.assertFalse(self.sumo.cps_allinone_col(self.sumo._cps_rows()[4]))

    def test_cps_allinone_box_1(self):
        self.assertTrue(self.sumo.cps_allinone_box(self.sumo._cps_boxs()[5]))

    def test_cps_allinone_box_2(self):
        self.assertFalse(self.sumo.cps_allinone_box(self.sumo._cps_rows()[6]))
    
    #------ Only functions
    
    def test_only_free_cells_1(self):
        self.assertEqual(self.sumo.only_free_cells(self.sumo._cps_this_box(8,8)), [(6,6),(7,6),(7,8),(8,7),(8,8)])
        
    def test_only_n_notin_row_1(self):
        self.assertEqual(self.sumo.only_n_notin_row(self.sumo._cps_this_box(4,6),5),[(5,6),(5,7),(5,8)])
        
    def test_only_n_notin_col_1(self):
        self.assertEqual(self.sumo.only_n_notin_col(self.sumo._cps_this_box(4,0),8),[(3,1),(4,1),(5,1)])
        
    def test_only_pen_n_in_cell_1(self):
        s = self.sumo
        s.pencil()
        b = s._cps_this_box(0,8)
        self.assertEqual(s.only_pen_n_in_cell(3,b),[(0,6),(0,8),(2,8)])
        
    def test_only_cps_in_cps_1(self):
        boxa = self.sumo._cps_this_box(4,4)
        cola = self.sumo._cps_this_col(4,4)
        xrsa = self.sumo.only_cps_in_cps(boxa,cola) # Box in Col
        self.assertEqual(set(xrsa),set([(3,4),(4,4),(5,4)])) # order of elements is not significant
        
    def test_only_cps_in_cps_2(self):
        boxa = self.sumo._cps_this_box(4,4)
        cola = self.sumo._cps_this_col(4,4)
        xrsa = self.sumo.only_cps_in_cps(cola,boxa) # Col in Box
        self.assertEqual(set(xrsa),set([(3,4),(4,4),(5,4)])) # order of elements is not significant
        
    def test_only_cps_notin_cps_3(self):
        boxa = self.sumo._cps_this_box(4,4)
        cola = self.sumo._cps_this_col(4,4)
        xrsa = self.sumo.only_cps_notin_cps(cola,boxa) # Col - Box
        self.assertEqual(set(xrsa),set([(0,4),(1,4),(2,4),(6,4),(7,4),(8,4)])) # order of elements is not significant
        
    def test_only_cps_notin_cps_4(self):
        boxa = self.sumo._cps_this_box(4,4)
        cola = self.sumo._cps_this_col(4,4)
        xrsa = self.sumo.only_cps_notin_cps(boxa,cola) # Box - Col
        self.assertEqual(set(xrsa),set([(3,3),(3,5),(4,3),(4,5),(5,3),(5,5)])) # order of elements is not significant
           
    #------ Pencil functions --------------------------------------------------
    
    def test_p_count_in_cps_1(self):
        cps_a = self.sumo._cps_this_row(8,8)
        res = self.sumo._p_count_in_cps(3,cps_a)
        #print self.sumo.show_big()
        #print "cps_a", cps_a
        #print "pensi", self.sumo.p_for_cpsXXX(cps_a)
        #print "cnt3:", res
        self.assertEqual(res,5)
    
    def test_p_for_cpsXXX(self):
        cps_a = self.sumo._cps_this_box(1,1)
        self.assertEqual(self.sumo.p_for_cpsXXX(cps_a),[set([]),set([1,2,4,6]),set([2,4,5,6,9]),set([1,2,4,5,9]),set([1,2,4]),set([]),set([1,4,5,6]),set([]),set([4,5,6])])
        
    #def test_only_n_notin_row