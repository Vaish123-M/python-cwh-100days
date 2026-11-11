"""
# Day 45: if __name__ == "__main__"

Every Python file has a built-in `__name__` variable.  When the file is run
directly, Python sets it to `"__main__"`.  When the file is imported, Python
sets it to the module's import name instead.

The main guard:

    if __name__ == "__main__":
        main()

keeps executable demonstration or application code from running during an
import.  Definitions above the guard remain available to other modules.
"""


def calculate_total(prices):
    """Return the sum of a sequence of prices."""
    return sum(prices)


def main():
    """Run this file's demonstration when it is executed directly."""
    prices = [12.50, 7.25, 3.00]
    total = calculate_total(prices)
    print("Prices:", prices)
    print("Total:", total)


# This call runs only for `python day45_main_guard.py`; importing this module
# exposes `calculate_total` and `main` without printing anything.
if __name__ == "__main__":
    main()
