// This seems to be very fast, generating 10,000 very crappy sudokus in about 50ms.

include <stdio.h>

static char s[9][9] = {
  { '7', '1', '3', '5', '4', '8', '2', '6', '9' },
  { '2', '9', '4', '7', '6', '3', '1', '8', '5' },
  { '8', '5', '6', '1', '2', '9', '4', '7', '3' },
  { '5', '4', '2', '8', '7', '1', '9', '3', '6' },
  { '1', '3', '7', '2', '9', '6', '5', '4', '8' },
  { '6', '8', '9', '4', '3', '5', '7', '1', '2' },
  { '4', '6', '5', '3', '1', '2', '8', '9', '7' },
  { '3', '2', '1', '9', '8', '7', '6', '5', '4' },
  { '9', '7', '8', '6', '5', '4', '3', '2', '1' }
};

const int perm[8][9] = {
  { 0, 1, 2, 3, 4, 5, 6, 7, 8 },
  { 1, 0, 2, 3, 4, 5, 6, 7, 8 },
  { 0, 1, 2, 4, 3, 5, 6, 7, 8 },
  { 0, 1, 2, 3, 4, 5, 7, 6, 8 },
  { 0, 2, 1, 3, 4, 5, 6, 7, 8 },
  { 0, 1, 2, 3, 5, 4, 6, 8, 7 },
  { 2, 1, 0, 3, 4, 5, 6, 7, 8 },
  { 0, 1, 2, 5, 4, 3, 6, 7, 8 }
};

static void output_sudoku(int number) {
  int blank_row = number % 9;
  int blank_col = (number / 9) % 9;
  char saved = s[blank_row][blank_col];
  s[blank_row][blank_col] = '.';
  int row_perm = (number / 81) & 7;
  int col_perm = (number / 81 / 8) & 7;
  int transpose = (number / 81 / 8 / 8) & 1;

  for (int row = 0; row < 9; row++) {
    for (int col = 0; col < 9; col++) {
      int rr = perm[row_perm][row];
      int cc = perm[col_perm][col];
      if (transpose) { int temp = rr; rr = cc; cc = temp; }
      putchar(s[rr][cc]);
    }
    putchar('\n');
  }
  putchar('\n');

  s[blank_row][blank_col] = saved;
}

int main() {
  for (int i = 0; i < 10000; ++i) {
    output_sudoku(i);
  }
}