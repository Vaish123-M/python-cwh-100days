"""
# Day 44: How import works in Python

When Python sees an import statement, it searches the locations in
`sys.path`, loads the requested module, and binds a name for that module in
the current namespace.  A module is normally executed once per interpreter
and then cached in `sys.modules`.

The examples below show importing a complete module, importing selected
names, using an alias, and inspecting the search path.  Prefer explicit
imports and avoid wildcard imports because they make a module's public names
unclear.
"""


import math
import sys
from math import ceil, sqrt


# Importing the module keeps the namespace clear: use the `math.` prefix.
print("Pi:", math.pi)
print("Sine of pi/2:", math.sin(math.pi / 2))

# Selected names can be used directly when they are needed frequently.
print("Square root:", sqrt(81))
print("Rounded up:", ceil(2.1))

# An alias gives a long or frequently used module a shorter local name.
import datetime as dt

today = dt.date.today()
print("Today:", today)

# `sys.path` contains the directories Python searches for imports.  The
# current project directory is normally included when running a script here.
print("First import locations:")
for path in sys.path[:3]:
    print(" -", path)

# Python caches loaded modules, so a later import reuses the same module
# object instead of executing its top-level code again.
print("math is cached:", "math" in sys.modules)
