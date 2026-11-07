"""
# Day 26: Exercise 2 Solution - Good Morning Sir

This solution revisits the greeting exercise with a reusable function.
`time.localtime().tm_hour` supplies the current local hour from 0 to 23.
Keeping the decision logic separate from the clock makes every branch easy
to test and keeps the program's behavior clear.
"""

import time


def get_greeting(hour):
    """Return a time-of-day greeting for an hour on a 24-hour clock."""
    if not 0 <= hour <= 23:
        raise ValueError("hour must be between 0 and 23")
    if hour < 12:
        return "Good morning, sir!"
    if hour < 18:
        return "Good afternoon, sir!"
    return "Good evening, sir!"


# Test every decision branch with fixed values.
for hour in (7, 13, 19):
    print(f"{hour:02d}:00 -> {get_greeting(hour)}")

# Use the actual local system timestamp for the live greeting.
now = time.localtime()
print("Live greeting:", get_greeting(now.tm_hour))

# Invalid timestamps are reported explicitly.
try:
    get_greeting(-1)
except ValueError as error:
    print("Invalid hour:", error)
