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


print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))
print("10 / text =", divide(10, "text"))

# Convert user-like text while handling only the expected conversion error.
for text in ("42", "not a number"):
    try:
        number = int(text)
    except ValueError:
        print("Invalid integer:", text)
    else:
        print("Parsed integer:", number)

# The `else` block runs only when the try block succeeds.
scores = {"Mina": 95}
try:
    print("Mina's score:", scores["Mina"])
    print("Asha's score:", scores["Asha"])
except KeyError as error:
    print("Missing student:", error.args[0])
