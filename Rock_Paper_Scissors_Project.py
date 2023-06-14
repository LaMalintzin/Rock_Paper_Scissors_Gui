import random

# Very simple Rock Paper Scissors game created by chatGPT

# 1. Use tkinter to create an GUI
# 2. Make the game continiue without restarting it each time.
# 3. Add a function to determine whos gets to 10 points first.
# 4. Add give up function, computer will say "Skynet will never loose!!!"

def play_game():
    print("Let's play Rock-Paper-Scissors!")
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    choices = ["Rock", "Paper", "Scissors"]
    
    while True:
        player_choice = input("Your turn: ")
        if player_choice.isdigit() and 1 <= int(player_choice) <= 3:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
    
    player_choice = choices[int(player_choice) - 1]
    computer_choice = random.choice(choices)
    
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

play_game()