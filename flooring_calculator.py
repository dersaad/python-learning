# This script calculates the total cost of flooring based on user input.

# Take user input for dimensions and price
length = float(input("Please enter the length (in meters):\n"))
width = float(input("Please enter the width (in meters):\n"))
price_per_meter = float(input("How much does 1 square meter cost? (in $):\n"))

# Calculate total area and total cost
total_area = length * width
total_cost = price_per_meter * total_area

# Display the results
message = f"""
The total area is: {total_area} square meters.
Total cost: {total_cost} $.
"""
print(message)