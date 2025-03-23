# This script calculates the future time after a given number of hours.

# Take user input for current time and hours to pass
try:
    current_hour = int(input("What is the current hour (0-23)?\n"))
    current_minute = int(input("What is the current minute (0-59)?\n"))
    hours_passed = int(input("Enter the number of hours that will pass:\n"))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Validate current time input
if current_hour < 0 or current_hour > 23 or current_minute < 0 or current_minute > 59:
    print("Invalid time! Please enter a valid time (hour: 0-23, minute: 0-59).")
    exit()

# Calculate the new time
total_minutes = current_hour * 60 + current_minute + hours_passed * 60
new_hour = (total_minutes // 60) % 24
new_minute = total_minutes % 60

# Display the result
message = f"The time after {hours_passed} hours will be: {new_hour:02d}:{new_minute:02d}."
print(message)