
import copy

a = [{'1', '2', '3'}, {'4'}, {'5', '6'}]

def change(list_x):
    for n in range(len(list_x)):
        chgn = list_x[n]
        chgn.discard('3')
        list_x[n] = chgn
    return list_x

print(f"org. a: {a}")
b = change(copy.deepcopy(a))
print(f"new. b: {b}")
print(f"???. a: {a}")

