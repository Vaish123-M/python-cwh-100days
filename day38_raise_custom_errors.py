"""
# Day 38: Raising Custom Errors

Use `raise` when a program detects invalid data.  A custom exception class
can describe a domain-specific failure while remaining catchable like other
Python exceptions.
"""

class InsufficientBalanceError(ValueError):
    """Raised when a withdrawal exceeds the available balance."""


def withdraw(balance, amount):
    """Return the balance after a valid withdrawal."""
    if amount <= 0:
        raise ValueError("withdrawal amount must be positive")
    if amount > balance:
        raise InsufficientBalanceError(
            f"cannot withdraw {amount}; balance is {balance}"
        )
    return balance - amount


balance = float(input("Enter the account balance: "))
amount = float(input("Enter the withdrawal amount: "))
try:
    print("Remaining balance:", withdraw(balance, amount))
except InsufficientBalanceError as error:
    print("Withdrawal declined:", error)
except ValueError as error:
    print("Invalid withdrawal:", error)

# Re-raise an exception when the caller should decide how to handle it.
def require_non_empty(text):
    """Return text after enforcing a non-empty string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text.strip():
        raise ValueError("text must not be empty")
    return text


print("Validated text:", require_non_empty(input("Enter non-empty text: ")))
