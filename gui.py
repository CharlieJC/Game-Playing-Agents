import tkinter as tk
from ai import MinimaxTTT, MinimaxTakeAway
from game import TicTacToe, TakeAway,Connect4


class TicTacToeGUI(TicTacToe):

    btns = [[None for i in range(3)] for j in range(3)]
    info = None

    def __init__(self, aiplayers, master, depth):
        super().__init__(aiplayers)
        self.master = master
        self.frame = tk.Frame(master)
        self.depth = depth

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

    btns = None
    info, game_state_info = None, None

    def __init__(self, aiplayers, master, depth):
        super().__init__(aiplayers)
        self.master = master
        self.frame = tk.Frame(master)
        self.depth = depth

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

class Connect4GUI(Connect4):

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

class MainMenuGUI():

  

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)

        # ai player checkboxes
        self.is_p1_ai = tk.BooleanVar()
        tk.Checkbutton(self.frame, text="Player 1 AI", variable=self.is_p1_ai).grid(row=1, sticky=tk.W)
        self.is_p2_ai = tk.BooleanVar()
        tk.Checkbutton(self.frame, text="Player 2 AI", variable=self.is_p2_ai).grid(row=2, sticky=tk.W)

        # depth entry
        depth_label = tk.Label(self.frame, text='Minimax Depth:').grid(row=3,column=0)
        self.depth_field = tk.Entry(self.frame)
        self.depth_field.grid(row=3, column=1, sticky=tk.W)
        self.depth_field.insert(0, '3')
        

        # play game buttons
        tk.Button(self.frame, text='Play a TicTactoe Game', command=self.playTTT).grid(row=4, sticky=tk.NSEW, pady=4)
        tk.Button(self.frame, text='Play a Take Away Game', command=self.playTakeAway).grid(row=5, sticky=tk.NSEW, pady=4)

        self.frame.pack()

    def playTTT(self):
        print(int(self.depth_field.get()))
        player1_ai = self.is_p1_ai.get()
        player2_ai = self.is_p2_ai.get()
        depth = int(self.depth_field.get())
        self.frame.destroy()
        game = TicTacToeGUI((player1_ai,player2_ai), self.master, depth)
        game.play()
    def playTakeAway(self):   
        player1_ai = self.is_p1_ai.get()
        player2_ai = self.is_p2_ai.get()
        depth = int(self.depth_field.get())
        self.frame.destroy()
        game = TakeAwayGUI((player1_ai,player2_ai), self.master, depth)
        game.play()
    
    
        
def main():
    root = tk.Tk()
    root.title("Game Playing Agents")
    MainMenuGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

