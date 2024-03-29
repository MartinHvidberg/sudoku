def same_row(i,j): return (i//9 == j//9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i//27 == j//27 and i%9//3 == j%9//3)

"""
     0,  1,  2,  | 3,  4,  5, | 6, 7, 8, 
     9, 10, 11,  |12, 13, 14, |15, 16, 17, 
     18, 19, 20, |21, 22, 23, |24, 25, 26, 
     
     27, 28, 29, |30, 31, 32, |33, 34, 35, 
     36, 37, 38, |39, 40, 41, |42, 43, 44, 
     45, 46, 47, |48, 49, 50, |51, 52, 53, 
     
     54, 55, 56, |57, 58, 59, |60, 61, 62, 
     63, 64, 65, |66, 67, 68, |69, 70, 71, 
     72, 73, 74, |75, 76, 77, |78, 79, 80
"""

print(f"TL: {[n for n in range(81) if same_block(n,10)]}")
print(f"TC: {[n for n in range(81) if same_block(n,13)]}")
print(f"TR: {[n for n in range(81) if same_block(n,16)]}")
print(f"CL: {[n for n in range(81) if same_block(n,37)]}")
print(f"CC: {[n for n in range(81) if same_block(n,40)]}")
print(f"CR: {[n for n in range(81) if same_block(n,43)]}")
print(f"LL: {[n for n in range(81) if same_block(n,64)]}")
print(f"LC: {[n for n in range(81) if same_block(n,67)]}")
print(f"LR: {[n for n in range(81) if same_block(n,70)]}")

# for i in range(81):
#     print(f"--: {[n for n in range(81) if same_block(n, i)]}")
