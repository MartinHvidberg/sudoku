class Board:

    solvedBoard = [[0 for i in range(9)] for j in range(9)]
    gameRunning = True

    def __init__(self):
        self.tabuleiro = [[0 for i in range(9)] for j in range(9)]

    def reset(self):
        self.tabuleiro = [[0 for i in range(9)] for j in range(9)]
        self.gameRunning = True

    def show(self):
        for i in self.tabuleiro:
            for j in i:
                print(j, end = ' ')
            print('')

    def setCell(self, linha, coluna, valor):
        self.tabuleiro[linha][coluna] = valor

    def isFull(self):
        for i in range(9):
            for j in range(9):
                if self.tabuleiro[i][j] == 0:
                    return False
        return True

    def numberPossibilities(self, linha, coluna):
        possible = [1 for i in range(10)]

        #horizontal check
        for col in range(9):
            if self.tabuleiro[linha][col]:
                possible[self.tabuleiro[linha][col]] = 0

        #vertical check
        for line in range(9):
            if self.tabuleiro[line][coluna]:
                possible[self.tabuleiro[line][coluna]] = 0

        #mini square check
        linhaSquare = (linha // 3) * 3
        colunaSquare = (coluna // 3) * 3
        for l in range(linhaSquare, linhaSquare + 3):
            for c in range(colunaSquare, colunaSquare + 3):
                if self.tabuleiro[l][c]:
                    possible[self.tabuleiro[l][c]] = 0

        toTry = []
        for k in range(1, 10):
            if possible[k]:
                toTry.append(k)

        return toTry

    def solve(self):
        self.show()
        print('')
        if self.isFull():
            for i in range(9):
                for j in range(9):
                    self.solvedBoard[i][j] = self.tabuleiro[i][j]
            self.gameRunning = False
            self.tabuleiro = self.solvedBoard
        elif self.gameRunning:
            found = False
            linha = 0
            coluna = 0
            for i in range(9):
                for j in range(9):
                    if (not self.tabuleiro[i][j]):
                        linha = i
                        coluna = j
                        found = True
                        break
                if found:
                    break
            numbers = self.numberPossibilities(linha, coluna)
            print(*numbers)
            print('')
            tamanho = len(numbers)
            for k in range(tamanho):
                if (not self.gameRunning):
                    self.tabuleiro = self.solvedBoard
                    break
                self.tabuleiro[linha][coluna] = numbers[k]
                self.solve()
            if (self.gameRunning):
                self.tabuleiro[linha][coluna] = 0

if __name__ == "__main__":
