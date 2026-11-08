"""
# Day 14: If, Elif, and Else

Conditional statements choose a branch based on a Boolean expression.
`if` checks the first condition, `elif` checks alternatives in order, and
`else` handles all remaining cases.  Indentation defines each block and is
required; four spaces are the conventional indentation.

Relational operators include `==`, `!=`, `<`, `>`, `<=`, and `>=`.
Logical operators are `and`, `or`, and `not`.  Comparisons can be chained,
such as `0 <= score <= 100`.
"""

score = float(input("Enter a score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "Needs improvement"
print("Grade:", grade)

# Conditions can combine comparisons with logical operators.
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").strip().lower() == "yes"
if age >= 18 and has_id:
    print("Entry permitted.")
else:
    print("Entry denied.")

# Truthiness lets collections participate in conditions.
items = ["notebook"]
if items:
    print("The basket is not empty.")
if not []:
    print("An empty list is false.")

# Use == for comparison; a single = performs assignment and is invalid here.
# if score = 100:  # SyntaxError.

# Edge case: validate a bounded value before categorizing it.
percentage = float(input("Enter a percentage: "))
if not 0 <= percentage <= 100:
    print("Percentage is outside the valid range.")
elif percentage >= 50:
    print("Pass")
else:
    print("Fail")
