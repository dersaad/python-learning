# This script simulates a basic login system with limited attempts.

# Set the correct credentials
correct_name = "saad"
correct_password = "12345"

# Set the maximum number of attempts
max_attempts = 3
attempts = 0

# Login loop
while attempts < max_attempts:
    # Take user input for name and password
    name = input("Please enter your name:\n").strip().lower()
    password = input("Please enter your password:\n").strip()

    # Check credentials
    if name == correct_name and password == correct_password:
        print("Welcome back, Saad!")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print(f"Sorry, wrong name or password. You have {max_attempts - attempts} attempts left.")
        else:
            print("Sorry, you have used all your attempts. Please try again later.")