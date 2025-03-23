# This script simulates a simple dice roll game.

import random

# Welcome message
print("Welcome to the Dice Roll Game! 🎲")

# Initialize roll counter
roll_count = 0

# Main game loop
while True:
    input("Press Enter to roll the dice... 🎲")
    
    # Roll the dice
    dice_result = random.randint(1, 6)
    roll_count += 1
    
    # Display the result
    print(f"The result of your dice roll is {dice_result} (Roll #{roll_count})")
    
    # Ask the user if they want to roll again
    play_again = input("Do you want to roll again? (yes/no): ").strip().lower()
    
    # Validate user input
    while play_again not in ["yes", "no"]:
        print("Invalid input! Please enter 'yes' or 'no'.")
        play_again = input("Do you want to roll again? (yes/no): ").strip().lower()
    
    # Exit the game if the user doesn't want to continue
    if play_again != "yes":
        print(f"Thanks for playing! You rolled the dice {roll_count} times. 🎲")
        break