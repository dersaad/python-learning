# This script checks if a person is eligible to drive based on age and driver's license.

# Take user input for name
name = input("Please enter your name:\n").strip()

# Take user input for age
while True:
    try:
        age = int(input("Please enter your age:\n").strip())
        break
    except ValueError:
        print("Invalid input! Please enter a valid age.")

# Take user input for driver's license
while True:
    license = input("Do you have a driver's license? (yes/no)\n").strip().lower()
    if license in ["yes", "no"]:
        break
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")

# Check eligibility
if age > 18 and license == "yes":
    print(f"Alright {name}, you can drive.")
else:
    print(f"Sorry {name}, you cannot drive. You do not meet the requirements.")