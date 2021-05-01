class Game():
    #2-tuple to store each players name
    #defaut player 1 and player 23
    players = (1,2)
    moves = []
    current_player = 0
    gameState = None
    move_error_text = 'That is not a valid move, try again.'

    #Checks if winner returns 'DRAW' only if draws are possible
    draws_possible = False

    def play(self):
        endgame = False
        while endgame == False:
            self.printGame()
            print("Player " + str(self.players[self.current_player]) + "'s turn!")
            validMove = False
            while validMove == False:
                validMove = self.move(self.inputMove())
            if self.winner() == None:
                self.nextTurn()
            elif self.draws_possible and self.winner() == 'DRAW':
                print("IT IS A DRAW!")
                endgame = True
            else:
                print('PLAYER ' + str(self.players[self.current_player]) + ' WINS!')
                endgame = True
        self.printGame()

    def nextTurn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def printGame(self):
        pass

    def winner(self):
        pass

    def move(self, keyPress):
        pass

    def undoMove(self, keyPress):
        pass

    def inputMove(self):
        inputKey = None
        while inputKey not in self.moves:
            print("Enter a number key from the move list: " + str(self.moves))
            try:
                inputKey = int(input())
            except ValueError:
                print(self.move_error_text)

        return inputKey

class TicTacToe(Game):
    players = ('X','O')
    moves = [1,2,3,4,5,6,7,8,9]
    gameState = [[' ' for x in range(3)] for y in range(3)]
    draws_possible = True

    keybind = [
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3],
    ]

    def winner(self):
        player = self.players[self.current_player]
        board = self.gameState
        # check rows
        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2] == player):
                return player
        # check columns
        for i in range(3):
            if (board[0][i] == board[1][i] == board[2][i] == player):
                return player
        # check diagonals
        if (board[0][0] == board[1][1] == board[2][2] == player):
            return player
        if (board[0][2] == board[1][1] == board[2][0] == player):
            return player

        # if there are free spaces
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    return None

        # otherwise its a draw
        return 'DRAW'

    def move(self, keyPress):
        for i in range(3):
            for j in range(3):
                if self.keybind[i][j] == keyPress:
                    if (self.gameState[i][j] == ' '):
                        self.gameState[i][j] = self.players[self.current_player]
                        return True
                    else:
                        print(self.move_error_text)
                        return False
        

    def printGame(self):
        for i in range(3):
            print('|', end='')
            for j in range(3):
                print(self.gameState[i][j], end='|')
            print()

class TakeAway(Game):
    
    gameState = 21
    moves = [1,2,3]
    players = [1,2,3]

    def winner(self):
        if self.gameState == 0:
            return self.players[self.current_player]
        else:
            return None

    def move(self, amount):
        if int(amount) not in [1,2,3]:
            print(self.move_error_text)
            return False
        if (self.gameState-amount) < 0:
            print(self.move_error_text)
            return False

        self.gameState -= amount
        return True


    def printGame(self):
        print(str(self.gameState) + " remaining")


def main():
    game = TakeAway()
    game.play()


if __name__ == "__main__":
    main()
