"""
# Day 11: Strings in Python

A string (`str`) is an immutable sequence of Unicode characters.  It can be
created with single quotes, double quotes, or triple quotes.  Matching quote
characters may be escaped with a backslash.  Because a string is a sequence,
it supports indexing, iteration, and membership testing.

Strings are immutable: operations create a new string instead of changing
the original.  Use `str()` to convert another value to text.
"""

single_quoted = 'Python'
double_quoted = "also Python"
triple_quoted = """A triple-quoted string
can span multiple lines."""
print(single_quoted, double_quoted)
print(triple_quoted)

# Escape sequences represent special characters inside a quoted string.
quoted_text = "She said, \"Hello!\"\nThis is a new line."
print(quoted_text)

# A raw string keeps backslashes literal, which is useful for file paths.
windows_path = r"C:\Users\Student\Documents"
print(windows_path)

# Strings behave like sequences: indexes start at zero and iteration visits
# one character at a time.
word = "Python"
print("First character:", word[0])
for character in word:
    print(character, end="|")
print()

# `in` tests whether a substring or character occurs in the string.
print("Py" in word)
print("z" in word)

# Edge case: an empty string is valid, but it has no indexable characters.
empty_string = ""
print("Empty string is false:", bool(empty_string))
# print(empty_string[0])  # IndexError: there is no character at index 0.

# Strings cannot be changed in place; build a replacement instead.
# word[0] = "p"  # TypeError: str does not support item assignment.
lowercase_word = "p" + word[1:]
print(lowercase_word)
