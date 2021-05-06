class Minimax():

    def __init__(self, game_state, player, opponent):
        self.player = player
        self.opponent = opponent
        self.game_state = game_state

    def movesLeft(self):
        pass

    def evaluate(self):
        pass

    def minimax(self, depth, max):
        pass

    def bestMove(self, depth):
        pass


class MinimaxTTT(Minimax):
    def movesLeft(self):
        for i in range(3):
            for j in range(3):
                if (self.game_state[i][j] == ' '):
                    return True
        return False


    # Eval(s) = 3X2(s) + X1(s) - (3O2(s) + O1(s))

    def evaluate(self):
        board = self.game_state
        # Check rows for a win
        players_points = 0
        opponent_points = 0
        for row in range(3):
            if (board[row][0] == board[row][1] == board[row][2] == self.player):
                return 10
            if (board[row][0] == board[row][1] == board[row][2] == self.opponent):
                return -10
            players_points += self.evaluate_line(
                self.player, board[row][0], board[row][1], board[row][2])
            opponent_points += self.evaluate_line(
                self.opponent, board[row][0], board[row][1], board[row][2])
        # Check columns for a win
        for col in range(3):
            if (board[0][col] == board[1][col] == board[2][col] == self.player):
                return 10
            if (board[0][col] == board[1][col] == board[2][col] == self.opponent):
                return -10
            players_points += self.evaluate_line(
                self.player, board[0][col], board[1][col], board[2][col])
            opponent_points += self.evaluate_line(
                self.opponent, board[0][col], board[1][col], board[2][col])
        # Check both diagonals for a win
        if (board[0][0] == board[1][1] == board[2][2] == self.player):
            return 10
        if (board[0][0] == board[1][1] == board[2][2] == self.opponent):
            return -10
        players_points += self.evaluate_line(self.player,
                                             [0][0], board[1][1], board[2][2])
        opponent_points += self.evaluate_line(
            self.opponent, [0][0], board[1][1], board[2][2])

        if (board[0][2] == board[1][1] == board[2][0] == self.player):
            return 10
        if (board[0][2] == board[1][1] == board[2][0] == self.opponent):
            return -10
        players_points += self.evaluate_line(self.player,
                                             board[0][2], board[1][1], board[2][0])
        opponent_points += self.evaluate_line(
            self.opponent, board[0][2], board[1][1], board[2][0])

        # No win
        return players_points-opponent_points

    def evaluate_line(self, player, p1, p2, p3):
        total = 0
        if (p1 == player):
            total += 1
        if (p2 == player):
            total += 1
        if (p3 == player):
            total += 1
            # 3*X2
        if total == 2:
            return 3
            # X1
        if total == 1:
            return 1
        return 0

    def minimax(self, depth, maxPlayer):
        utility = self.evaluate()

        # return when depth limit is reached
        if depth == 0:
            return utility

        # return when won
        if utility == 10:
            return utility

        # return when opponents won
        if utility == -10:
            return utility

        # return when no moved left
        if self.movesLeft() == False:
            return utility

        if maxPlayer:
            bestUtility = -10000
            for row in range(3):
                for col in range(3):
                    if self.game_state[row][col] == ' ':
                        self.game_state[row][col] = self.player
                        bestUtility = max(
                            bestUtility, self.minimax(depth-1, not maxPlayer))
                        self.game_state[row][col] = ' '
            return bestUtility
        else:
            bestUtility = 10000
            for row in range(3):
                for col in range(3):
                    if self.game_state[row][col] == ' ':
                        self.game_state[row][col] = self.opponent
                        bestUtility = min(
                            bestUtility, self.minimax(depth-1, not maxPlayer))
                        self.game_state[row][col] = ' '
            return bestUtility

    def bestMove(self, depth):
        bestUtility = -10000
        bestMove = (None, None)

        for row in range(3):
            for col in range(3):
                if self.game_state[row][col] == ' ':
                    self.game_state[row][col] = self.player
                    moveUtility = self.minimax(depth, False)
                    self.game_state[row][col] = ' '

                    if moveUtility > bestUtility:
                        bestMove = (row, col)
                        bestUtility = moveUtility
        if bestMove[0] == None:
            print("GOT HERE")
        return bestMove

class MinimaxTakeAway(Minimax):
    #must be kept in order
    possible_moves = [1,2,3]

    def movesLeft(self):
        return self.game_state != 0

    def evaluate(self):
        score = 0
        # player won
        if self.game_state == 0:
            return 100
        #if you end on a 1 higher than the highest move
        #you have essentially won
        if self.game_state == (max(self.possible_moves) + 1):
            return 100
        #if this is the state after your move you lose
        if int(self.game_state) in self.possible_moves:
            return -100
        #if its not disisible by 4 after your move they can make you pick the
        #count that is disisible by 4
        # if self.game_state % 4 != 0:
        #     score -= 5
        return score

    def minimax(self, depth, maxPlayer):
        utility = self.evaluate()

        # return when depth limit is reached
        if depth == 0:
            return utility

        #win or lose
        if utility == 100 or utility == -100:
            return utility

        # return when no moved left
        if self.movesLeft() == False:
            return utility

        if maxPlayer:
            bestUtility = -10000
            for move in self.possible_moves:
                if self.game_state-move >= 0:
                    self.game_state -= move
                    bestUtility = max(
                        bestUtility, self.minimax(depth-1, not maxPlayer))
                    self.game_state += move
            return bestUtility
        else:
            bestUtility = 10000
            for move in self.possible_moves:
                if self.game_state-move >= 0:
                    self.game_state -= move
                    bestUtility = min(
                        bestUtility, self.minimax(depth-1, not maxPlayer))
                    self.game_state += move
            return bestUtility

    def bestMove(self, depth):
        bestUtility = -10000
        bestMove = (None, None)

        for move in self.possible_moves:
            if self.game_state-move >= 0:
                self.game_state -= move
                moveUtility = self.minimax(depth, False)
                self.game_state += move
                # print(f'{moveUtility} : {move}')
                if moveUtility > bestUtility:
                    bestMove = move
                    bestUtility = moveUtility
        return (bestMove)

class MinimaxConnect4(Minimax):

    moves = [1,2,3,4,5,6,7]

    def movesLeft(self):
        for x in range(7):
            for y in range(6):
                if (self.game_state[y][x] == ' '):
                    return True
        return False

    def evaluate(self):
        score = 0
        #width from left
        xLength = len(self.game_state[0])
        #depth from top
        yLength = len(self.game_state)
        board = self.game_state
        
        #check horizontal wins
        for x in range(xLength):
            for y in range(yLength-3):
                score += self.evaluate_line(self.player, board[y][x], board[y+1][x], board[y+2][x], board[y+3][x])
                score -= self.evaluate_line(self.opponent, board[y][x], board[y+1][x], board[y+2][x], board[y+3][x])
        #check vertical wins
        for x in range(xLength-3):
            for y in range(yLength):
                score += self.evaluate_line(self.player, board[y][x], board[y][x+1], board[y][x+2], board[y][x+3])
                score -= self.evaluate_line(self.opponent, board[y][x], board[y][x+1], board[y][x+2], board[y][x+3])

        #check / diagonal
        for x in range(3, xLength):
            for y in range(yLength-3):
                score += self.evaluate_line(self.player, board[y][x], board[y+1][x-1], board[y+2][x-2], board[y+3][x-3])
                score -= self.evaluate_line(self.opponent, board[y][x], board[y+1][x-1], board[y+2][x-2], board[y+3][x-3])
        #check \ diagonal
        for x in range(xLength-3):
            for y in range(yLength-3):
                score += self.evaluate_line(self.player, board[y][x], board[y+1][x+1], board[y+2][x+2], board[y+3][x+3])
                score -= self.evaluate_line(self.opponent, board[y][x], board[y+1][x+1], board[y+2][x+2], board[y+3][x+3])

        # No win
        return score

    def evaluate_line(self, player, p1, p2, p3, p4):
        score = 0
        total = 0
        empty = 0
        
        #count how many of this players coins and empties are in this line
        if p1 == player:
            total += 1
        if p1 == ' ':
            empty += 1
        if p2 == player:
            total += 1
        if p2 == ' ':
            empty += 1
        if p3 == player:
            total += 1
        if p3 == ' ':
            empty += 1
        if p4 == player:
            total += 1
        if p4 == ' ':
            empty += 1
        
        # player has won
        if total == 4:
            score += 100
        
        # player has 1 move to win
        if total == 3 and empty == 1:
            score += 5

        # player has 2 moves to win
        if total == 2 and empty == 2:
            score += 2
        return score

    def minimax(self, depth, maxPlayer):
        utility = self.evaluate()

        # return when depth limit is reached
        if depth == 0:
            return utility

        # return when no moved left
        if self.movesLeft() == False:
            return utility

        if maxPlayer:
            bestUtility = -10000
            for move in self.moves:
                if self.dropCoin(move-1, self.player):
                    bestUtility = max(
                        bestUtility, self.minimax(depth-1, not maxPlayer))
                    self.removeCoin(move-1)
            return bestUtility
        else:
            bestUtility = 10000
            for move in self.moves:
                if self.dropCoin(move-1, self.opponent):
                    bestUtility = min(
                        bestUtility, self.minimax(depth-1, not maxPlayer))
                    self.removeCoin(move-1)
            return bestUtility


    def bestMove(self, depth):
        bestUtility = -10000
        bestMove = None

        for move in self.moves:
            if self.dropCoin(move-1, self.player):
                moveUtility = self.minimax(depth, False)
                self.removeCoin(move-1)

                if moveUtility > bestUtility:
                    bestMove = move
                    bestUtility = moveUtility

        return bestMove

    def dropCoin(self,pos, player):
        for y in range(5,-1,-1):
            if self.game_state[y][pos] == ' ':
                self.game_state[y][pos] = player
                return True
        #if full
        return False

    def removeCoin(self,pos):
        for y in range(0,6):
            if self.game_state[y][pos] != ' ':
                self.game_state[y][pos] = ' '
                return True
        #if full
        return False

class MinimaxConnect4AB(MinimaxConnect4):
    def alphabeta(self, depth, maxPlayer, a, b):
        utility = self.evaluate()

        # return when depth limit is reached
        if depth == 0:
            return utility

        # return when won
        if utility == 10:
            return utility

        # return when opponents won
        if utility == -10:
            return utility

        # return when no moved left
        if self.movesLeft() == False:
            return utility

        if maxPlayer:
            bestUtility = -10000
            for move in self.moves:
                if self.dropCoin(move-1, self.player):
                    bestUtility = max(
                        bestUtility, self.alphabeta(depth-1, not maxPlayer, a, b))
                    a = max(a,bestUtility)
                    self.removeCoin(move-1)
                    if a >= b:
                        break
            return bestUtility
        else:
            bestUtility = 10000
            for move in self.moves:
                if self.dropCoin(move-1, self.opponent):
                    bestUtility = min(
                        bestUtility, self.alphabeta(depth-1, not maxPlayer, a, b))
                    b = min(b, bestUtility)
                    self.removeCoin(move-1)
                    if b <= a:
                        break
            return bestUtility

    def bestMove(self, depth):
        bestUtility = -10000
        bestMove = None

        for move in self.moves:
            if self.dropCoin(move-1, self.player):
                moveUtility = self.alphabeta(depth, False, -10000, 10000)
                self.removeCoin(move-1)

                if moveUtility > bestUtility:
                    bestMove = move
                    bestUtility = moveUtility

        return bestMove

