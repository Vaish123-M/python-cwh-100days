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


try:
    hour = int(input("Enter the current hour (0-23): ").strip())
    print(greeting_for_hour(hour))
except ValueError as error:
    print("Please enter a whole number from 0 to 23:", error)
