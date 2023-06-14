import random
from tkinter import *


# Main screen
master = Tk()
master.title("Rock Paper Scissors-Game")

#Labels (Etiketter) 
Label(master, text="<---Rock---Paper---Scissors---> ", font=("Calibri", 16)).grid(row=0, sticky=N, pady=10, padx=200)
Label(master, text="Please make your move ", font=("Calibri", 14)).grid(row=1, sticky=N)

player_score_label = Label(master, text="Player score : 0 ", font=("Calibri", 12))
player_score_label.grid(row=2, sticky=W)

cpu_score_label = Label(master, text="Cpu score : 0 ", font=("Calibri", 12))
cpu_score_label.grid(row=2, sticky=E)

player_choice_label = Label(master, font=("Calibri", 12))
player_choice_label.grid(row=3, sticky=W)

cpu_choice_label = Label(master, font=("Calibri", 12))
cpu_choice_label.grid(row=3, sticky=E)

outcome_label = Label(master, font=("Calibri", 12))
outcome_label.grid(row=3, sticky=N)

# Dummy Label to make an extra gap under the buttons
Label(master).grid(row=5)

master.mainloop()
