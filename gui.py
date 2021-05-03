import tkinter as tk
from ai import MinimaxTTT, MinimaxTakeAway
from game import TicTacToe, TakeAway


class TicTacToeGUI(TicTacToe):

    btns = [[None for i in range(3)] for j in range(3)]
    info = None

    def __init__(self, aiplayers, master):
        super().__init__(aiplayers)
        self.master = master
        self.frame = tk.Frame(master)

    def onClick(self, btn):
        if self.winner() != None:
            return
        row, col = None, None
        for i in range(3):
            for j in range(3):
                if self.btns[i][j] == btn:
                    row = i
                    col = j
                
        #if button coordinates are not found return        
        if row == None or col == None:
            return

        if self.game_state[row][col] == ' ':
            self.game_state[row][col] = self.players[self.current_player]
        else:
            #if move is invalid return
            return

        #After human player has moved check win conditions
        if self.winner() == 'DRAW':
            self.update()
            self.info['text'] = "IT WAS A DRAW"
            return
        if self.winner() == self.players[self.current_player]:
            self.update()
            self.info['text'] = self.winner() + " WON!"
            return

        self.nextTurn()
        if self.aiplayers[self.current_player]:
            self.process_ai_move()
            #After AI has moved check win conditions
            if self.winner() == 'DRAW':
                self.update()
                self.info['text'] = "IT WAS A DRAW"
                return
            if self.winner() == self.players[self.current_player]:
                self.update()
                self.info['text'] = self.winner() + " WON!"
                return
            self.nextTurn()
        self.update()

    def play(self):
        self.create_game_window()
        self.frame.pack()

        #if we have two AI players who cant click buttons
        #loop infinitely until they are done
        if self.aiplayers[0] == self.aiplayers[1] == True:
            while True:
                self.process_ai_move()
                #After AI has moved check win conditions
                if self.winner() == 'DRAW':
                    self.update()
                    self.info['text'] = "IT WAS A DRAW"
                    return
                if self.winner() == self.players[self.current_player]:
                    self.update()
                    self.info['text'] = self.winner() + " WON!"
                    return
                self.nextTurn()
        #if the first player is AI
        if self.aiplayers[self.current_player]:
            self.process_ai_move()
            #After AI has moved check win conditions
            if self.winner() == 'DRAW':
                self.update()
                self.info['text'] = "IT WAS A DRAW"
                return
            if self.winner() == self.players[self.current_player]:
                self.update()
                self.info['text'] = self.winner() + " WON!"
                return
            self.nextTurn()
        self.update()

    def create_game_window(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.frame, text=("     " + self.game_state[row][col] + "     "))
                btn['command'] = lambda btn=btn: self.onClick(btn)
                btn.grid(row=row,column=col,sticky=tk.NSEW)
                self.btns[row][col] = btn
        
        info = tk.Label(self.frame,text = f'PLAYER {self.players[self.current_player]}\'s TURN')
        info.grid(row=4,column=0, columnspan=3)
        self.info = info

        for i in range(4):
            tk.Grid.columnconfigure(self.frame, i, weight=1)

        for j in range(3):
            tk.Grid.rowconfigure(self.frame, j, weight=1)

    def update(self):
        self.printGame()
        turn = self.players[self.current_player]
        self.info['text'] = f'Player {turn}s turn!'
        for row in range(3):
            for col in range(3):
                btn = self.btns[row][col]
                btn['text'] = "     " + self.game_state[row][col] + "     "



class TakeAwayGUI(TakeAway):

    btn1, btn2, btn3 = None, None, None
    info, game_state_info = None, None

    def __init__(self, aiplayers, master):
        super().__init__(aiplayers)
        self.master = master
        self.frame = tk.Frame(master)

    def onClick(self, btn):
        if self.winner() != None:
            return
        if btn == self.btn1:
            if self.move(1) == False:
                return
        elif btn == self.btn2:
            if self.move(2) == False:
                return
        elif btn == self.btn3:
            if self.move(3) == False:
                return
                
        

        #After human player has moved check win conditions
        if self.winner() == self.players[self.current_player]:
            self.update()
            self.info['text'] = "PLAYER " + str(self.winner()) + " WON!"
            return

        self.nextTurn()
        if self.aiplayers[self.current_player]:
            self.process_ai_move()
            #After AI has moved check win conditions
            if self.winner() == self.players[self.current_player]:
                self.update()
                self.info['text'] = "PLAYER " + str(self.winner()) + " WON!"
                return
            self.nextTurn()
        self.update()

    def play(self):
        self.create_game_window()
        self.frame.pack()

        #if we have two AI players who cant click buttons
        #loop infinitely until they are done
        if self.aiplayers[0] == self.aiplayers[1] == True:
            while True:
                self.process_ai_move()
                #After AI has moved check win conditions
                if self.winner() == 'DRAW':
                    self.update()
                    self.info['text'] = "IT WAS A DRAW"
                    return
                if self.winner() == self.players[self.current_player]:
                    self.update()
                    self.info['text'] = 'PLAYER ' + str(self.winner()) + " WON!"
                    return
                self.nextTurn()
        #if the first player is AI
        if self.aiplayers[self.current_player]:
            self.process_ai_move()
            #After AI has moved check win conditions
            if self.winner() == 'DRAW':
                self.update()
                self.info['text'] = "IT WAS A DRAW"
                return
            if self.winner() == self.players[self.current_player]:
                self.update()
                self.info['text'] = self.winner() + " WON!"
                return
            self.nextTurn()
        self.update()
            
    def create_game_window(self):
        
        info = tk.Label(self.frame,text = f'PLAYER {self.players[self.current_player]}s TURN')
        info.grid(row=0,column=0, columnspan=3)
        self.info = info

        game_state_info = tk.Label(self.frame,text = ('o'*self.game_state))
        game_state_info.grid(row=1,column=0, columnspan=3)
        self.game_state_info = game_state_info

        btn1 = tk.Button(self.frame, text=("take 1"))
        btn1['command'] = lambda btn1=btn1: self.onClick(btn1)
        self.btn1 = btn1
        btn2 = tk.Button(self.frame, text=("take 2"))
        btn2['command'] = lambda btn2=btn2: self.onClick(btn2)
        self.btn2 = btn2
        btn3 = tk.Button(self.frame, text=("take 3"))
        btn3['command'] = lambda btn3=btn3: self.onClick(btn3)
        self.btn3 = btn3

        btn1.grid(row=2,column=0,sticky=tk.NSEW)
        btn2.grid(row=2,column=1,sticky=tk.NSEW)
        btn3.grid(row=2,column=2,sticky=tk.NSEW)

    def update(self):
        self.printGame()
        turn = self.players[self.current_player]
        self.info['text'] = f'PLAYER {self.players[self.current_player]}s TURN'
        self.game_state_info['text'] = 'o'*self.game_state

        
def main():
    root = tk.Tk()
    # game = TicTacToeGUI((True,False), root)
    game = TakeAwayGUI((True,False), root)
    game.play()
    root.mainloop()

    
    

# def main():

# TicTacToe((False,True),False).play()


if __name__ == "__main__":
    main()

