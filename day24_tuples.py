"""
# Day 24: Tuples

A tuple is an ordered, immutable collection written with parentheses.
Tuples support indexing, slicing, iteration, and membership checks, but
their item assignments are not allowed.  A one-item tuple requires a
trailing comma: `(42,)`; `(42)` is just an integer in parentheses.

Tuples are useful for fixed records and unpacking multiple returned values.
"""

coordinates = tuple(map(int, input(
    "Enter two coordinates separated by a space: "
).split()))
mixed_tuple = ("Mina", 21, True)
single_item = (42,)
not_a_tuple = (42)

print("Coordinates:", coordinates)
print("First coordinate:", coordinates[0])
print("Last item:", mixed_tuple[-1])
print("Single-item type:", type(single_item).__name__)
print("Parenthesized number type:", type(not_a_tuple).__name__)

# Tuples can be iterated and tested for membership.
for coordinate in coordinates:
    print("Coordinate:", coordinate)
print("20 in coordinates:", 20 in coordinates)

# Tuple unpacking assigns each item to a name.
x, y = coordinates
print("x and y:", x, y)

# Edge case: unpacking requires the same number of targets and values.
# x, y = (1, 2, 3)  # ValueError: too many values to unpack.
# coordinates[0] = 99  # TypeError: tuples are immutable.

# A tuple may contain a mutable object; immutability applies to its slots.
tuple_with_list = (["red"],)
tuple_with_list[0].append("blue")
print("Mutable inner list changed:", tuple_with_list)
