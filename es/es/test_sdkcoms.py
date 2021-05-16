import unittest
import sdk_coms

SDKI = '100000002090400050006000700050903000000070000000850040700000600030009080002000001'
SDKC = ''  # TBD a completed SuDoKu
SDKZ = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'


class MyTestCase(unittest.TestCase):

    def test_n_kl(self):  # Just a carry-over from _base. This should be deleted here.
        sdk = sdk_coms.SDK_coms(SDKZ)
        self.assertEqual((6, 0), sdk.n2kl(6))
        self.assertEqual((4, 1), sdk.n2kl(13))
        self.assertEqual((3, 7), sdk.n2kl(66))


if __name__ == '__main__':
    unittest.main()
