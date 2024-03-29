
import SuDoKuX

with open(r"../data/text/find_doubles.txt", 'r') as fil_in:
    for line in fil_in:
        line = line.strip()  # remove trailing \n
        str_lin = line.split('#')[0].replace('.', '0').strip()
        print(f"input ->  {line}\n      -> |{str_lin}|")
        SuDoKuX.r(str_lin, True)

# The screen-output of this is also used as input to Samurai-solving, so don't change it for no reason...!
