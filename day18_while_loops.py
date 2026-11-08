"""
# Day 18: While Loops

A `while` loop repeats while its condition is true.  The loop body must
eventually change relevant state or use a control statement; otherwise it
can run forever.  `while` also supports an `else` block that runs when the
condition becomes false normally.

Use `for` when iterating over a known sequence and `while` when repetition
depends on a condition or an event.
"""

maximum_attempts = int(input("Enter the maximum number of attempts: "))
attempt = 1
while attempt <= maximum_attempts:
    print("Attempt:", attempt)
    attempt += 1  # Progress prevents an infinite loop.
else:
    print("All attempts completed.")

# A sentinel value controls when input-like processing ends.
pending = [task.strip() for task in input(
    "Enter tasks separated by commas: "
).split(",") if task.strip()]
while pending:
    task = pending.pop(0)
    print("Processing:", task)

# The condition is false immediately, so this body is skipped.
count = 0
while count > 0:
    print("Not printed")
print("No work remained.")

# Edge case: always update the state in a bounded retry loop.
remaining = 3
while remaining:
    remaining -= 1
print("Remaining retries:", remaining)

# `while True` is valid only when a reachable break exists.
value = 0
while True:
    value += 1
    if value == 2:
        break
print("Stopped at:", value)
