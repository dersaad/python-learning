# This script is a simple game where the user guesses a random number between 1 and 10.

import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Set the maximum number of attempts
max_attempts = 3
attempts = 0

# Main game loop
while attempts < max_attempts:
    # Take user input for the guess
    try:
        user_guess = int(input("Please guess a number between 1 and 10:\n").strip())
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    # Increment the attempt counter
    attempts += 1

    # Check if the guess is correct
    if user_guess == random_number:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
    else:
        print(f"Wrong guess! You have {max_attempts - attempts} attempts left.")

# If the user runs out of attempts
if attempts == max_attempts:
    print(f"Sorry, you've used all your attempts. The correct number was {random_number}.")