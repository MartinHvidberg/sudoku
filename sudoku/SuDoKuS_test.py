import unittest
import SuDoKuS

class SmallNumericalFunctions(unittest.TestCase):

    def test_same_col(self):
        self.assertTrue(SuDoKuS.same_col(0,0))
        self.assertTrue(SuDoKuS.same_col(0,9))
        self.assertFalse(SuDoKuS.same_col(0,1))

    def test_same_row(self):
        self.assertTrue(SuDoKuS.same_row(0,0))
        self.assertTrue(SuDoKuS.same_row(0,2))
        self.assertFalse(SuDoKuS.same_row(0,9))

    def test_same_box(self):
        self.assertTrue(SuDoKuS.same_box(0,0))
        self.assertTrue(SuDoKuS.same_box(6,16))
        self.assertFalse(SuDoKuS.same_box(0,77))

class BuildUpFunctions(unittest.TestCase):

    def test_str2loi(self):
        self.assertEqual(SuDoKuS.str2loi(".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76.."), [0, 4, 0, 8, 0, 5, 2, 0, 0, 0, 2, 0, 0, 4, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 4, 0, 9, 0, 0, 0, 3, 1, 2, 0, 1, 0, 6, 0, 7, 8, 0, 0, 3, 3, 7, 0, 9, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 6, 7, 0, 0, 0, 0, 8, 3, 5, 9, 0, 1, 0, 0, 1, 9, 0, 0, 7, 6, 0, 0])

    def test_loi2sdk(self):
        loi = SuDoKuS.str2loi(".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..")
        sdk = SuDoKuS.loi2sdk(loi)
        self.assertEqual(sdk['s'], loi)
        self.assertEqual(sdk['p'], [{6,7,9},set(),{1,3,7},set(),{1,3,6,9},set(),set(),{3,6,7,9},{1,6,7,9},{6,7,8,9},set(),{1,3,7},{1,6,7},set(),{1},{3,8,9},set(),{1,6,7,8,9},set(),{3,6,8},{1,3,7},{1,2,6,7},{1,2,3,6,9},{1,2},{3,8,9},{3,6,7,9},set(),{4,8},set(),{4,5},{5,6},{6},set(),set(),set(),{5,6,7},set(),{5},set(),{2,5},set(),set(),{4,5,9},{4,9},set(),set(),set(),{2,5},set(),{1,2,6},set(),{5},set(),{5,6},{2,4},{3,5},{2,3,4,5},{1,2,4},{1,2,8},set(),set(),{3,4,9},{2,5,8,9},{2,4,6,7},{6},set(),set(),set(),set(),{4},set(),{2},{2,4},set(),set(),{2,4},{2,8},set(),set(),{3,4},{2,5,8}])
        self.assertEqual(sdk['sol'], set())
        self.assertEqual(sdk['bum'], False)

    def test_place(self):
        loi = SuDoKuS.str2loi(".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..")
        sdk = SuDoKuS.loi2sdk(loi)
        SuDoKuS.place(6, 12, sdk)
        loi_new = SuDoKuS.str2loi(".4.8.52...2.64..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..")
        self.assertEqual(sdk['s'], loi_new)
        self.assertEqual(sdk['p'], [{6,7,9},set(),{1,3,7},set(),{1,3,9},set(),set(),{3,6,7,9},{1,6,7,9},{7,8,9},set(),{1,3,7},{1,7},set(),{1},{3,8,9},set(),{1,7,8,9},set(),{3,6,8},{1,3,7},{1,2,7},{1,2,3,9},{1,2},{3,8,9},{3,6,7,9},set(),{4,8},set(),{4,5},{5},{6},set(),set(),set(),{5,6,7},set(),{5},set(),{2,5},set(),set(),{4,5,9},{4,9},set(),set(),set(),{2,5},set(),{1,2,6},set(),{5},set(),{5,6},{2,4},{3,5},{2,3,4,5},{1,2,4},{1,2,8},set(),set(),{3,4,9},{2,5,8,9},{2,4,6,7},{6},set(),set(),set(),set(),{4},set(),{2},{2,4},set(),set(),{2,4},{2,8},set(),set(),{3,4},{2,5,8}])

    def test_Guessing(self):
        loi = SuDoKuS.str2loi(".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..")
        sdk = SuDoKuS.loi2sdk(loi)
        lst_empty_fields = SuDoKuS.list_empty_fields_id(sdk)
        self.assertEqual(lst_empty_fields, [0,2,4,7,8,9,11,12,14,15,17,19,20,21,22,23,24,25,27,29,30,31,35,37,39,42,43,47,49,51,53,54,55,56,57,58,61,62,63,64,69,71,72,75,76,79,80])
        min_p_count = SuDoKuS.find_min_p_count(sdk)
        self.assertEqual(min_p_count, 1)
        min_p_cell = SuDoKuS.find_min_p_cell(sdk)
        self.assertEqual(min_p_cell, 14)
        guess = SuDoKuS.guess(min_p_cell, sdk)
        #self.assertEqual(guess, 1)

if __name__ == '__main__':
    unittest.main()
