
from string import maketrans
import copy

import SuDoKu_simple
import SuDoKuO


class SuDoKuNrmlz(SuDoKuO.SuDoKu):
    """ My SuDoKu class + Normalisation Analysis end Transformations """

    def __init__(self, str_ini):
        SuDoKuO.SuDoKu.__init__(self, str_ini)
        self._norm = ""

    def clean_all_but_m(self):
        """ Reset percil marks ect. since they make no sence with the changed data """
        self.p = [[set() for i in range(9)] for j in range(9)]  # Empty (empty lists) pencil-matrix
        self.rec = list()  # Track record of solving tactics steps

    def permute(self):
        """ Permute the matrix - so the order become 123456789 """
        str_alpha = "abcdefghi."
        str_numrc = "123456789."

        str_org = self.show_line()
        str_origi = str()
        for str_c in str_org.replace('.',''):
            if not str_c in str_origi:
                str_origi += str_c
        #print "local order: {}".format(str_origi)
        trantab = maketrans(str_origi+'.', str_alpha)
        str_a = str_org.translate(trantab)
        trantab = maketrans(str_alpha, str_numrc)
        str_p = str_a.translate(trantab)
        self.m = [[int(str_p[j * 9 + i].replace('.', '0')) for i in range(9)] for j in range(9)]
        self.clean_all_but_m()
        return

    def flip_h(self):
        """ Flip the matrix - horizontally """
        lst_t = self.m
        self.m = [lst_v[::-1] for lst_v in lst_t]
        self.clean_all_but_m()

    def flip_v(self):
        """ Flip the matrix - vertically """
        lst_t = self.m
        self.m = lst_t[::-1]
        self.clean_all_but_m()

    def turn_r(self):
        """ Turn the maxrix 90 degrees - right """
        self.m = [col[::-1] for col in self.cols()]

    def turn_l(self):
        """ Turn the maxrix 90 degrees - left """
        self.m = [col for col in self.cols()][::-1]


if __name__ == '__main__':

    str_s = ".4.8.52...2..4..5.5.......4.9...312.1.6.78..337.9.4.8......67....8359.1..19..76.."
    # S = SuDoKuNrmlz(str_s)
    # print "Original\n", S
    # S.permute()
    # print "Permuted\n", S
    # S.flip_v()
    # print "Flip-V\n", S
    # S.flip_h()
    # print "Flip-H\n", S

    print "# Normalizing candidates..."
    S = SuDoKuNrmlz(str_s)
    # lst_nc = [S, copy.deepcopy(S), copy.deepcopy(S), copy.deepcopy(S)]
    # for n in [1,3]:
    #     lst_nc[n].flip_h()
    # for n in [2,3]:
    #     lst_nc[n].flip_v()
    # for sdk in lst_nc:
    #     print sdk
    print "\n# Auto multiplyer"
    lst_sdk = [S]
    # Multiply, and flip H
    lst_add = [SuDoKuNrmlz(sdk.show_line()) for sdk in lst_sdk]
    for sdk in lst_add:
        sdk.flip_h()
    lst_sdk.extend(lst_add)
    # Multiply, and flip V
    lst_add = [SuDoKuNrmlz(sdk.show_line()) for sdk in lst_sdk]
    for sdk in lst_add:
        sdk.flip_v()
    lst_sdk.extend(lst_add)
    # Copy to Left twist, and Right twist
    lst_lft = [SuDoKuNrmlz(sdk.show_line()) for sdk in lst_sdk]
    lst_rgt = [SuDoKuNrmlz(sdk.show_line()) for sdk in lst_sdk]
    # Multiply, and Left twist
    lst_add = [SuDoKuNrmlz(sdk.show_line()) for sdk in lst_lft]
    for sdk in lst_add:
        sdk.turn_l() # turn 90
    lst_lft.extend(lst_add)
    for sdk in lst_add:
        sdk.turn_l() # turn 180
    lst_lft.extend(lst_add)
    for sdk in lst_add:
        sdk.turn_l() # turn 270
    lst_lft.extend(lst_add)
    lst_sdk.extend(lst_lft)
    # Multiply, and Right twist
    lst_add = [SuDoKuNrmlz(sdk.show_line()) for sdk in lst_rgt]
    for sdk in lst_add:
        sdk.turn_r() # turn 90
    lst_rgt.extend(lst_add)
    for sdk in lst_add:
        sdk.turn_r() # turn 180
    lst_rgt.extend(lst_add)
    for sdk in lst_add:
        sdk.turn_r() # turn 270
    lst_rgt.extend(lst_add)
    lst_sdk.extend(lst_rgt)

    print lst_sdk
    for sdk in lst_sdk:
        print sdk.show_line()
    print len(lst_sdk)
    lst_sdk = list(set([sdk.show_line() for sdk in lst_sdk]))
    lst_sdk.sort()
    for sdk in lst_sdk:
        print sdk
    print len(lst_sdk)

    print lst_sdk[0]
    Sn = SuDoKuNrmlz(lst_sdk[0])
    Sp = SuDoKuNrmlz(lst_sdk[0])
    Snp = SuDoKuNrmlz(lst_sdk[0])
    Sp.permute()
    Snp.permute()
    print S
    print Sn
    print Sp
    print Snp
    S.slap()
    print S.stats()
    Sn.slap()
    print Sn.stats()
    Sp.slap()
    print Sp.stats()
    Snp.slap()
    print Snp.stats()
