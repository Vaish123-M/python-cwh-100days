"""
# Day 29: Docstrings

A docstring is a string literal placed immediately inside a module, class,
or function definition.  Python stores it in the object's `__doc__`
attribute.  Docstrings describe what code does, its arguments, return value,
and important exceptions; comments are better for implementation notes.

Triple-quoted strings are common because they can span lines.  A docstring
must be the first statement in the definition to be recognized as one.
"""

"""This module docstring is available through __doc__."""


def convert_minutes(minutes):
    """Convert non-negative minutes to whole hours and remaining minutes.

    Args:
        minutes: A non-negative integer number of minutes.

    Returns:
        A tuple containing (hours, remaining_minutes).

    Raises:
        ValueError: If minutes is negative.
    """
    if minutes < 0:
        raise ValueError("minutes cannot be negative")
    return divmod(minutes, 60)


class Course:
    """Represent a course with a title and lesson count."""

    def __init__(self, title, lessons):
        """Store the course metadata."""
        self.title = title
        self.lessons = lessons


print("Function documentation:\n", convert_minutes.__doc__)
print("Class documentation:", Course.__doc__)
course = Course("Python", 30)
print(course.title, course.lessons)
print("Conversion:", convert_minutes(125))

# Edge case: malformed input is rejected by the function's documented rule.
try:
    convert_minutes(-5)
except ValueError as error:
    print("Docstring-described error:", error)
