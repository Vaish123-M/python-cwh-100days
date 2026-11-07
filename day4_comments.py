"""
# Day 4: Comments

Comments document intent for humans and are ignored by the interpreter.
Use `#` for a single-line comment.  A triple-quoted string at the beginning
of a module, function, or class is a docstring; it is documentation stored
in `__doc__`, not technically a comment.

Good comments explain why a non-obvious choice exists.  Avoid narrating
obvious code or leaving stale comments that disagree with the program.
"""

# This comment explains the purpose of the constant.
SECONDS_PER_MINUTE = 60

minutes = 5  # Inline comments can clarify a literal when kept brief.
seconds = minutes * SECONDS_PER_MINUTE
print(f"{minutes} minutes contains {seconds} seconds.")

# Comments can temporarily disable a line while experimenting.
# print("This line is intentionally not executed.")

"""
This is a string literal spanning lines.  It can look like a block comment,
but Python still creates the string expression (unless it is a docstring).
Use # comments for ordinary notes.
"""
print("Comments do not change the result of the calculation.")

# Edge case: a # inside quotes is data, not a comment.
hashtag = "# is part of this string"
print(hashtag)
