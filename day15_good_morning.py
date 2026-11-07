"""
# Day 15: Exercise 2 - Good Morning Sir

Build a greeting program that reads the local system time and wishes the
user according to the hour.  The `time` module's `localtime()` returns a
struct-like value whose `tm_hour` is an integer from 0 through 23.

This example keeps the greeting logic in a function so it can be tested with
known hours.  The final call uses the actual local system clock.
"""

import time


def greeting_for_hour(hour):
    """Return a greeting for a valid 24-hour clock hour."""
    if not 0 <= hour <= 23:
        raise ValueError("hour must be between 0 and 23")
    if hour < 12:
        return "Good morning!"
    if hour < 18:
        return "Good afternoon!"
    return "Good evening!"


# Use fixed examples first so each branch is visible and predictable.
for example_hour in (8, 14, 20):
    print(example_hour, "->", greeting_for_hour(example_hour))

# `localtime()` uses the machine's local timezone.
current_hour = time.localtime().tm_hour
print("Current local greeting:", greeting_for_hour(current_hour))

# Edge case: invalid hours are rejected rather than silently misclassified.
try:
    greeting_for_hour(24)
except ValueError as error:
    print("Time validation:", error)
