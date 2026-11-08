"""
# Day 16: Match-Case Statements

Structural pattern matching uses `match` and one or more `case` clauses.
It was introduced in Python 3.10.  It can replace long equality-based
`if`/`elif` chains and can also inspect the structure of sequences or
dictionaries.  `_` is a wildcard fallback.

Unlike `if`, `match` compares a subject against patterns.  The optional
`case pattern if guard` adds an extra Boolean condition.
"""

command = input("Enter a command (start/stop/restart): ").strip().lower()
match command:
    case "start":
        print("Starting the service.")
    case "stop":
        print("Stopping the service.")
    case "restart":
        print("Restarting the service.")
    case _:
        print("Unknown command.")

# Multiple alternatives can share one case with `|`.
status_code = int(input("Enter an HTTP status code: "))
match status_code:
    case 200 | 201:
        print("Successful response.")
    case 404:
        print("Resource not found.")
    case code if 400 <= code < 500:
        print("Other client error:", status_code)
    case _:
        print("Other response.")

# Patterns can unpack a sequence and bind names.
point = tuple(map(int, input("Enter x and y coordinates separated by a space: ").split()))
match point:
    case (0, y):
        print("Point lies on the y-axis at", y)
    case (x, 0):
        print("Point lies on the x-axis at", x)
    case (x, y):
        print("Point:", x, y)

# The wildcard handles edge cases not listed explicitly.
for value in ("pause", "start"):
    match value:
        case "start":
            print(value, "recognized")
        case _:
            print(value, "not recognized")
