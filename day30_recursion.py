"""
# Day 30: Recursion

Recursion is a technique where a function calls itself on a smaller version
of a problem.  Every recursive function needs a base case that stops calls
and a recursive case that moves toward it.

Factorial is defined as n! = n * (n - 1)! with 0! = 1.  Fibonacci numbers
are defined by F(0)=0, F(1)=1, and F(n)=F(n-1)+F(n-2).  The simple Fibonacci
implementation below is educational but exponential; iteration or caching
is better for large values.  Python also limits recursion depth.
"""


def factorial(number):
    """Return n! for a non-negative integer n."""
    if number < 0:
        raise ValueError("factorial is undefined for negative numbers")
    if number in (0, 1):  # Base case.
        return 1
    return number * factorial(number - 1)  # Recursive case.


def fibonacci(number):
    """Return the nth Fibonacci number using direct recursion."""
    if number < 0:
        raise ValueError("Fibonacci index cannot be negative")
    if number in (0, 1):  # Base cases.
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


print("5! =", factorial(5))
print("Fibonacci sequence:", [fibonacci(index) for index in range(8)])

# Recursion can process nested structures by reducing each branch.
def sum_nested(values):
    """Sum integers in a list that may contain nested lists."""
    total = 0
    for value in values:
        if isinstance(value, list):
            total += sum_nested(value)
        else:
            total += value
    return total


print("Nested sum:", sum_nested([1, [2, [3]], 4]))

# Edge cases: base values return immediately; invalid input raises clearly.
print("0! =", factorial(0))
try:
    fibonacci(-1)
except ValueError as error:
    print("Recursion input error:", error)

# Very deep recursion can raise RecursionError; prefer iteration for scale.
