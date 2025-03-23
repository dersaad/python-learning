# This script converts temperature from Celsius to Fahrenheit.

# Take user input for temperature in Celsius
try:
    temperature = float(input("Please enter the temperature in Celsius:\n"))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# Convert Celsius to Fahrenheit
fahrenheit = (9/5 * temperature) + 32

# Display the result with 2 decimal places
message = f"The temperature in Fahrenheit is {fahrenheit:.2f}."
print(message)