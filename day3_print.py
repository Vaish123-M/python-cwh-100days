"""
# Day 3: The `print` Function

`print()` writes text to standard output.  Its common signature is
`print(*objects, sep=" ", end="\\n")`.  It converts each object to text,
separates objects with `sep`, and finishes with `end`.

Strings may use single or double quotes.  f-strings (`f"{value}"`) embed
expressions and are usually clearer than manual concatenation.
"""

name = "Ada"
score = 95

# Multiple arguments are separated by a space by default.
print("Name:", name, "Score:", score)

# sep changes the text between arguments; end changes the final character.
print("2026", "11", "07", sep="-")
print("Loading", end="...")
print("done")

# f-strings format values without converting them manually.
print(f"{name} scored {score}%")
print(f"Pi to two places: {3.14159:.2f}")

# `str()` explicitly converts an object to text for concatenation.
print("Score as text: " + str(score))

# Edge case: printing no arguments prints only the value of end (a newline).
print()

# `sep` and `end` must be keyword arguments after the positional objects.
# print("a", sep=",", "b")  # SyntaxError: positional argument follows keyword.
