
# Bringing a sudoku on it's normal form

### Figure
Using the 81 digit long string representing the sudoku
1. Replace all non-0 with 1, thus generating a string of only 0 and 1, that is interpreted as a binary number N.
2. While looping through all possible (8?) solid permutations: 
The normal figure is the permutation where the binary number N becomes smallest.

### Substitution into order
Having transformed the SuDoKu, the original one - not the binary,  to it's normal Figure.
1. Find the first non-0 digit, and replace all occurrences of this digit with an 'a'
    Find the second and replace all occurrences with 'b'
    repeat until all numbers are substituted with letters
2. Replace all 'a'=1, 'b'=2, etc. 
    The digits now appear in order, with respect to first appearance.

### Appendix. Naming convention

Naming a SuDoKu by describing it's normal form + the permutation from the normal form.

Name has 4 parts. 2 parts to describe the normal form, and 2 to describe the permutation. All four parts are itegers.
They are mentioned with separators like this: n_n!n_n.

Example, in decimal and hexadecimal:
326598_7845126575216984!6_951378624 
x4FBC6_1BDF19DEBBD958!6_38B4E2C0


#### Name for a normal form
1. an integer describing the Figure
    The Figure, described above, is a large integer in it's binary form. This integer is simply the id of the figure.
    By default the id is shown in decimal form, or as hex with a leading 'x', to save space
2. a list of numbers describing the fill of figure
    The list of digits in the sudoku, skipping all blank fields. A SuDoKu with 17 clues will have 17 digits in this list.
    This integer is simply the id of the fill of the figure.
    By default the id is shown in decimal form, or as hex with a leading 'x', to save space.

#### Name of the Permutations
1. Describing the 8 permutation with integer 0..7.
    If the SuDoKu is a normal figure, it's p0
    The p value is always shown as decimal form
2. The substitution of digit values, needed to transform the normal form to this form.
    This is a list of 9 digits, stating what each of the normal form's 9 values should be substituted to, respectively.
    If the SuDoKu is normal, it's s0 for short, though the equivalent s123456789 is allowed.
    By default the s value is shown in decimal form, or as hex with a leading 'x', to save space
