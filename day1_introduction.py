""" 
# Day 1: Introduction to Python

This lesson introduces Python, a readable, interpreted, general-purpose
language.  We run statements from top to bottom and use indentation to
describe blocks.  Python files use the `.py` extension.

Core ideas:
- A statement is an instruction, and an expression produces a value.
- Python is case-sensitive: `print` and `Print` are different names.
- `#` starts a single-line comment; comments are ignored by Python.
"""

# The first program traditionally prints a greeting.
print("Hello, Python!")

# A string literal is text enclosed in matching single or double quotes.
message = "Python uses significant indentation."
print(message)

# Expressions can be evaluated inside a print call.
print("2 + 3 =", 2 + 3)

# Names must be spelled consistently.  This would fail because the names
# are case-sensitive: print("hello") and Print("hello") are not equivalent.

# Python allows multiple statements, but one statement per line is clearer.
language = "Python"
version = 3
print(language, version)

# Edge case: an empty string is valid text, but it contains no characters.
empty_text = ""
print("Empty text length:", len(empty_text))
