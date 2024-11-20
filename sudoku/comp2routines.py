
*** Dont use this, use /ec_sudoku/* instead ***


import SuDoKuS


with open(r"../data/speed/SolvedLG.txt", 'r') as fil_in:
    for line in fil_in:
        line = line.split('#')[0].strip().replace(',', '')
        print(f"input->   {line.replace('0','.')}")
        lst_minr = SuDoKuS.minr(line)
        print(f"<-minr: {lst_minr}")
        lst_rolf = SuDoKuS.rolf(line)
        print(f"<-rolf: {lst_rolf}")
