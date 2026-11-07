"""
# Day 7: Calculator Exercise

Exercise: define two numbers and display their sum, difference, product,
quotient, floor quotient, remainder, and exponent.  Arithmetic operators
are `+`, `-`, `*`, `/`, `//`, `%`, and `**`.

This first version focuses on translating an exercise into expressions.
The next lesson adds a reusable solution with validation.
"""

first_number = 50
second_number = 3

# Each expression is evaluated before print displays its label and result.
print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("True division:", first_number / second_number)
print("Floor division:", first_number // second_number)
print("Remainder:", first_number % second_number)
print("Exponentiation:", first_number ** second_number)

# Parentheses make precedence explicit: multiplication happens before
# addition without them, so (first_number + second_number) changes the result.
print("Grouped expression:", (first_number + second_number) * 2)

# Edge case: the divisor must not be zero for /, //, or %.
safe_divisor = 0
if safe_divisor == 0:
    print("Cannot divide by zero.")
