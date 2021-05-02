from tkinter import Tk, Label, Button

root = Tk()


board = [
        [' ', 'X', 'X'],
        ['X', 'O', ' '],
        [' ', 'O', ' ']
    ]

grid_buttons = [[None for i in range(3)] for j in range(3)]

# for row in range(3):
#     for col in range(3):
#         label = Label(root, text=("     " + board[row][col] + "     "))
#         label.grid(row=row,column=col)

def click(row,col):
    board[row][col] == 'X'
    grid_buttons[row][col].text = "TEST"

def create_buttons():
    for row in range(3):
        for col in range(3):
            button = Button(root, text=("     " + board[row][col] + "     "), command = lambda: click(row,col))
            grid_buttons[row][col] = button
            button.grid(row=row,column=col)

create_buttons()
root.mainloop()
def main():
    pass
    

if __name__ == "__main__":
    main()
