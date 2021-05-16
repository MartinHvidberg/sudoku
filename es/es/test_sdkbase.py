import unittest
import sdk_base
#import sdk_coms as sdk_base  # To test if sdk_base functionality inherits to sdk_coms, Rename all 'sdk_base.SDK_base()'

SDKZ = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'  # A completely empty SuDoKu grid
SDKI = '100000002090400050006000700050903000000070000000850040700000600030009080002000001'  # Some hard SuDoKu, Maybe 'the monster'
SDKA = '703108459900060800000000000010290367075003008000701000002070015086350020000010000'  # A (random) SuDoKu from file 13a at http://lipas.uwasa.fi/~timan/sudoku/
SDKC = '763128459924567831851934276418295367275643198639781542342876915186359724597412683'  # Solution to SDKA


class MyTestCase(unittest.TestCase):

    def test_n_kl(self):
        sdk = sdk_base.SDK_base(SDKZ)
        self.assertEqual((6, 0), sdk.n2kl(6))
        self.assertEqual((4, 1), sdk.n2kl(13))
        self.assertEqual((3, 7), sdk.n2kl(66))
        # kl2n  - TBI

    def test_cps_this_x(self):
        sdk = sdk_base.SDK_base(SDKZ)
        self.assertEqual([(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)],sdk.cps_this_col(1,4))  # Col
        self.assertEqual([(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8)],sdk.cps_this_col(8,7))
        self.assertEqual([(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7)],sdk.cps_this_row(8,7))  # Row
        self.assertEqual([(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)],sdk.cps_this_row(6,2))
        self.assertEqual([(3,6),(4,6),(5,6),(3,7),(4,7),(5,7),(3,8),(4,8),(5,8)],sdk.cps_this_box(3,8))  # Box
        self.assertEqual([(0,3),(1,3),(2,3),(0,4),(1,4),(2,4),(0,5),(1,5),(2,5)],sdk.cps_this_box(0,5))

    def test_init(self):
        sdk = sdk_base.SDK_base(SDKI)
        self.assertEqual([[1,0,0,0,0,0,0,0,2],
                          [0,9,0,4,0,0,0,5,0],
                          [0,0,6,0,0,0,7,0,0],
                          [0,5,0,9,0,3,0,0,0],
                          [0,0,0,0,7,0,0,0,0],
                          [0,0,0,8,5,0,0,4,0],
                          [7,0,0,0,0,0,6,0,0],
                          [0,3,0,0,0,9,0,8,0],
                          [0,0,2,0,0,0,0,0,1]], sdk.get())

    def test_show(self):
        sdk = sdk_base.SDK_base(SDKI)
        print(sdk.show_small())
        self.assertEqual("""+---+---+---+
|1  |   |  2|
| 9 |4  | 5 |
|  6|   |7  |
+---+---+---+
| 5 |9 3|   |
|   | 7 |   |
|   |85 | 4 |
+---+---+---+
|7  |   |6  |
| 3 |  9| 8 |
|  2|   |  1|
+---+---+---+""", sdk.show_small())


    def test_get_set(self):
        sdk = sdk_base.SDK_base(SDKZ)
        self.assertEqual(0, sdk.get(6, 6))
        self.assertTrue(sdk.set(6, 6, 6))
        self.assertEqual(6, sdk.get(6, 6))
        self.assertTrue(sdk.set(2, 8, 9))
        self.assertEqual(9, sdk.get(2, 8))
        # Illegal inserts
        self.assertFalse(sdk.set(5, 6, 6))  # Duplicate 6 in row
        self.assertFalse(sdk.set(6, 0, 6))  # Duplicate 6 in col
        self.assertFalse(sdk.set(7, 8, 6))  # Duplicate 6 in box

    def test_cols_rows_boxs_areas(self):
        sdk = sdk_base.SDK_base(SDKI)
        exp = [ [1,0,0,0,0,0,0,0,2],
                [0,9,0,4,0,0,0,5,0],
                [0,0,6,0,0,0,7,0,0],
                [0,5,0,9,0,3,0,0,0],
                [0,0,0,0,7,0,0,0,0],
                [0,0,0,8,5,0,0,4,0],
                [7,0,0,0,0,0,6,0,0],
                [0,3,0,0,0,9,0,8,0],
                [0,0,2,0,0,0,0,0,1]]
        self.assertEqual(exp, sdk.rows())
        exp = [ [1,0,0,0,0,0,7,0,0],
                [0,9,0,5,0,0,0,3,0],
                [0,0,6,0,0,0,0,0,2],
                [0,4,0,9,0,8,0,0,0],
                [0,0,0,0,7,5,0,0,0],
                [0,0,0,3,0,0,0,9,0],
                [0,0,7,0,0,0,6,0,0],
                [0,5,0,0,0,4,0,8,0],
                [2,0,0,0,0,0,0,0,1]]
        self.assertEqual(exp, sdk.cols())
        exp = [ [1,0,0,0,9,0,0,0,6],
                [0,0,0,4,0,0,0,0,0],
                [0,0,2,0,5,0,7,0,0],
                [0,5,0,0,0,0,0,0,0],
                [9,0,3,0,7,0,8,5,0],
                [0,0,0,0,0,0,0,4,0],
                [7,0,0,0,3,0,0,0,2],
                [0,0,0,0,0,9,0,0,0],
                [6,0,0,0,8,0,0,0,1]]
        self.assertEqual(exp, sdk.boxs())
        exp = [ [1,0,0,0,0,0,0,0,2],
                [0,9,0,4,0,0,0,5,0],
                [0,0,6,0,0,0,7,0,0],
                [0,5,0,9,0,3,0,0,0],
                [0,0,0,0,7,0,0,0,0],
                [0,0,0,8,5,0,0,4,0],
                [7,0,0,0,0,0,6,0,0],
                [0,3,0,0,0,9,0,8,0],
                [0,0,2,0,0,0,0,0,1],
                [1,0,0,0,0,0,7,0,0],
                [0,9,0,5,0,0,0,3,0],
                [0,0,6,0,0,0,0,0,2],
                [0,4,0,9,0,8,0,0,0],
                [0,0,0,0,7,5,0,0,0],
                [0,0,0,3,0,0,0,9,0],
                [0,0,7,0,0,0,6,0,0],
                [0,5,0,0,0,4,0,8,0],
                [2,0,0,0,0,0,0,0,1],
                [1,0,0,0,9,0,0,0,6],
                [0,0,0,4,0,0,0,0,0],
                [0,0,2,0,5,0,7,0,0],
                [0,5,0,0,0,0,0,0,0],
                [9,0,3,0,7,0,8,5,0],
                [0,0,0,0,0,0,0,4,0],
                [7,0,0,0,3,0,0,0,2],
                [0,0,0,0,0,9,0,0,0],
                [6,0,0,0,8,0,0,0,1]]
        self.assertEqual(exp, sdk.areas())

    def test_this_x(self):
        sdk = sdk_base.SDK_base(SDKI)
        self.assertEqual([0,0,6,0,0,0,7,0,0],sdk.this_row(4,2))  # Row
        self.assertEqual([7,0,0,0,0,0,6,0,0],sdk.this_row(5,6))
        self.assertEqual([0,0,0,0,7,5,0,0,0],sdk.this_col(4,3))  # Col
        self.assertEqual([0,4,0,9,0,8,0,0,0],sdk.this_col(3,7))
        self.assertEqual([9,0,3,0,7,0,8,5,0],sdk.this_box(4,5))  # Box

    def test_valid_complete(self):
        # validate  - Difficult to test, as software won't let me build illegal data :-(
        # is_valid  - Quite trivial, but no excuse not to test!
        # complete
        sdki = sdk_base.SDK_base(SDKI)
        self.assertFalse(sdki.is_complete())
        sdkc = sdk_base.SDK_base(SDKC)
        self.assertTrue(sdkc.is_complete())


if __name__ == '__main__':
    unittest.main()
