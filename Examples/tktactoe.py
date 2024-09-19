import tkinter as tk

window = tk.Tk()

# {{## BEGIN tic-tac-toe-2 ##}}
playerturn = "X"

def buttonclick(event):
    """This is the button-click handler"""
    global playerturn
    event.widget["text"] = playerturn
    if playerturn == "X":
        playerturn = "O"
    else:
        playerturn = "X"
# {{## END tic-tac-toe-2 ##}}


# {{## BEGIN tic-tac-toe-1 ##}}
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        button = tk.Button(master=frame, width=15, height=5, text=f" ")
        button.bind("<Button-1>", buttonclick)
        button.pack()
# {{## END tic-tac-toe-1 ##}}

window.mainloop()
