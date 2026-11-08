"""
# Day 36: Exception Handling

Exceptions report runtime problems such as invalid input, missing dictionary
keys, or division by zero.  Use `try` for risky code and catch specific
exceptions with `except` so unrelated programming errors remain visible.
"""

def divide(left, right):
    """Return left divided by right, or report expected input errors."""
    try:
        return left / right
    except ZeroDivisionError:
        print("A number cannot be divided by zero.")
    except TypeError:
        print("Both values must be numbers.")
    return None


left = float(input("Enter the dividend: "))
right = input("Enter the divisor: ")
try:
    right = float(right)
except ValueError:
    print("The divisor is not a number.")
else:
    print("Result:", divide(left, right))

# Convert user-like text while handling only the expected conversion error.
for text in (input("Enter an integer: "),):
    try:
        number = int(text)
    except ValueError:
        print("Invalid integer:", text)
    else:
        print("Parsed integer:", number)

# The `else` block runs only when the try block succeeds.
scores = {"Mina": int(input("Enter Mina's score: "))}
try:
    print("Mina's score:", scores["Mina"])
    print("Asha's score:", scores["Asha"])
except KeyError as error:
    print("Missing student:", error.args[0])
