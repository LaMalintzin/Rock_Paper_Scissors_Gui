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
    if player_score >= 10 or cpu_score >= 10 or user_choice == "give_up":
        outcome_label.config(fg="brown", text="Game Over!!!", font=("calibri", 20))
        return play_again()
    
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

        # Check winner after the round 
    winner = check_winner(player_score,cpu_score)
    if winner:
        outcome_label.config(fg="brown", text="Game Over!! {} wins!".format(winner))
        
def check_winner(player_score, cpu_score):
    if player_score >= 10:
        return "Player"
    elif cpu_score >= 10:
        return "Computer"
    else:
        return
    
def show_message():
    # Create a new top-level window
    popup_window = Toplevel(master)
    popup_window.title("Give up message")
    
    # Create a label with the message
    message_label = Label(popup_window, fg="brown", text="Skynet will always prevail!!!!", font=("Calibri", 16))
    message_label.pack(padx=20, pady=20)

def restart_game(window):
    global cpu_score
    global player_score

    cpu_score = 0
    player_score = 0

    # Reset score labels
    player_score_label.config(text="Player score: 0")
    cpu_score_label.config(text="Cpu score: 0")

    # Reset outcome label
    outcome_label.config(text="")

    # Enable buttons
    rock_button.config(state=NORMAL)
    paper_button.config(state=NORMAL)
    scissors_button.config(state=NORMAL)

    window.destroy()


def play_again():
    popup_window = Toplevel(master)
    popup_window.title("Play another round?")

    message_label = Label(popup_window, fg="brown", text="Play another round?", font=("Calibri", 24))
    message_label.grid(row=0, columnspan=2, padx=10, pady=20, sticky="n")

    Button(popup_window, text="Yes" ,width=15, command=lambda: restart_game(popup_window)).grid(row=1, column=0, padx=5, sticky="e")
    Button(popup_window, text="No" ,width=15, command=popup_window.destroy).grid(row=1, column=1, padx=5, sticky="w")
    
    Label(popup_window).grid(row=2)


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
rock_button = Button(master, text="Rock" ,width=15, command=lambda:outcome_handler("rock"))
paper_button = Button(master, text="Paper" ,width=15, command=lambda:outcome_handler("paper"))
scissors_button = Button(master, text="Scissors" ,width=15, command=lambda:outcome_handler("scissors"))

rock_button.grid(row=4, sticky=W, padx=5, pady=5)
paper_button.grid(row=4, sticky=N, padx=5)
scissors_button.grid(row=4, sticky=E, padx=5, pady=5)

# Dummy Label to make an extra gap under the buttons
Label(master).grid(row=5)
Label(master).grid(row=6)

give_up_button = Button(master, text="Give up" ,width=30, command=show_message, 
       bg="red", fg="white")

give_up_button.grid(row=7, sticky=S, padx=5, pady=5)

master.mainloop()
