# This script simulates a coin toss game where the user guesses the outcome.

import random

# Function to check the winner
def check_winner(user_guess, result):
    print(f"The computer coin toss result was: {result}")
    if user_guess == result:
        print("Congratulations, you have won! 🎉")
        return True
    else:
        print("Sorry, you lost!")
        return False

# Welcome message
print("\nWelcome to the Coin Guessing Game!\nChoose a method to toss the coin:")
print("1. Using random.randint()")
print("2. Using random.random()")

# Take user input for the choice
try:
    choice_number = int(input("Please enter your choice (1 or 2):\n").strip())
except ValueError:
    print("Invalid input! Please enter a number (1 or 2).")
    exit()

# Validate user input
if choice_number not in [1, 2]:
    print("Invalid choice. Please select either 1 or 2.")
    exit()

# Main game loop
while True:
    # Take user input for the guess
    user_guess = input("Enter your guess (Heads or Tails):\n").strip().lower()

    # Perform the coin toss based on the chosen method
    if choice_number == 1:
        result = random.choice(["heads", "tails"])
    else:
        result = "heads" if random.random() > 0.5 else "tails"

    # Check the winner
    if check_winner(user_guess, result):
        break  # Exit the loop if the user wins

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no):\n").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 🎮")
        break