# This script demonstrates copying a list in Python.

my_frined = ["elbota", "mahmoud", "mostafa", "goe", "mego", "nada", "maha"]

# Copying the list
copied_list = my_frined.copy()
copied_list.append("saad")
copied_list.remove("goe")

print(f"Original List: {my_frined}")
print(f"Copied List: {copied_list}")