# to make a sname water gun game in python 
import random

choice = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

computer_choice = random.choice(list(choice.keys()))
player_choice = input("Enter your choice: r for rock, p for paper, s for scissors: ")

if player_choice not in choice:
    print("Invalid choice")
else:
    if computer_choice == player_choice:
        print("It's a tie!")
    elif (computer_choice == 'r' and player_choice == 's') or \
         (computer_choice == 'p' and player_choice == 'r') or \
         (computer_choice == 's' and player_choice == 'p'):
        print("Computer wins!")
        print(f"Computer's choice: {choice[computer_choice]}")
        print(f"Player's choice: {choice[player_choice]}")
    else:
        print("Player wins!")
        print(f"Player's choice: {choice[player_choice]}")
        print(f"Computer's choice: {choice[computer_choice]}")