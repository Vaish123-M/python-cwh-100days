"""
# Day 21: Function Arguments

Arguments are values passed to a function's parameters.  Required parameters
must be supplied, while default parameters provide a fallback value.
Keyword arguments use `name=value` and make calls self-documenting.

`*args` collects extra positional arguments into a tuple, and `**kwargs`
collects extra keyword arguments into a dictionary.  Parameters with
defaults must come after required parameters.
"""


def describe_person(name, age=18, *, city="Unknown"):
    """Use a required argument, defaults, and a keyword-only argument."""
    return f"{name} is {age} years old and lives in {city}."


def total_cost(*prices, tax_rate=0):
    """Accept any number of prices and an optional keyword-only tax rate."""
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)


def show_settings(**settings):
    """Accept arbitrary named settings as a dictionary."""
    for key, value in settings.items():
        print(f"{key} = {value}")


print(describe_person("Asha"))
print(describe_person("Ravi", age=25, city="Delhi"))
print("Total:", total_cost(10, 5, tax_rate=0.1))
show_settings(theme="dark", notifications=True)

# A list or tuple can be unpacked into positional arguments with *.
prices = [3, 7, 2]
print("Unpacked total:", total_cost(*prices))

# A dictionary can be unpacked into keyword arguments with **.
profile = {"name": "Leela", "age": 30, "city": "Pune"}
print(describe_person(**profile))

# Edge cases: missing required arguments and unexpected keywords are errors.
# describe_person()  # TypeError: required name is missing.
# describe_person("A", country="IN")  # TypeError: unexpected keyword.
