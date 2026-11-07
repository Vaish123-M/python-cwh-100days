"""
# Day 28: f-Strings

An f-string is a formatted string literal prefixed with `f`.  Expressions
inside `{}` are evaluated and inserted into the result.  Format specifiers
after a colon control presentation, such as `.2f` for two decimal places,
`,` for thousands separators, and `:>10` for right alignment.

F-strings are usually clearer than manual string concatenation and preserve
the original value's type while formatting its text representation.
"""

name = "Asha"
items = 3
price = 19.995

print(f"Hello, {name}!")
print(f"{name} bought {items} items.")
print(f"Total: ${price:.2f}")
print(f"Large number: {1234567:,}")
print(f"Aligned: {'Python':>10}")

# Expressions can appear inside braces.
width, height = 8, 5
print(f"Area of {width} x {height}: {width * height}")

# Dates and numbers can be formatted with explicit specifiers.
ratio = 1 / 3
print(f"Ratio: {ratio:.1%}")

# Literal braces are doubled because single braces indicate an expression.
print(f"Dictionary syntax looks like {{'name': '{name}'}}")

# Edge case: None and Boolean values are formatted as their text forms.
missing = None
enabled = True
print(f"Missing: {missing}, Enabled: {enabled}")
