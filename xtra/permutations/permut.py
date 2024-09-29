

"""
Playing around with possibilities, the real stuff is in SuDoKu_Norm.py
"""

All this 'self' nonsense will never work outside a class ...

def show_medium(lst_sdk):

    def p(i, j):
        return str(lst_sdk[i*9+j])

    def l(i):
        return ("| " + p(i, 0) + " " + p(i, 1) + " " + p(i, 2)
                + " | " + p(i, 3) + " " + p(i, 4) + " " + p(i, 5)
                + " | " + p(i, 6) + " " + p(i, 7) + " " + p(i, 8) + " |\n").replace('0', ' ')

    def q():
        v = '+ - - - + - - - + - - - +\n'
        return (v + l(0) + l(1) + l(2) + v + l(3) + l(4) + l(5) + v + l(6) + l(7) + l(8) + v).strip()

    if len(lst_sdk) == 81:
        return q()
    else:
        print(f"Wrong length list: {len(lst_sdk)}")


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


refsdk = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789!"#{}&*/()=?+-@£$[]'

print(show_medium(refsdk))
refsdk = turn_l(refsdk)
print(show_medium(refsdk))
refsdk = turn_l(refsdk)
print(show_medium(refsdk))
refsdk = turn_l(refsdk)
print(show_medium(refsdk))

