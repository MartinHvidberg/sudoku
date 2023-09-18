
# Bringing a sudoku on its normal form

A SoDuKo can exist in many forms, we call these forms permutations.

## Permutations

If you take a perfectly good SuDoKu, e.g. printed on paper, and turn the paper 
180 degr. it's still the same SuDoKu, even though the numbers - as you still 
read from top-left courner -  now appear in another order.
You have just created a permutation of the same SoDuKo.
The numbers appear to draw a different figure, so we call these 
permutations **figure-permutations**.
You can create figure-permutations by turning or flipping the SuDoKu. There 
are 8 different figure-permutations.

Similar, if you swap all the 4's and 5's. You still have the essential same 
SuDoKu. In fact, you could swap all the numbers for there letter equivalent, 
and you will still have the same SuDoKu.
By substituting the alphabet of the SoDuKo, while preserving the logic of the 
quiz, we render it into another language, style. Therefore, we call these 
permutations **alphabet-permutations**.
As the SoDuKo 'alphabet' has 9 letters, not including 0, there are 9! = 
362.880 different **alphabet-permutations**


### The 'normal' permutation
In the following we will describe a method for finding the one of the 
potential 8 * 362.880 = 2903040 (almost 3 mill) possible permutations, that 
should represent the SuDoKu. We call this permutation: The 'normal' 
permutation.

Note that the method requires that we first find the 'normal' figure-permutation, and 
then the 'normal' alpha-permutation. Not the other way.

### Finding the 'normal' figure-permutation
Using the 81 digit long string representing the sudoku
1. Replace all non-0 with 1, thus generating a string of only 0 and 1, that is 
   interpreted as a binary number N.
2. While looping through all possible 8 figure-permutations: 
The normal figure is the permutation where the binary number N becomes smallest.

It is unclear if some symmetrical SoDuKos can have figure-permutations that 
flip into itself, i.e. do not change when flipped.
In that case we will progress both (or more) permutations to the alphabetic 
normalisation. 
After alphabet normalise all of these. The one, with the then lowest 
value is considered the 'normal' permutation.

### Finding the 'normal' alphabet-permutation
Having transformed the SuDoKu, the original one - not the binary, to its 
normal figure-permutation.
1. Find the first non-0 digit, and replace all occurrences of this digit with an 'a'
    Find the second and replace all occurrences with 'b'
    repeat until all numbers are substituted with letters
2. Then replace all 'a'=1, 'b'=2, etc. 
    The digits now appear in order, with respect to first appearance.

We now have the 'normal' permutation

## Appendix. Naming convention

Naming a SuDoKu by describing it's normal form + the permutation from the normal form.

Name has 4 parts. 2 parts to describe the normal-permutation, and 2 to 
describe the specific permutation. All four parts are itegers.
They are mentioned with separators like this: `<n>_<n>!<n>_<n>` and it's 
suggested to use a leading NSN_ for Normalized SoDuKo Name.

Example, in decimal (Base10) and hexadecimal (Base16):

- NSN_326598_7845126575216984!6_951378624
- NSN_x4FBC6_1BDF19DEBBD958!6_38B4E2C0

The 'x' indicates that all 4 elements are given as hex numbers.

Optional Base64 encoding could provide even shorter names, and therefore the 
separators '_' and '! ' are selected, so they don't conflict with standard 
Base64 alphabet.

#### Name for a normal-permutation
1. An integer describing the figure-permutation's figure as an 81 long binary 
    number of only 0's and 1's, described above. This binary number is the 
    first part of the name
2. A list of numbers describing the fill of figure.

   The list of digits in the sudoku, skipping all blank fields. A SuDoKu with 
   17 clues will have 17 digits in this list.
   This integer is simply the fill of the figure.

#### Name of the specific-permutations
1. Describing the 8 permutation with integer 0..7.
    If the SuDoKu is a normal figure, it's 0

    _ToDo_: Describe the sequense of flips, turns and mirrorings that is required 
    to progress from permutation 0 to 1, from 1 to 2, etc. 
2. The substitution of digit values, needed to transform the normal permutation to 
    this permutation.
    This is a list of 9 digits, stating what each of the normal form's 9 
    values should be substituted to, respectively.
    If the SuDoKu is normal, it's valid to write 0 for short, though the equivalent 
    123456789 is allowed.

If a SuDoKu is in its normal form, that last two numbers would be !0_0 or if 
spelled out !0_123456789. In either case it's valid to just skip the lot, as 
the first two numbers describes the 'normal' permutation.

By default, all number value are shown in decimal form, or as hex with a 
leading 'x', to save (a few bytes of) space.
