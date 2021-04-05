
import SuDoKuX

with open(r"../data/flower5_pol200508.txt", 'r') as fil_in:
    for line in fil_in:
        line = line.strip().replace(',', '')
        print(f"input ->  {line.replace('0','.')}")
        SuDoKuX.r(line, True)
