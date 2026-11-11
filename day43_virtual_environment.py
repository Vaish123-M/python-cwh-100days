"""
# Day 43: Virtual environments in Python

A virtual environment is an isolated directory containing a Python
interpreter and project-specific packages.  It prevents dependencies for one
project from affecting another project or the system installation.

Typical Windows commands from the project directory are:

    python -m venv .venv
    .venv\\Scripts\\Activate.ps1
    python -m pip install package-name
    python -m pip freeze > requirements.txt
    deactivate

Use `python -m pip` so that pip belongs to the interpreter in the active
environment.  The `.venv` directory is normally excluded from version
control; share a requirements file instead of committing the environment.
"""


import os
import sys


# `sys.prefix` identifies the active Python environment.
print("Python executable:", sys.executable)
print("Environment prefix:", sys.prefix)

# In a venv, `sys.base_prefix` points to the Python installation from which
# the environment was created.  Different prefixes indicate a virtual env.
is_virtual_environment = sys.prefix != sys.base_prefix
print("Running in a virtual environment:", is_virtual_environment)

# Environment variables can be read without changing the environment.
print("Current working directory:", os.getcwd())

# Installing packages is intentionally done from the terminal, not from a
# script, so dependency changes remain explicit and reproducible.
