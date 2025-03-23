# This script simulates a simple Rock, Paper, Scissors game with multiple rounds.

import random

# Welcome message
print("Welcome to Rock, Paper, Scissors!")

# Define the possible choices
choices = ["Rock", "Paper", "Scissors"]

# Main game loop
while True:
    # Take user input for their choice
    user_choice = input("Please enter your choice (Rock, Paper, Scissors):\n").strip().title()

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice! Please enter 'Rock', 'Paper', or 'Scissors'.")
        continue

    # Generate the computer's choice
    computer_choice = random.choice(choices)

    # Display the choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("Congratulations, you won!")
    else:
        print("Game over. Try again.")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no):\n").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break