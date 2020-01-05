import unittest
import SuDoKuS

class SuDoKuTestCase(unittest.TestCase):
    """ Tests for SuDoKuS.py """

    str_test_sdk_1 = ".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76.."  # Legal
    str_test_sdk_2 = ".4.8.52...2..4..5.5...X...4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76.."  # Error
    str_test_sdk_3 = "812519116725321222133136831341243445957667353466854768574778579288485687699992994"  # Solved
    lst_test_sdk_1 = [0,4,0,8,0,5,2,0,0,0,2,0,0,4,0,0,5,0,5,0,0,0,0,0,0,0,4,0,9,0,0,0,3,1,2,0,1,0,6,0,7,8,0,0,3,3,7,0,9,0,4,0,8,0,0,0,0,0,0,6,7,0,0,0,0,8,3,5,9,0,1,0,0,1,9,0,0,7,6,0,0]

    # str2loi(str_in) - tests
    def test_str2loi(self):
        """...?"""
        self.assertEqual(SuDoKuS.str2loi(0), [])  # input wrong type
        self.assertEqual(SuDoKuS.str2loi(""), [])  # input too short
        self.assertEqual(SuDoKuS.str2loi(SuDoKuTestCase.str_test_sdk_2),[])  # input illegal char
        self.assertEqual(SuDoKuS.str2loi(SuDoKuTestCase.str_test_sdk_1),SuDoKuTestCase.lst_test_sdk_1)  # Valid input

    def test_show_small(self):
        """"""
        self.assertEqual(SuDoKuS.show_small(SuDoKuTestCase.lst_test_sdk_1),
            """+---+---+---+
| 4 |8 5|2  |
| 2 | 4 | 5 |
|5  |   |  4|
+---+---+---+
| 9 |  3|12 |
|1 6| 78|  3|
|37 |9 4| 8 |
+---+---+---+
|   |  6|7  |
|  8|359| 1 |
| 19|  7|6  |
+---+---+---+""")

    def test_list_empty_fields_id(self):
        self.assertEqual(SuDoKuS.list_empty_fields_id(SuDoKuTestCase.lst_test_sdk_1),
            [0,2,4,7,8,9,11,12,14,15,17,19,20,21,22,23,24,25,27,29,30,31,35,37,39,
             42,43,47,49,51,53,54,55,56,57,58,61,62,63,64,69,71,72,75,76,79,80])

    def test_sudoku_is_solved(self):
        self.assertTrue(SuDoKuS.sudoku_is_solved(SuDoKuS.str2loi(SuDoKuTestCase.str_test_sdk_3)))
        self.assertFalse(SuDoKuS.sudoku_is_solved(SuDoKuS.str2loi(SuDoKuTestCase.str_test_sdk_1)))
        self.assertFalse(SuDoKuS.sudoku_is_solved(SuDoKuTestCase.lst_test_sdk_1))

if __name__ == '__main__':
    unittest.main()