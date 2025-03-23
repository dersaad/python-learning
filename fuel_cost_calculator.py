# This script calculates the total fuel cost for a trip.

# Take user input for distance, fuel consumption, and price per liter
try:
    distance = float(input("Enter the distance (in kilometers):\n"))
    fuel_consumption = float(input("Enter the fuel consumption per 100 kilometers (in liters):\n"))
    price_per_liter = float(input("Enter the price per liter of fuel (in $):\n"))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Validate inputs
if distance <= 0 or fuel_consumption <= 0 or price_per_liter <= 0:
    print("Invalid input! All values must be greater than 0.")
    exit()

# Calculate the total cost
total_cost = (distance / 100) * fuel_consumption * price_per_liter

# Display the result
message = f"Total fuel cost: {total_cost:.2f} $."
print(message)