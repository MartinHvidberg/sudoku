import unittest
import SuDoKu_simple

class SameCRB(unittest.TestCase):

    def test_same_col(self):
        self.assertTrue(SuDoKu_simple.same_col(0,0))
        self.assertTrue(SuDoKu_simple.same_col(0,9))
        self.assertFalse(SuDoKu_simple.same_col(0,1))

    def test_same_row(self):
        self.assertTrue(SuDoKu_simple.same_row(0,0))
        self.assertTrue(SuDoKu_simple.same_row(0,2))
        self.assertFalse(SuDoKu_simple.same_row(0,9))

    def test_same_box(self):
        self.assertTrue(SuDoKu_simple.same_box(0,0))
        self.assertTrue(SuDoKu_simple.same_box(6,16))
        self.assertFalse(SuDoKu_simple.same_box(0,77))

class Validate(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(SuDoKu_simple.valid('9265714833514862798749235165823671941492583677631..8252387..651617835942495612738'.replace('.', '0')))
        self.assertTrue(SuDoKu_simple.valid('9265714833514862798749235165823671941492583677631498252387..651617835942495612738'.replace('.', '0')))
        self.assertTrue(SuDoKu_simple.valid('9265714833514862798749235165823671941492583677631..825238794651617835942495612738'.replace('.', '0')))
        self.assertTrue(SuDoKu_simple.valid('926571483351486279874923516582367194149258367763149825238794651617835942495612738'.replace('.', '0')))
        self.assertFalse(SuDoKu_simple.valid('926571483351486279874923516582367194149258367763144825238799651617835942495612738'.replace('.', '0')))

class Done(unittest.TestCase):

    def test_done(self):
        self.assertFalse(SuDoKu_simple.done('9265714833514862798749235165823671941492583677631..8252387..651617835942495612738'.replace('.', '0')))
        self.assertFalse(SuDoKu_simple.done('9265714833514862798749235165823671941492583677631498252387..651617835942495612738'.replace('.', '0')))
        self.assertFalse(SuDoKu_simple.done('9265714833514862798749235165823671941492583677631..825238794651617835942495612738'.replace('.', '0')))
        self.assertTrue(SuDoKu_simple.done('926571483351486279874923516582367194149258367763149825238794651617835942495612738'.replace('.', '0')))  # full and valid
        self.assertFalse(SuDoKu_simple.done('926571483351486279874923516582367194149258367763144825238799651617835942495612738'.replace('.', '0')))  # full, but not valid

class Pencil(unittest.TestCase):

    def test_pencil(self):
        sdk1 = '.4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76..'.replace('.', '0')
        n, m = 2, 4
        # # Old pencil
        # self.assertEqual({'4', '5', '7'}, SuDoKu_simple.col_pencil(sdk1, n, m))
        # self.assertEqual({'4', '5'}, SuDoKu_simple.row_pencil(sdk1, n, m))
        # self.assertEqual({'4', '5', '8'}, SuDoKu_simple.box_pencil(sdk1, n, m))
        # self.assertEqual({'4', '5', '7', '8'}, SuDoKu_simple.pencil(sdk1, n, m))  # taken in any dimension
        # New pcl
        self.assertEqual({'1', '2', '3', '6', '8', '9'}, SuDoKu_simple.col_pcl(sdk1, n, m))
        self.assertEqual({'1', '2', '3', '6', '7', '8', '9'}, SuDoKu_simple.row_pcl(sdk1, n, m))
        self.assertEqual({'1', '2', '3', '6', '7', '9'}, SuDoKu_simple.box_pcl(sdk1, n, m))
        self.assertEqual({'1', '2', '3', '6', '9'}, SuDoKu_simple.pcl(sdk1, n, m))  # vacant in all dimensions


if __name__ == '__main__':
    unittest.main()
