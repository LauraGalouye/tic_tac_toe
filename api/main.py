import tkinter as tk
from tkinter import Toplevel
from tkinter import ttk
from tkinter import Canvas


# Function that resets the game
def reset():
    global current_player, win
    current_player = "X"
    win = False
    for column in buttons:
        for button in column:
            button.config(text="")  
    #canvas.delete("all")

def check_nul():
    print("Match nul")
    show_custom_messagebox("Match nul", "La partie est un match nul !")

# Function that prints the winner
def print_winner():
    global win
    if win is False:
        win = True
        print("Le joueur", current_player, "a gagné")
        show_custom_messagebox("Victoire", f"Le joueur {current_player} a gagné !")

# Function that switches the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Function drawing the winning line
def draw_winning_line(start_x, start_y, end_x, end_y):
    canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=5)

# Function that checks if there is a winner
def check_winner(clicked_row, clicked_column):
    # Check row
    count = 0
    for i in range (3): 
        current_button = buttons [i][clicked_row]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:   
        print_winner()
        #draw_winning_line(0, clicked_row * 167 + 83, 500, clicked_row * 167 + 83)
    
    # Check column
    count = 0
    for i in range (3):
        current_button = buttons [clicked_column][i]
        if current_button ['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()
        #draw_winning_line(clicked_column * 167 + 83, 0, clicked_column * 167 + 83, 500)
    
    # Check diagonal
    count = 0
    for i in range (3):
        current_button = buttons [i][i]
        if current_button ['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()
        #draw_winning_line(0, 0, 500, 500)
    
    # Check diagonal 2
    count = 0
    for i in range (3):
        current_button = buttons [2-i][i]
        if current_button ['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()
        #draw_winning_line(0, 500, 500, 0)

    # Check if the grid is full
    count = 0
    for column in buttons:
        for button in column:
            if button['text'] != "":
                count += 1
    if count == 9:
        check_nul()
        print("Match nul")

# Function that is called when a button is clicked
def place_symbol(row, column):
    print("Button clicked", row, column)

    clicked_button = buttons[column][row]
    if clicked_button ['text']== "":
        clicked_button.config(text=current_player)
        if current_player == "X":
            clicked_button.config(foreground="lightgreen")
        else:
            clicked_button.config(foreground="lightblue")

        check_winner(row, column)
        switch_player()

# Function that shows a custom messagebox
def show_custom_messagebox(title, message):

    custom_box = Toplevel(root)
    custom_box.title(title)
    custom_box.geometry("300x150")
    custom_box.config(bg="lightblue")

    message_label = tk.Label(custom_box, text=message, bg="lightblue", font=("Arial", 14))
    message_label.pack(pady=20)

    ok_button = tk.Button(custom_box, text="OK", command=custom_box.destroy, font=("Arial", 12))
    ok_button.pack(pady=10)

# Function that draws the grid
def draw_grid():
    for column in range(3):
        button_in_column = []
        for row in range(3):
            button = tk.Button(
                root, font=("Arial", 50),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column, padx=5, pady=5)    
            button_in_column.append(button)
        buttons.append(button_in_column)    

buttons  = []

# Create a list to store the buttons
buttons = []
current_player = "X"
win = False

# Create the main window
root = tk.Tk()

# Set the title and the size of the window
root.title("TicTacToe")
root.minsize (500, 500)

# Create style for the button
style = ttk.Style()
style.configure("Rounded.TButton", font=("Arial", 20), padding=10, borderwidth=5, relief="raised")

# Draw the grid
draw_grid()

#Create the canvas for drawing the winning line
#canvas = tk.Canvas(root, width=500, height=500)
#canvas.grid(row=0, column=0, rowspan=3, columnspan=3)

#Create reset button
reset_button = ttk.Button(root, text="Reset", style="Rounded.TButton", command=reset)
reset_button.grid(row=3, column=1, pady=20)

# Start the main loop
root.mainloop() 
