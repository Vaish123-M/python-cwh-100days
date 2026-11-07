"""
# Day 6: Variables and Data Types

Common built-in types include `int` (whole numbers), `float` (decimal
numbers), `complex`, `bool`, `str` (text), `list`, `tuple`, `set`, `dict`,
and `NoneType`.  `type(value)` reports a value's type.

Lists and dictionaries are mutable; strings and tuples are immutable.
Choose a type based on the operations and data model you need.
"""

whole_number = 42
decimal_number = 3.14
truth_value = True
text = "Python"
items = ["book", "pen"]          # Ordered, mutable collection.
coordinates = (10, 20)           # Ordered, immutable collection.
unique_numbers = {1, 2, 2, 3}   # Duplicate 2 is stored once.
person = {"name": "Mina", "age": 20}
nothing = None                   # Explicitly represents no value.

for label, value in [
    ("int", whole_number), ("float", decimal_number),
    ("bool", truth_value), ("str", text), ("list", items),
    ("tuple", coordinates), ("set", unique_numbers),
    ("dict", person), ("None", nothing),
]:
    print(f"{label}: {value!r} -> {type(value).__name__}")

# Indexing starts at zero; negative indexes count from the end.
print("First character:", text[0])
print("Last item:", items[-1])

# Lists can change in place; strings cannot.
items.append("notebook")
print("Updated list:", items)
# text[0] = "p"  # TypeError: strings are immutable.

# Edge case: division produces a float, and division by zero is invalid.
print("7 / 2:", 7 / 2)
# print(7 / 0)  # ZeroDivisionError.
