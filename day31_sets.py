"""
# Day 31: Sets

A set is an unordered, mutable collection of unique values.  Sets remove
duplicates automatically and support fast membership checks.  Use `set()`
to create an empty set because `{}` creates an empty dictionary.
"""

numbers = {1, 2, 2, 3, 4}
empty_set = set()
empty_dictionary = {}

print("Unique numbers:", numbers)
print("Empty set type:", type(empty_set).__name__)
print("Empty dictionary type:", type(empty_dictionary).__name__)

# Sets are useful for membership checks and duplicate removal.
print("3 in numbers:", 3 in numbers)
names = ["Mina", "Asha", "Mina", "Leo"]
print("Unique names:", set(names))

# Sets do not support indexing because they have no positional order.
numbers.add(5)
print("After adding 5:", numbers)

# A set can contain immutable values, but not mutable lists or dictionaries.
coordinates = {(0, 0), (1, 1)}
print("Coordinate set:", coordinates)
# coordinates.add([2, 2])  # TypeError: lists are unhashable.
