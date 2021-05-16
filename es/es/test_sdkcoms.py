import unittest
import sdk_coms

SDKZ = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'  # A completely empty SuDoKu grid
SDKI = '100000002090400050006000700050903000000070000000850040700000600030009080002000001'  # Some hard SuDoKu, Maybe 'the monster'
SDKA = '703108459900060800000000000010290367075003008000701000002070015086350020000010000'  # A (random) SuDoKu from file 13a at http://lipas.uwasa.fi/~timan/sudoku/
SDKC = '763128459924567831851934276418295367275643198639781542342876915186359724597412683'  # Solution to SDKA


class MyTestCase(unittest.TestCase):

    def test_n_kl(self):  # Just a carry-over from _base. This should be deleted here.
        sdk = sdk_coms.SDK_coms(SDKZ)
        self.assertEqual((6, 0), sdk.n2kl(6))
        self.assertEqual((4, 1), sdk.n2kl(13))
        self.assertEqual((3, 7), sdk.n2kl(66))


if __name__ == '__main__':
    unittest.main()
