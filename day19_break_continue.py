"""
# Day 19: Break and Continue

`break` immediately exits the nearest loop.  `continue` skips the rest of
the current iteration and begins the next one.  They are useful for early
success, invalid records, sentinels, and filtering.

When a loop has an `else` clause, it runs only if the loop ends without
`break`; `continue` does not prevent the `else` clause.
"""

# Skip an unwanted value with continue.
for number in range(1, 8):
    if number % 2 == 0:
        continue
    print("Odd number:", number)

# Stop searching once the target is found.
target = 5
for number in range(1, 10):
    if number == target:
        print("Found:", target)
        break
else:
    print("Target was not found.")

# This else runs because no break occurred.
for number in (2, 4, 6):
    if number == 5:
        break
else:
    print("No value matched 5.")

# `break` applies only to the innermost loop.
for row in range(2):
    for column in range(3):
        if column == 1:
            break
        print("Cell:", row, column)

# Edge case: validate records by skipping malformed entries.
values = [10, None, 5]
total = 0
for value in values:
    if value is None:
        continue
    total += value
print("Total of usable values:", total)
