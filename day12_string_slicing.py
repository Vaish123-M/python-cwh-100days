"""
# Day 12: String Slicing and Operations

Indexing uses `text[index]`; slicing uses `text[start:stop:step]`.  The start
is included, the stop is excluded, and omitted values use sequence defaults.
Positive indexes count from the left; negative indexes count from the right.

`len()` returns the number of characters.  A slice never raises an error when
its bounds extend beyond the string, but a step of zero is invalid.
"""

text = input("Enter some text: ")
print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])

# The stop index is exclusive: indexes 0 through 5 produce "Python".
print("First word:", text[0:6])
print("From index 7:", text[7:])
print("Up to index 6:", text[:6])
print("Copy:", text[:])

# A step selects every nth character.  A negative step reverses a sequence.
print("Every second character:", text[::2])
print("Reversed:", text[::-1])

# Negative slicing is convenient for suffixes.
filename = "report.txt"
print("Extension:", filename[-3:])
print("Without extension:", filename[:-4])

# Slices beyond the bounds are safely clipped.
print("Clipped slice:", text[-100:100])

# Edge case: an empty or backwards slice can be valid but contains no text.
print("Backwards with positive step:", text[10:3])
# print(text[::0])  # ValueError: slice step cannot be zero.

# Slicing creates a new string; the original is unchanged.
prefix = text[:6]
print("Original:", text, "Prefix:", prefix)
