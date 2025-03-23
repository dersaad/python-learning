# This script classifies a grade into categories (Excellent, Good, Acceptable, Fail).

# Welcome message
print("Welcome! Please enter your grade (0 - 100).")

# Take user input for grade
try:
    grade = float(input("Enter the grade as a number:\n").strip())
except ValueError:
    print("Invalid input! Please enter a numerical grade between 0 and 100.")
    exit()

# Validate input
if not (0 <= grade <= 100):
    print("Error: Grade must be between 0 and 100.")
    exit()

# Classify the grade
if grade >= 90:
    print("Congratulations, your grade is Excellent!")
elif grade >= 75:
    print("Congratulations, your grade is Good!")
elif grade >= 50:
    print("Your grade is Acceptable.")
else:
    print("You have failed this year, but you can make up for it next year.")