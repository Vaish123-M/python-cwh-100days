"""
# Day 8: Calculator Exercise Solution

This solution packages the calculator in a function so it can be reused.
`return` sends a value back to the caller.  A guard prevents division by
zero before using `/`, `//`, or `%`.

The function accepts numbers; input conversion belongs at the user-interface
boundary.  This keeps the calculation easy to test with integers or floats.
"""


def calculate(first_number, second_number):
    """Return all calculator results as a dictionary."""
    if second_number == 0:
        raise ValueError("The second number must not be zero.")

    return {
        "addition": first_number + second_number,
        "subtraction": first_number - second_number,
        "multiplication": first_number * second_number,
        "true division": first_number / second_number,
        "floor division": first_number // second_number,
        "remainder": first_number % second_number,
        "exponentiation": first_number ** second_number,
    }


results = calculate(50, 3)
for operation, result in results.items():
    print(f"{operation.title()}: {result}")

# Edge case: handle the expected error explicitly at the call site.
try:
    calculate(10, 0)
except ValueError as error:
    print("Calculator error:", error)

# Negative floor division rounds down, rather than truncating toward zero.
print("Negative floor division:", calculate(-7, 2)["floor division"])
