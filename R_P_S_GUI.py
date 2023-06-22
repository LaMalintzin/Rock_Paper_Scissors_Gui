import random
from tkinter import *

#Dictionary and vars
schema = {
    "rock":{"rock":1, "paper":0,"scissors":2},
    "paper":{"rock":2, "paper":1, "scissors":0},
    "scissors":{"rock":0, "paper":2, "scissors":1}
}
cpu_score = 0
player_score = 0

#Function
def outcome_handler(user_choice):
    global cpu_score
    global player_score

    # Disable buttons after a player reaches 10 points
    if player_score == 10 or cpu_score == 10:
        outcome_label.config(fg="yellow", text="Game Over!!!", font=("calibri", 20))
        return
    
    # Array handling the three game values
    outcomes = ["rock","paper","scissors"]
    # Random numbers referencing to the values in the array 
    random_number = random.randint(0,2)
    cpu_choice = outcomes[random_number]
    result = schema[user_choice][cpu_choice]

    # Adding text to the player_choice_label and the computer_choice_label
    player_choice_label.config(fg="red", text="Player Choice : " +str (user_choice))
    cpu_choice_label.config(fg="green" , text="Cpu Choice : " + str(cpu_choice))

    if result == 2:
        player_score = player_score + 2
        player_score_label.config(text="Player : "+str(player_score))
        outcome_label.config(fg="blue", text="Outcome : Player won")
    elif result == 1: 
        player_score = player_score + 1
        cpu_score = cpu_score + 1
        player_score_label.config(text="Player : "+str(player_score))
        cpu_score_label.config(text="Computer : "+str(cpu_score))
        outcome_label.config(fg="blue",text="Outcome : It's a draw")
    elif result == 0:
        cpu_score = cpu_score + 2
        cpu_score_label.config(text="Computer : "+str(cpu_score))
        outcome_label.config(fg="blue", text="Outcome : Computer won")

    #print(outcomes[random_number])


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

# Buttons
Button(master, text="Rock" ,width=15, command=lambda:outcome_handler("rock")).grid(row=4, sticky=W, padx=5, pady=5)
Button(master, text="Paper" ,width=15, command=lambda:outcome_handler("paper")).grid(row=4, sticky=N, padx=5)
Button(master, text="Scissors" ,width=15, command=lambda:outcome_handler("scissors")).grid(row=4, sticky=E, padx=5, pady=5)
# Dummy Label to make an extra gap under the buttons
Label(master).grid(row=5)

master.mainloop()
