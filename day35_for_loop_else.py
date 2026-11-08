"""
# Day 35: For Loop with Else

The `else` block of a `for` loop runs when the loop finishes normally.
It does not run when the loop exits with `break`.  This is useful for
searches: the loop can break when it finds a match, and `else` handles the
case where no match was found.
"""

target = int(input("Enter a number to search for from 1 to 10: "))
for number in range(1, 11):
    if number == target:
        print("Found:", target)
        break
else:
    print("Target was not found.")

# Because no value matches 99, the loop completes and else runs.
for number in (2, 4, 6):
    if number == 99:
        break
else:
    print("No value matched 99.")

# An empty iterable also completes normally, so its else block runs.
for item in []:
    print("Never printed:", item)
else:
    print("The empty loop completed.")

# `continue` does not prevent else; only `break` does.
for number in range(1, 5):
    if number % 2 == 0:
        continue
    print("Odd number:", number)
else:
    print("Loop completed without break.")
