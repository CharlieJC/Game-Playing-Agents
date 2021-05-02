import tkinter as tk

class TicTacToeGUI():

    board = [
        [' ', 'X', 'X'],
        ['X', 'O', ' '],
        [' ', 'O', ' ']
    ]

    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.draw()
        self.frame.pack()
    def draw(self):
        self.create_game_buttons()

    def create_game_buttons(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.frame, text=("     " + self.board[row][col] + "     "))
                btn['command'] = lambda btn=btn: self.click(btn,row,col)
                btn.grid(row=row,column=col)

    def click(self,btn, row,col):
        btn['text'] = "     " + 'X' + "     "


# class TakeAwayGUI():
#     def __init__(self,master):
#         self.master = master
#         self.frame - tk.Frame(self.master)
#         self.frame.pack()
#     def draw():

# class HomeScreenGUI():
#     def __init__()

def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()
