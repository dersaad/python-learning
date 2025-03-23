# This script checks if a person is eligible for an Egyptian ID based on nationality and age.

# Take user input for nationality
is_egyptian = input("Are you Egyptian? Type 'yes' or 'no':\n").strip().lower()

# Check eligibility
if is_egyptian == "yes":
    age = input("Are you above 18? Type 'yes' or 'no':\n").strip().lower()
    if age == "yes":
        print("You can have an ID.")
    elif age == "no":
        print("Sorry, you have to be 18 or older.")
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")
elif is_egyptian == "no":
    print("Sorry, an Egyptian ID is given only to Egyptians.")
else:
    print("Invalid input! Please enter 'yes' or 'no'.")