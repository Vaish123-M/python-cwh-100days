"""
# Day 2: Modules

A module is a `.py` file containing reusable code.  `import` loads a module,
and dot notation accesses one of its names.  The standard library provides
modules such as `math`, `random`, and `datetime`; third-party modules must
be installed separately.

Import forms:
- `import math` keeps the namespace explicit (`math.sqrt(16)`).
- `from math import pi` imports one known name.
- Avoid `from module import *` because it hides where names came from.
"""

import math
import random
from datetime import date

# The module name before the dot makes the source of sqrt obvious.
print("Square root of 81:", math.sqrt(81))
print("Pi rounded to 3 places:", round(math.pi, 3))

# A directly imported name can be used without the module prefix.
print("Today is:", date.today())

# randint includes both endpoints.  The output is intentionally variable.
print("A number from 1 through 6:", random.randint(1, 6))

# Edge case: math.sqrt accepts non-negative numbers.  sqrt(-1) raises
# ValueError, so validate data before calling it in a real program.
number = 0
if number >= 0:
    print("Square root of", number, "is", math.sqrt(number))

# Import aliases are useful when a module name is long.
import statistics as stats
print("Mean:", stats.mean([10, 20, 30]))
