
*** Dont use this, use /ec_sudoku/* instead ***

import unittest

import SuDoKu_Comm


class MyTestCase(unittest.TestCase):
    def test_set_empty_to_zero(self):
        str_samp1 = "13.475269527.6941896481273.679154.23.456289712817.35464569371.27.258639489324.657"
        str_rslt1 = SuDoKu_Comm.set_empty_to_zero(str_samp1)
        self.assertEqual(str_rslt1, str_samp1.replace('.', '0'))
        str_samp2 = "13a475269527b6941896481273c679154d23e456289712817f35464569371g27h258639489324i657"  # now with abc
        str_rslt2 = SuDoKu_Comm.set_empty_to_zero(str_samp2)
        self.assertEqual(str_rslt2, str_samp1.replace('.', '0'))  # re-use samp1 for reference


if __name__ == '__main__':
    unittest.main()
