"""
# Day 17: For Loops

A `for` loop iterates over each item in an iterable such as a string, list,
tuple, or `range`.  `range(start, stop, step)` excludes `stop`, so
`range(1, 4)` produces 1, 2, and 3.  The loop variable is assigned each item
in turn.

Use `enumerate()` when both an index and item are needed.  A loop can have an
`else` clause that runs when it finishes normally, not when it uses `break`.
"""

for character in input("Enter text to iterate over: "):
    print("Character:", character)

stop = int(input("Count up to (exclusive): "))
for number in range(1, stop):
    print("Number:", number)

# Start and step make a countdown possible.
for number in range(10, 4, -2):
    print("Countdown:", number)

# enumerate() supplies zero-based indexes.
for index, fruit in enumerate(["apple", "banana"], start=1):
    print(index, fruit)

# A loop can accumulate a result.
total = 0
for number in range(1, stop):
    total += number
print("Total:", total)

# Edge case: an empty range executes zero times, then reaches its else clause.
for number in range(3, 3):
    print("Never printed:", number)
else:
    print("Empty range completed.")
