# This script demonstrates basic list operations in Python.

my_frined = ["elbota", "mahmoud", "mostafa", "goe", "mego", "nada", "maha"]

# Adding a new name to the list
user_name = input("Please type your name\n")
if user_name in my_frined:
    print("This name already exists in the list")
else:
    my_frined.append(user_name)
    my_frined.sort()
    print("Name added successfully!")
print(f"Updated List: {my_frined}")

# Modifying the list
my_frined[0] = "Ahmed"
print(f"Modified List: {my_frined}")

# Inserting and appending
my_frined.append("Ali")
my_frined.insert(0, "Sara")
print(f"List after insert and append: {my_frined}")

# Removing elements
my_frined.pop(-1)
my_frined.remove("mahmoud")
print(f"List after removal: {my_frined}")

# Length of the list
print(f"Length of the list: {len(my_frined)}")

# Sorting the list
my_frined.sort()
print(f"Sorted List (Ascending): {my_frined}")

my_frined.sort(reverse=True)
print(f"Sorted List (Descending): {my_frined}")

# Reversing the list
my_frined.reverse()
print(f"Reversed List: {my_frined}")

# Iterating through the list
print("List elements:")
for name in my_frined:
    print(name)

# Checking if an element exists
if "Yousef" in my_frined:
    print("Yes")
else:
    print("No")