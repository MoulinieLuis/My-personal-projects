#This program aims to create a Rock Paper Scissors game
import random

player_choice = input("Choose Rock, Paper or Scissors: ").lower()

computer_choice = random.choice(["rock", "paper", "scissors"])


print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
