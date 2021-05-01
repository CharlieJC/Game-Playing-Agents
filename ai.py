from game import Game

import math
import sys


class AIPlayerGame(Game):

    ai_players = []

    winScore = 10

    def minimax(self, depth, max):

        utility = self.evaluation()
        if utility == self.winScore or utility == -self.winScore:
            return utility

        if max:
            best = -sys.maxsize
            for move in self.remainingMoves():
                player = self.players[self.current_player]
                tempMove(move, player)
                best = max(best, minimax(depth+1, not max))
                tempRemove(move)
            return best
        else:
            best = sys.maxsize
            for move in self.remainingMoves():
                opponent = self.players((self.current_player + 1) % len(self.players))
                tempMove(move, opponent)
                best = min(best, minimax(depth+1, not max))
                tempRemove(move)
            return best

    def evaluation(self):
        pass

    def remainingMoves(self):
        pass

    # function for temporarily changing the game state
    # for a specific player
    def tempMove(self, move, player):
        pass

    def removeMove(self, move):
        pass
