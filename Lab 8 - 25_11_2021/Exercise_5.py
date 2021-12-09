# tic-tac-toe (1v1)

# GUI framework library
import tkinter as tk
from tkinter import Button, PhotoImage, ttk, font, messagebox
from tkinter.constants import DISABLED
from functools import partial

gui = tk.Tk()

# Global settings
gui_size = 500 # In px
button_height = (gui_size/3) - 6
button_width = (gui_size/3) - 6
font_size = font.Font(size = 100)
button_img = PhotoImage(width = 1, height = 1)

# Used simbols, start the first
simbols = ["x", "o", True]
# Table to store inserted values (3x3 table)
table = [["" for i in range(3)] for j in range(3)]

def win_conditions():
    # Check win conditions (same row, column or diagonal)
    if (
        table[0] == [simbols[0] for i in range(3)] or table[1] == [simbols[0] for i in range(3)] or table[2] == [simbols[0] for i in range(3)] or
        [(table[i][0]) for i in range(3)]  == [simbols[0] for i in range(3)] or [(table[i][1]) for i in range(3)]  == [simbols[0] for i in range(3)] or [(table[i][2]) for i in range(3)]  == [simbols[0] for i in range(3)] or
        [(table[i][i]) for i in range(3)]  == [simbols[0] for i in range(3)] or [(table[i-1][-i]) for i in range(3, 0, -1)]  == [simbols[0] for i in range(3)]
    ):
        return simbols[0]
    elif (
        table[0] == [simbols[1] for i in range(3)] or table[1] == [simbols[1] for i in range(3)] or table[2] == [simbols[1] for i in range(3)] or
        [(table[i][0]) for i in range(3)]  == [simbols[1] for i in range(3)] or [(table[i][1]) for i in range(3)]  == [simbols[1] for i in range(3)] or [(table[i][2]) for i in range(3)]  == [simbols[1] for i in range(3)] or
        [(table[i][i]) for i in range(3)]  == [simbols[1] for i in range(3)] or [(table[i-1][-i]) for i in range(3, 0, -1)]  == [simbols[1] for i in range(3)]
    ):
        return simbols[1]
    else:
        return 0

# Function to execute every button_press event
def button_press(button_index):

    # Switch between the two simbols
    simbols[2] = not simbols[2]

    # Write the value to the button and disable it
    globals()[f"button_{button_index}"].config(text = simbols[simbols[2]], font = font_size)
    globals()[f"button_{button_index}"]["state"] = "disabled"

    # Update the table and call the function to controll if a user has win
    table[button_index[0]][button_index[1]] = simbols[simbols[2]]
    if win_conditions() == simbols[0]:
        messagebox.showinfo(title = "You have won!", message = f"Player with \"{simbols[0]}\" has won!")
        gui.destroy()
    elif win_conditions() == simbols[1]:
        messagebox.showinfo(title = "You have won!", message = f"Player with \"{simbols[1]}\" has won!")
        gui.destroy()
    else: 
        return 0

# GUI Settings
gui.geometry(str(gui_size)+"x"+str(gui_size))
gui.resizable(False, False)
gui.columnconfigure(3, weight = 1)
gui.rowconfigure(3, weight = 1)
gui.title("Tic-Tac-Toe")

# Button 1-9 (indexes) creation
for i in range(3):  
    for j in range(3):  
        globals()[f"button_{(i,j)}"] = Button(
            gui,
            image = button_img,
            compound="c",
            command = partial(button_press, (i,j)),
            height = button_height,
            width = button_width
            )
        globals()[f"button_{(i,j)}"].grid(row = i, column = j)

# Used to update the gui windows
gui.mainloop()