"""
# Day 41: Short-hand if-else statements

Python supports a conditional expression for choosing between two values in
one line.  Its general form is:

    value_if_true if condition else value_if_false

The condition is evaluated first.  Only the selected value is used, which is
useful for small decisions such as labels, messages, and display values.
Regular multi-line `if`/`else` blocks are clearer when a decision performs
several actions or contains complicated logic.
"""


# A conditional expression selects one of two strings.
age = 20
message = "You can vote." if age >= 18 else "You cannot vote yet."
print(message)

# The expression can be used directly inside another expression.
number = 7
parity = "even" if number % 2 == 0 else "odd"
print(number, "is", parity)

# A value can be assigned a default when an optional value is missing.
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# Conditional expressions can be nested, but a normal if/elif/else block is
# usually easier to read when there are more than two alternatives.
score = 82
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print("Grade:", grade)

# This is the long form of a decision that performs multiple statements.
if age >= 18:
    access_message = "Access granted"
else:
    access_message = "Access denied"
print(access_message)
