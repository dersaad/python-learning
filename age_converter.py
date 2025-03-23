# This script calculates age in days and seconds, with an option to include leap years.

# Take user input for age in years
try:
    age = int(input("Enter your age in years:\n"))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Validate input
if age < 0:
    print("Invalid input! Age cannot be negative.")
    exit()

# Ask the user if they want to include leap years
include_leap_years = input("Do you want to include leap years? (yes/no):\n").strip().lower()

# Calculate age in days and seconds
if include_leap_years == "yes":
    leap_years = age // 4  # Approximate number of leap years
    days = age * 365 + leap_years
    message = f"Your age is {age} years, {days:,} days (including leap years), or {days * 86400:,} seconds."
else:
    days = age * 365
    message = f"Your age is {age} years, {days:,} days (excluding leap years), or {days * 86400:,} seconds."

# Display the result
print(message)