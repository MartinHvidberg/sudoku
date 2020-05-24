import pprint

lst_sdk_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

def no_init_diff(str_ou, str_in):
    return True

def is_valid_sol(str_ou):
    return True


with open('speed_comp_others.log', 'r') as fil_i:
    lst_in = [l.strip() for l in fil_i.readlines() if l != '\n']

num_cnt = 0
dic_sol = dict()  # Dictionary summarising times per Solver
dic_sdk = dict()  # Dictionary summarising times per SoDuKo
for lin in lst_in:
    if lin[0] == "#":
        if all([tok in lin for tok in ['<', '>', ':']]):
            lin.replace(',', ';')
            for tok in ['<', '>', ':']:
                lin = lin.replace(tok, ',')
            try:
                str_nam, str_in, str_ou, str_tim = [tok.strip() for tok in lin[1:].split(',')]
            except ValueError:
                print(f"Can't split: {lin}")
                continue
            if len(str_in) == 81 and all([tok in lst_sdk_chars for tok in str_in]):
                if len(str_ou) == 81 and all([tok in lst_sdk_chars for tok in str_ou]):
                    if str_tim[:3] == 'in ' and str_tim[-3:] == ' ms':
                        try:
                            num_tim = int(str_tim[3:-3])
                        except ValueError:
                            print(f"Warning: malformat time: {str_tim}")
                            continue
                        if no_init_diff(str_ou, str_in):
                            if is_valid_sol(str_ou):
                                # add_the_score
                                str_nam = str_nam.lstrip('#').strip()
                                if str_nam not in dic_sol.keys():
                                    dic_sol[str_nam] = list()
                                dic_sol[str_nam].append((str_in, str_ou, str_tim[3:-3].strip()))
                                if str_in not in dic_sdk.keys():
                                    dic_sdk[str_in] = list()
                                dic_sdk[str_in].append((str_nam, str_tim[3:-3].strip()))
                            else:
                                print("Warning: Not valid solution")
                        else:
                            print("Warning: Initial different in and ou")
                else:
                    print("Warning: Illegal char in putput")
            else:
                print("Warning: Illegal char in input")
            num_cnt += 1
        else:
            print(f"WARNING: Unexpected line format in: {lin}")
print(f"Found {num_cnt} data lines")

pprint.pprint(dic_sol)
pprint.pprint(dic_sdk)