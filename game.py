from ai import MinimaxTTT, MinimaxTakeAway, MinimaxConnect4, MinimaxConnect4AB

class Game():
    #2-tuple to store each players name
    #defaut player 1 and player 23
    players = (1,2)
    moves = []
    current_player = 0
    game_state = None
    move_error_text = 'That is not a valid move, try again.'

    #Checks if winner returns 'DRAW' only if draws are possible
    draws_possible = False

    def __init__(self, aiplayers):
        self.aiplayers = aiplayers

    def play(self):
        endgame = False
        while endgame == False:
            self.printGame()
            print("Player " + str(self.players[self.current_player]) + "'s turn!")
            if self.aiplayers[self.current_player]:
                self.process_ai_move()
            else:
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

    def process_ai_move(self, depth = 100000):
        pass

    def nextTurn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def printGame(self):
        pass

    def winner(self):
        pass

    def move(self, keyPress):
        pass

    def opponent(self, player):
        if self.players[0] == player:
            return self.players[1]
        if self.players[1] == player:
            return self.players[0]

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
    game_state = [[' ' for x in range(3)] for y in range(3)]
    draws_possible = True

    keybind = [
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3],
    ]

    def process_ai_move(self, depth=3):
        bestMove = MinimaxTTT(self.game_state,self.players[self.current_player],self.opponent(self.players[self.current_player])).bestMove(depth)
        self.game_state[bestMove[0]][bestMove[1]] = self.players[self.current_player]
        return 

    def winner(self):
        player = self.players[self.current_player]
        board = self.game_state
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
                    if (self.game_state[i][j] == ' '):
                        self.game_state[i][j] = self.players[self.current_player]
                        return True
                    else:
                        print(self.move_error_text)
                        return False     

    def printGame(self):
        for i in range(3):
            print('|', end='')
            for j in range(3):
                print(self.game_state[i][j], end='|')
            print()

class TakeAway(Game):
    
    game_state = 21
    moves = [1,2,3]
    players = (1,2)

    def process_ai_move(self, depth=3):
        bestMove = MinimaxTakeAway(self.game_state,self.players[self.current_player],self.opponent(self.players[self.current_player])).bestMove(depth)
        self.game_state -= bestMove
        return 

    def winner(self):
        if self.game_state == 0:
            return self.players[self.current_player]
        else:
            return None

    def move(self, amount):
        if int(amount) not in [1,2,3]:
            print(self.move_error_text)
            return False
        if (self.game_state-amount) < 0:
            print(self.move_error_text)
            return False

        self.game_state -= amount
        return True

    def printGame(self):
        print(str(self.game_state) + " remaining")

class Connect4(Game):

    players = ('R','G')
    moves = [1,2,3,4,5,6,7]
    game_state = [[' ' for x in range(7)] for y in range(6)]

    def process_ai_move(self, depth=3):
        bestMove = MinimaxConnect4AB(self.game_state,self.players[self.current_player],self.opponent(self.players[self.current_player])).bestMove(depth)
        self.move(bestMove)
        return 

    #using the non beta pruned version for testing purposes
    def process_ai_move_inefficient(self, depth=3):
        bestMove = MinimaxConnect4(self.game_state,self.players[self.current_player],self.opponent(self.players[self.current_player])).bestMove(depth)
        self.move(bestMove)
        return 

    def winner(self):
        #width from left
        xLength = len(self.game_state[0])
        #depth from top
        yLength = len(self.game_state)
        board = self.game_state
        
        #check horizontal wins
        for x in range(xLength):
            for y in range(yLength-3):
                if board[y][x] == board[y+1][x] == board[y+2][x] == board[y+3][x] != ' ':
                    return board[y][x]
        #check vertical wins
        for x in range(xLength-3):
            for y in range(yLength):
                if board[y][x] == board[y][x+1] == board[y][x+2] == board[y][x+3] != ' ':
                    return board[y][x]

        #check / diagonal
        for x in range(3, xLength):
            for y in range(yLength-3):
                if board[y][x] == board[y+1][x-1] == board[y+2][x-2] == board[y+3][x-3] != ' ':
                    return board[y][x]
        #check \ diagonal
        for x in range(xLength-3):
            for y in range(yLength-3):
                if board[y][x] == board[y+1][x+1] == board[y+2][x+2] == board[y+3][x+3] != ' ':
                    return board[y][x]

    def move(self, slot):
        if int(slot) not in self.moves:
            print(self.move_error_text)
            return False
        if self.dropCoin(slot-1) == False:
            print(self.move_error_text)
            return False
        else:
            return True

    def dropCoin(self,pos):
        for y in range(5,-1,-1):
            if self.game_state[y][pos] == ' ':
                self.game_state[y][pos] = self.players[self.current_player]
                return True
        #if full
        return False

    def removeCoin(self,pos):
        if pos in range(1,7):
            for y in range(0,6):
                if self.game_state[y][pos] != ' ':
                    self.game_state[y][pos] = ' '
                    return True
        #if full
        return False

    def printGame(self):
        for x in range(6):
            print('|', end='')
            for y in range(7):
                print(self.game_state[x][y], end='|')
            print()

        print('|1|2|3|4|5|6|7|')


def main():
    player1_ai = False
    player2_ai = False
    print("Should player one be AI? (Y/N)")
    temp = input()
    if temp == 'Y' or temp == 'y':
        player1_ai = True
    print("Should player two be AI? (Y/N)")
    temp = input()
    if temp == 'Y' or temp == 'y':
        player2_ai = True
    print("Please choose a game to play! (1,2,3)")
    print('1 - TicTacToe')
    print('2 - Take Away Game')
    print('3 - Connect 4')

    index = input()
    if int(index) == 1:
        game = TicTacToe((player1_ai,player2_ai))
        game.play()
    elif int(index) == 2:
        game = TakeAway((player1_ai,player2_ai))
        game.play()
    else:
        game = Connect4((player1_ai,player2_ai))
        game.play()
    
if __name__ == "__main__":
    main()