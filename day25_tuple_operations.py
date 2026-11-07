"""
# Day 25: Operations on Tuples

Tuples support concatenation with `+`, repetition with `*`, slicing, and
the methods `count()` and `index()`.  They cannot be modified directly.
To add or remove items, convert the tuple to a list, modify the list, and
convert it back.

Slicing follows `[start:stop:step]`, with an exclusive stop index.
"""

numbers = (1, 2, 3, 2)
print("Slice:", numbers[1:3])
print("Reversed:", numbers[::-1])
print("Concatenated:", numbers + (4, 5))
print("Repeated:", ("go",) * 3)
print("Count of 2:", numbers.count(2))
print("First 3 at:", numbers.index(3))

# Convert temporarily when a new tuple with changed contents is required.
temporary = list(numbers)
temporary.append(6)
temporary.remove(1)
numbers = tuple(temporary)
print("Changed through list conversion:", numbers)

# Tuple unpacking and starred unpacking are practical operations.
first, *middle, last = numbers
print("First:", first, "Middle:", middle, "Last:", last)

# Edge cases: index() raises ValueError when no item matches.
try:
    numbers.index(999)
except ValueError:
    print("999 is not present.")

# A one-item tuple still needs its comma during concatenation.
print("Single tuple:", (10,))
