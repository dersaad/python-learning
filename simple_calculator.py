# This script performs basic arithmetic operations with error handling and retry.

def get_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Error: Please enter a valid number (digits only).")

def get_operation():
    while True:
        operation = input("Choose an operation (+, -, *, /):\n").strip()
        if operation in ["+", "-", "*", "/"]:
            return operation
        else:
            print("Error: Invalid operation! Please choose from (+, -, *, /).")

# Take user input for numbers and operation
num1 = get_number("Enter the first number:\n")
num2 = get_number("Enter the second number:\n")
operation = get_operation()

# Perform the selected operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
        exit()  # Exit the script if division by zero is attempted
    else:
        result = num1 / num2

# Display the result
print(f"Result: {result}")