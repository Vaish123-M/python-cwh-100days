"""
# Day 23: List Methods

List methods mutate the list or return information about it.  Important
methods include `append()`, `insert()`, `sort()`, `reverse()`, `index()`,
`count()`, and `copy()`.  Most mutating methods return `None`; do not assign
their result when you want to keep the list.
"""

numbers = [int(number) for number in input(
    "Enter numbers separated by spaces: "
).split()]
numbers.append(5)
numbers.insert(1, 9)
print("After append and insert:", numbers)

# sort() and reverse() modify the list in place.
numbers.sort()
print("Sorted:", numbers)
numbers.reverse()
print("Reversed:", numbers)

# index() finds the first matching position; count() counts all matches.
print("First 1 at index:", numbers.index(1))
print("Number of 1s:", numbers.count(1))

# copy() makes a shallow copy, so top-level changes are independent.
backup = numbers.copy()
numbers.append(100)
print("Original:", numbers)
print("Copy:", backup)

# Edge cases: missing index values raise ValueError, and sort() returns None.
try:
    numbers.index(999)
except ValueError:
    print("999 is not in the list.")

sort_result = numbers.sort()
print("sort() return value:", sort_result)

# `list.copy()` is shallow for nested lists.
nested = [["a"]]
nested_copy = nested.copy()
nested_copy[0].append("b")
print("Nested values share the inner list:", nested)
