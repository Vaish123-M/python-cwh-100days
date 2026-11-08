"""
# Day 37: Finally

The `finally` block runs whether the `try` block succeeds, raises an
exception, or an `except` block handles it.  Use it for cleanup that must
always happen, such as closing a resource or resetting program state.
"""

def read_first_line(lines):
    """Read from a list-like resource and always close it."""
    resource = iter(lines)
    try:
        return next(resource)
    except StopIteration:
        print("The resource is empty.")
        return None
    finally:
        print("Resource cleanup completed.")


print("First line:", read_first_line(["first", "second"]))
print("First line:", read_first_line([]))

# Cleanup also runs when an exception is handled.
is_connected = True
try:
    if is_connected:
        raise ConnectionError("server unavailable")
except ConnectionError as error:
    print("Connection error:", error)
finally:
    is_connected = False
    print("Connection reset:", is_connected)

# A function can return from try, but finally still executes first.
def status():
    try:
        return "success"
    finally:
        print("Status cleanup runs before returning.")


print("Status:", status())
