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

    def bestMove(self):
        pass


class MinimaxTTT(Minimax):
    def movesLeft(self):
        for i in range(3):
            for j in range(3):
                if (self.game_state[i][j] == ' '):
                    return True
        return False

    # def evaluate(self):
    #     board = self.game_state
    #     #Check rows for a win
    #     for row in range(3):
    #         if (board[row][0] == board[row][1] == board[row][2] == self.player):
    #             return 10
    #         if (board[row][0] == board[row][1] == board[row][2] == self.opponent):
    #             return -10

    #     #Check columns for a win
    #     for col in range(3):
    #         if (board[0][col] == board[1][col] == board[2][col] == self.player):
    #             return 10
    #         if (board[0][col] == board[1][col] == board[2][col] == self.opponent):
    #             return -10

    #     #Check both diagonals for a win
    #     if (board[0][0] == board[1][1] == board[2][2] == self.player):
    #         return 10
    #     if (board[0][0] == board[1][1] == board[2][2] == self.opponent):
    #         return -10

    #     if (board[0][2] == board[1][1] == board[2][0] == self.player):
    #         return 10
    #     if (board[0][2] == board[1][1] == board[2][0] == self.opponent):
    #         return -10

    #     #No win
        # return 0

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

    def bestMove(self):
        bestUtility = -10000
        bestMove = (None, None)

        for row in range(3):
            for col in range(3):
                if self.game_state[row][col] == ' ':
                    self.game_state[row][col] = self.player
                    moveUtility = self.minimax(1, False)
                    self.game_state[row][col] = ' '

                    if moveUtility > bestUtility:
                        bestMove = (row, col)
                        bestUtility = moveUtility
        return bestMove


class MinimaxTakeAway(Minimax):

    def movesLeft(self):
        return self.game_state != 0

    def evaluate(self):
        # player won
        if self.game_state == 0:
            return 10
        #preferable to keep it divisible by 4 after your move
        if self.game_state % 4 == 0:
            return 5
        #if this is the state after your move you lose
        if int(self.game_state) in [1, 2, 3]:
            return -10
        #if its not disisible by 4 after your move they can make you pick the
        #count that is disisible by 4
        if self.game_state % 4 != 0:
            return -5

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
            for move in [1, 2, 3]:
                if self.game_state-move >= 0:
                    self.game_state -= move
                    bestUtility = max(
                        bestUtility, self.minimax(depth-1, not maxPlayer))
                    self.game_state += move
            return bestUtility
        else:
            bestUtility = 10000
            for move in [1, 2, 3]:
                if self.game_state-move >= 0:
                    self.game_state -= move
                    bestUtility = min(
                        bestUtility, self.minimax(depth-1, not maxPlayer))
                    self.game_state += move
            return bestUtility

    def bestMove(self):
        bestUtility = -10000
        bestMove = (None, None)

        for move in [1, 2, 3]:
            if self.game_state-move >= 0:
                self.game_state -= move
                moveUtility = self.minimax(10000, False)
                self.game_state += move
                # print(f'{moveUtility} : {move}')
                if moveUtility > bestUtility:
                    bestMove = move
                    bestUtility = moveUtility
        return (bestMove)

# for testing purposes
def main():
    # board = [
    #     [' ', 'X', ' '],
    #     [' ', ' ', ' '],
    #     [' ', 'O', ' ']
    # ]

    # print(MinimaxTTT(board, 'X', 'O').evaluate())

    state = 7
    print(MinimaxTakeAway(state, '1', '2').bestMove())



if __name__ == "__main__":
    main()
