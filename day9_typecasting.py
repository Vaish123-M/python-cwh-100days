"""
# Day 9: Typecasting

Typecasting (conversion) creates a value of another type.  Common functions
are `int()`, `float()`, `str()`, `bool()`, `list()`, and `tuple()`.
Conversions must be valid: `int("12")` works, but `int("12.5")` does not.

Explicit conversion is clearer than relying on implicit numeric promotion.
Remember that `bool("")`, `bool(0)`, `bool([])`, and `bool(None)` are False;
most other non-empty/non-zero values are True.
"""

text_number = "15"
integer_number = int(text_number)
decimal_number = float(text_number)
print("Integer:", integer_number, type(integer_number).__name__)
print("Float:", decimal_number, type(decimal_number).__name__)
print("Text:", str(integer_number), type(str(integer_number)).__name__)

# Convert a string of characters into a list of individual characters.
print("Characters:", list("cat"))
print("Tuple:", tuple([1, 2, 3]))

# Boolean conversion follows truthiness, not textual meaning.
print("bool(0):", bool(0))
print("bool('False'):", bool("False"))  # Non-empty text is True.

# Edge case: catch invalid external text instead of crashing unexpectedly.
user_text = "12.5"
try:
    print(int(user_text))
except ValueError:
    print("That text is a decimal, not a whole-number literal.")

# Converting a float to int truncates toward zero; it does not round.
print("int(-3.9):", int(-3.9))
