# This script demonstrates filtering a list in Python.

my_frined = ["elbota", "mahmoud", "mostafa", "goe", "mego", "nada", "maha"]

# Filtering names that start with 'm'
filterated_name = []
for name in my_frined:
    if name.lower().startswith("m"):
        filterated_name.append(name)
print(filterated_name)