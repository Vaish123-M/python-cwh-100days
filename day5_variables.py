"""
# Day 5: Variables

A variable is a name bound to an object.  Assignment uses `=`, while
comparison uses `==`.  Names may contain letters, digits, and underscores,
but cannot start with a digit or be a Python keyword.  Python uses dynamic
typing: a name can later refer to an object of another type.

Use descriptive `snake_case` names, constants in `UPPER_CASE`, and avoid
shadowing built-ins such as `sum` or `list`.
"""

student_name = input("Enter the student's name: ").strip()
age = int(input("Enter the student's age: "))
is_enrolled = input("Is the student enrolled? (yes/no): ").strip().lower() == "yes"
print(student_name, age, is_enrolled)

# Assignment evaluates the right side first, then binds the name.
next_age = age + 1
print("Next age:", next_age)

# Several names can be assigned at once when the number of values matches.
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
area = width * height
print("Area:", area)

# Swapping needs no temporary variable.
width, height = height, width
print("After swap:", width, height)

# Augmented assignment updates a numeric value.
counter = 0
counter += 1
print("Counter:", counter)

# Edge case: this is rebinding, not changing the original integer object.
value = 10
value = "ten"
print("Value now has a different type:", value)

# `==` compares values; `=` assigns.  `if value = 10` is invalid syntax.
