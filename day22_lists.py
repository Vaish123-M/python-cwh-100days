"""
# Day 22: Introduction to Lists

A list is an ordered, mutable collection written with square brackets.
Items may have different types.  Indexing starts at zero, negative indexes
count from the end, and `in` tests membership.

Lists can be changed after creation, unlike strings and tuples.  A list
stores references to objects, so copying and aliasing should be understood.
"""

shopping = [item.strip() for item in input(
    "Enter shopping items separated by commas: "
).split(",") if item.strip()]
mixed = ["text", 42, True]
print("Shopping:", shopping)
print("Mixed values:", mixed)

# Indexing and negative indexing select one item.
print("First item:", shopping[0])
print("Last item:", shopping[-1])

# `in` and `not in` test whether an item exists.
if "tea" in shopping:
    print("Tea is on the list.")
if "coffee" not in shopping:
    print("Coffee is not on the list.")

# Lists support slicing just like strings.
print("First two:", shopping[:2])

# Mutation changes the existing list.
shopping[1] = "green tea"
print("Updated:", shopping)

# Edge case: an empty list is false, and indexing it raises IndexError.
empty = []
if not empty:
    print("The list is empty.")
# print(empty[0])  # IndexError: list index out of range.

# A list can contain another list.
matrix = [[1, 2], [3, 4]]
print("Nested item:", matrix[1][0])
