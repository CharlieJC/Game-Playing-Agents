



class Game():
    winner = False
    turn = 1

    def play(self):
        pass

    def print(self):
        pass



class TicTacToe(Game):
    board = [
            ['','',''],
            ['','',''],
            ['','',''],
        ]

    keybind = [
            [7,8,9],
            [4,5,6],
            [1,2,3],
        ]

    def print(self):
        pass

class TakeAway(Game):
    total = 21