# This script generates a random 4-digit PIN and checks if it matches the user's input.

import random

# Set the maximum number of attempts
max_attempts = 3
attempts = 0

# Main loop
while attempts < max_attempts:
    # Take user input for a 4-digit PIN
    user_pin = input("Please enter a 4-digit PIN:\n").strip()

    # Validate user input
    if not user_pin.isdigit() or len(user_pin) != 4:
        print("Invalid input! Please enter exactly 4 digits.")
        attempts += 1
        print(f"You have {max_attempts - attempts} attempts left.")
        continue

    # Generate a random 4-digit PIN
    digits = "0123456789"  # All possible digits
    computer_pin = "".join(random.choices(digits, k=4))

    # Display the generated PIN
    print(f"Generated PIN: {computer_pin}")

    # Check if the user's PIN matches the generated PIN
    if user_pin == computer_pin:
        print("Correct password!")
        break
    else:
        attempts += 1
        print(f"Wrong password. You have {max_attempts - attempts} attempts left.")

# If the user runs out of attempts
if attempts == max_attempts:
    print("Sorry, you've used all your attempts.")