import unittest
import sdk_hums
import sdk_prmu

# refsdk = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789!"#{}&*/()=?+-@£$[]'
lol_u = [
        ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e'],
        ['E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I'],
        ['j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n'],
        ['N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R'],
        ['s', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w'],
        ['W', 'x', 'X', 'y', 'Y', 'z', 'Z', 'Ø', '1'],
        ['2', '3', '4', '5', '6', '7', '8', '9', '!'],
        ['"', '#', '{', '}', '&', '*', '/', '(', ')'],
        ['=', '?', '+', '-', '@', '£', '$', '[', ']']
    ]


class MyTestCase(unittest.TestCase):

    def test_turns(self):
        sdk = sdk_hums.SdkHums("")
        sdk.set_matrix(lol_u)  # Brute force overwrite the matrix with this (invalid) contents

        str_ref = """+---+---+---+
|aAb|BcC|dDe|
|EfF|gGh|HiI|
|jJk|KlL|mMn|
+---+---+---+
|NoO|pPq|QrR|
|sSt|TuU|vVw|
|WxX|yYz|ZØ1|
+---+---+---+
|234|567|89!|
|"#{|}&*|/()|
|=?+|-@£|$[]|
+---+---+---+"""
        str_val = str(sdk.show_small())
        self.assertEqual(str_ref, str_val)

        # Turn it one nutch
        str_ref_tr1 = """+---+---+---+
|="2|WsN|jEa|
|?#3|xSo|JfA|
|+{4|XtO|kFb|
+---+---+---+
|-}5|yTp|KgB|
|@&6|YuP|lGc|
|£*7|zUq|LhC|
+---+---+---+
|$/8|ZvQ|mHd|
|[(9|ØVr|MiD|
|])!|1wR|nIe|
+---+---+---+"""
        sdktr1 = sdk_prmu.turn_r(sdk)
        str_val_tr1 = str(sdktr1.show_small())
        self.assertEqual(str_ref_tr1, str_val_tr1)

        # Turn it two nutch
        str_ref_tr2 = """+---+---+---+
|][$|£@-|+?=|
|)(/|*&}|{#"|
|!98|765|432|
+---+---+---+
|1ØZ|zYy|XxW|
|wVv|UuT|tSs|
|RrQ|qPp|OoN|
+---+---+---+
|nMm|LlK|kJj|
|IiH|hGg|FfE|
|eDd|CcB|bAa|
+---+---+---+"""
        sdktr2 = sdk_prmu.turn_r(sdktr1)
        str_val_tr2 = str(sdktr2.show_small())
        self.assertEqual(str_ref_tr2, str_val_tr2)

        # Turn it three nutch
        str_ref_tr3 = """+---+---+---+
|eIn|Rw1|!)]|
|DiM|rVØ|9([|
|dHm|QvZ|8/$|
+---+---+---+
|ChL|qUz|7*£|
|cGl|PuY|6&@|
|BgK|pTy|5}-|
+---+---+---+
|bFk|OtX|4{+|
|AfJ|oSx|3#?|
|aEj|NsW|2"=|
+---+---+---+"""
        sdktr3 = sdk_prmu.turn_r(sdktr2)
        str_val_tr3 = str(sdktr3.show_small())
        self.assertEqual(str_ref_tr3, str_val_tr3)

        # Turn it four nutch
        str_ref_tr4 = """+---+---+---+
|aAb|BcC|dDe|
|EfF|gGh|HiI|
|jJk|KlL|mMn|
+---+---+---+
|NoO|pPq|QrR|
|sSt|TuU|vVw|
|WxX|yYz|ZØ1|
+---+---+---+
|234|567|89!|
|"#{|}&*|/()|
|=?+|-@£|$[]|
+---+---+---+"""
        sdktr4 = sdk_prmu.turn_r(sdktr3)
        str_val_tr4 = str(sdktr4.show_small())
        self.assertEqual(str_ref_tr4, str_val_tr4)

        self.assertEqual(str_val, str_val_tr4)
        self.assertEqual(str_val_tr3, str(sdk_prmu.turn_l(sdktr4).show_small()))
        self.assertEqual(str_val_tr2, str(sdk_prmu.turn_l(sdktr3).show_small()))
        self.assertEqual(str_val_tr1, str(sdk_prmu.turn_l(sdktr2).show_small()))
        self.assertEqual(str_val, sdk_prmu.turn_l(sdktr1).show_small())


    def test_flips(self):
        sdk = sdk_hums.SdkHums("")
        sdk.set_matrix(lol_u)  # Brute force overwrite the matrix with this (invalid) contents

        str_ref = """+---+---+---+
|aAb|BcC|dDe|
|EfF|gGh|HiI|
|jJk|KlL|mMn|
+---+---+---+
|NoO|pPq|QrR|
|sSt|TuU|vVw|
|WxX|yYz|ZØ1|
+---+---+---+
|234|567|89!|
|"#{|}&*|/()|
|=?+|-@£|$[]|
+---+---+---+"""
        str_val = str(sdk.show_small())
        self.assertEqual(str_ref, str_val)

        # flip horizontal
        str_refflip_h = """+---+---+---+
|eDd|CcB|bAa|
|IiH|hGg|FfE|
|nMm|LlK|kJj|
+---+---+---+
|RrQ|qPp|OoN|
|wVv|UuT|tSs|
|1ØZ|zYy|XxW|
+---+---+---+
|!98|765|432|
|)(/|*&}|{#"|
|][$|£@-|+?=|
+---+---+---+"""
        sdkf_h = sdk_prmu.flip_h(sdk)
        str_valflip_h = str(sdkf_h.show_small())
        self.assertEqual(str_refflip_h, str_valflip_h)

        # Then flip Vertically
        str_refflip_hv = """+---+---+---+
|][$|£@-|+?=|
|)(/|*&}|{#"|
|!98|765|432|
+---+---+---+
|1ØZ|zYy|XxW|
|wVv|UuT|tSs|
|RrQ|qPp|OoN|
+---+---+---+
|nMm|LlK|kJj|
|IiH|hGg|FfE|
|eDd|CcB|bAa|
+---+---+---+"""
        sdkf_hv = sdk_prmu.flip_v(sdkf_h)
        str_valflip_hv = str(sdkf_hv.show_small())
        self.assertEqual(str_refflip_hv, str_valflip_hv)

        # Then flip Horizontal, again
        str_refflip_hvh = """+---+---+---+
|=?+|-@£|$[]|
|"#{|}&*|/()|
|234|567|89!|
+---+---+---+
|WxX|yYz|ZØ1|
|sSt|TuU|vVw|
|NoO|pPq|QrR|
+---+---+---+
|jJk|KlL|mMn|
|EfF|gGh|HiI|
|aAb|BcC|dDe|
+---+---+---+"""
        sdkf_hvh = sdk_prmu.flip_h(sdkf_hv)
        str_valflip_hvh = str(sdkf_hvh.show_small())
        self.assertEqual(str_refflip_hvh, str_valflip_hvh)

        # Then flip Vertical, again
        str_refflip_hvhv = str_ref  # we are back to the original...
        sdkf_hvhv = sdk_prmu.flip_v(sdkf_hvh)
        str_valflip_hvhv = str(sdkf_hvhv.show_small())
        self.assertEqual(str_refflip_hvhv, str_valflip_hvhv)

        self.assertEqual(str_val, str_valflip_hvhv)
        self.assertEqual(str_valflip_hvh, str(sdk_prmu.flip_v(sdkf_hvhv).show_small()))
        self.assertEqual(str_valflip_hv, str(sdk_prmu.flip_h(sdkf_hvh).show_small()))
        self.assertEqual(str_valflip_h, str(sdk_prmu.flip_v(sdkf_hv).show_small()))
        self.assertEqual(str_val, str(sdk_prmu.flip_h(sdkf_h).show_small()))


# turn & flip
# t_r2 = f_hv = t_l2 = f_vh = f_diagonal?

if __name__ == '__main__':
    unittest.main()
