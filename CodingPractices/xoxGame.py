class Game():
    def __init__(self):
        self.board = [[" "," "," "], [" "," "," "], [" "," "," "]]
        self.status = True
        self.move = 0

    def play(self):
        if self.move % 2 ==0:
            self.p1choice()
        else:
            self.p2choice()

        self.status = self.checkGame()

        if not self.status:
            self.showBoard()
            whoWins = ""
            if self.move % 2 ==0:
                whoWins = "X"
            else:
                whoWins = "O"
            print("Game Over! Winner is = {}".format(whoWins))

        self.move += 1

    def p1choice(self):
        self.showBoard()
        print("Player 1's turn")
        row = int(input("Enter the row number (1-3): "))
        while row < 1 or row > 3:
            print("Invalid input. Please enter a number between 1 and 3.")
            row = int(input("Enter the row number (1-3): "))

        col = int(input("Enter the column number (1-3): "))
        while col < 1 or col > 3:
            print("Invalid input. Please enter a number between 1 and 3.")
            col = int(input("Enter the column number (1-3): "))

        if self.isFull(row, col):
            self.p1choice()
        else:
            self.board[row-1][col-1] = "X"

    def p2choice(self):
        self.showBoard()
        print("Player 2's turn")
        row = int(input("Enter the row number (1-3): "))
        while row < 1 or row > 3:
            print("Invalid input. Please enter a number between 1 and 3.")
            row = int(input("Enter the row number (1-3): "))

        col = int(input("Enter the column number (1-3): "))
        while col < 1 or col > 3:
            print("Invalid input. Please enter a number between 1 and 3.")
            col = int(input("Enter the column number (1-3): "))

        if self.isFull(row, col):
            self.p2choice()
        else:
            self.board[row-1][col-1] = "O"

    def isFull(self, row, col):
        if self.board[row-1][col-1] != " ":
            return True
        else:
            return False

    def showBoard(self):

        for i in self.board:
            for j in i:
                print(j, end=" ")
            print("\n")

    def checkGame(self):
        if [self.board[0][0], self.board[0][1], self.board[0][2]] == ["X", "X", "X"]:
            print("Player 1 wins!")
            return False
        if [self.board[1][0], self.board[1][1], self.board[1][2]] == ["X", "X", "X"]:
            print("Player 1 wins!")
            return False
        if [self.board[2][0], self.board[2][1], self.board[2][2]] == ["X", "X", "X"]:
            print("Player 1 wins!")
            return False
        if [self.board[0][0], self.board[1][0], self.board[2][0]] == ["X", "X", "X"]:
            print("Player 1 wins!")
            return False
        if [self.board[0][1], self.board[1][1], self.board[2][1]] == ["X", "X", "X"]:
            print("Player 1 wins!")
            return False
        if [self.board[0][2], self.board[1][2], self.board[2][2]] == ["X", "X", "X"]:
            print("Player 1 wins!")
            return False
        if [self.board[0][0], self.board[1][1], self.board[2][2]] == ["X", "X", "X"]:
            print("Player 1 wins!")
            return False
        if [self.board[0][2], self.board[1][1], self.board[2][0]] == ["X", "X", "X"]:
            print("Player 1 wins!")
            return False
        if [self.board[0][0], self.board[0][1], self.board[0][2]] == ["O", "O", "O"]:
            print("Player 2 wins!")
            return False
        if [self.board[1][0], self.board[1][1], self.board[1][2]] == ["O", "O", "O"]:
            print("Player 2 wins!")
            return False
        if [self.board[2][0], self.board[2][1], self.board[2][2]] == ["O", "O", "O"]:
            print("Player 2 wins!")
            return False
        if [self.board[0][0], self.board[1][0], self.board[2][0]] == ["O", "O", "O"]:
            print("Player 2 wins!")
            return False
        if [self.board[0][1], self.board[1][1], self.board[2][1]] == ["O", "O", "O"]:
            print("Player 2 wins!")
            return False
        if [self.board[0][2], self.board[1][2], self.board[2][2]] == ["O", "O", "O"]:
            print("Player 2 wins!")
            return False
        if [self.board[0][0], self.board[1][1], self.board[2][2]] == ["O", "O", "O"]:
            print("Player 2 wins!")
            return False
        if [self.board[0][2], self.board[1][1], self.board[2][0]] == ["O", "O", "O"]:
            print("Player 2 wins!")
            return False
        
        return True
        

game = Game()
while game.status:
    game.play() 
