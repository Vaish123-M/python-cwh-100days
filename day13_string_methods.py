"""
# Day 13: String Methods

String methods return transformed strings or useful information.  Common
methods include `upper()`, `lower()`, `strip()`, `replace()`, `split()`,
`capitalize()`, `find()`, and `endswith()`.  Since strings are immutable,
save a returned value if the transformation is needed later.

Methods are called with dot notation and parentheses, for example
`text.upper()`.  Most methods are case-sensitive unless documented otherwise.
"""

messy_text = "  hello, python world  "
print("Upper:", messy_text.upper())
print("Lower:", messy_text.lower())
print("Capitalized:", messy_text.strip().capitalize())
print("Stripped:", messy_text.strip())

# replace() substitutes every matching occurrence unless count is supplied.
print("Replaced:", messy_text.strip().replace("python", "Python"))
print("Replace once:", "one one one".replace("one", "1", 1))

# split() creates a list; join() performs the reverse style of operation.
words = "red,green,blue".split(",")
print("Words:", words)
print("Joined:", " | ".join(words))

# find() returns the first index, or -1 when the substring is absent.
sentence = "Python is readable"
print("Index of 'read':", sentence.find("read"))
print("Missing index:", sentence.find("Java"))
print("Ends with 'able':", sentence.endswith("able"))

# Edge case: strip() removes whitespace at the ends, not characters inside.
print("Internal spaces remain:", " a  b ".strip())

# String methods are case-sensitive and return new strings.
original = "python"
changed = original.upper()
print("Original:", original, "Changed:", changed)
