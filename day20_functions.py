"""
# Day 20: Functions

A function is a reusable block defined with `def`.  Its header contains the
name and parameters, followed by an indented body.  Call it with parentheses.
`return` sends a result to the caller; reaching the end without `return`
returns `None`.

Parameters receive arguments.  Defaults make arguments optional, and keyword
arguments make calls clearer.  Keep functions focused on one task and avoid
mutable default values such as `items=[]`.
"""


def greet(name):
    """Return a friendly greeting for one name."""
    return f"Hello, {name}!"


def rectangle_area(width, height=1):
    """Return the area using a required width and optional height."""
    if width < 0 or height < 0:
        raise ValueError("dimensions cannot be negative")
    return width * height


def add_all(*numbers):
    """Return the sum of any number of positional arguments."""
    return sum(numbers)


print(greet("Mina"))
print("Square area:", rectangle_area(5))
print("Rectangle area:", rectangle_area(width=4, height=3))
print("Sum:", add_all(1, 2, 3, 4))

# A function without an explicit return produces None.
def show_message(message):
    print(message)


result = show_message("Printed inside the function")
print("Returned value:", result)

# Edge case: raise a clear error for invalid arguments and handle it at the
# call site instead of silently returning a misleading result.
try:
    rectangle_area(-2, 3)
except ValueError as error:
    print("Function error:", error)

# Do not use a mutable list as a default; create it inside the function.
def add_item(item, items=None):
    """Return a new list containing item, without shared default state."""
    if items is None:
        items = []
    return [*items, item]


print(add_item("pen"))
print(add_item("book"))
