"""
# Day 10: User Input

`input(prompt)` displays a prompt and returns the user's response as a
string after Enter is pressed.  Convert that string explicitly when a
number is required.  `strip()` removes surrounding whitespace.

Interactive programs should validate input and explain errors.  The
`EOFError` handler below also makes the script safe when input is redirected
or unavailable in an automated run.
"""

try:
    name = input("What is your name? ").strip()
    age_text = input("What is your age? ").strip()
except EOFError:
    print("No input was provided.")
else:
    # Empty input is valid text syntactically, but not a useful name here.
    if not name:
        print("Please provide a non-empty name.")
    else:
        try:
            age = int(age_text)
        except ValueError:
            # This handles text such as "", "twenty", and "12.5".
            print("Age must be a whole number, such as 20.")
        else:
            if age < 0:
                print("Age cannot be negative.")
            else:
                print(f"Hello, {name}! You are {age} years old.")

# `input()` always returns text: input("2") gives "2", not integer 2.
# Use float() instead of int() when decimal input is expected.
# Never use eval(input(...)) for ordinary user data: it can execute code.
