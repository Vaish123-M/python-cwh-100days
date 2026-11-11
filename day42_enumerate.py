"""
# Day 42: The enumerate() function

`enumerate()` loops over an iterable while producing both an item and its
index.  Each iteration returns a pair in the form `(index, item)`, which can
be unpacked directly in a `for` loop:

    for index, item in enumerate(items, start=0):
        ...

The optional `start` argument changes the first index.  It does not change
the iterable itself.  `enumerate()` is preferable to manually maintaining a
counter because it keeps the counter synchronized with the loop.
"""


languages = ["Python", "JavaScript", "C", "Rust"]

# The default index starts at zero, as it does for normal Python sequences.
for index, language in enumerate(languages):
    print(index, language)

# `start=1` is convenient when displaying a human-friendly numbered list.
for number, language in enumerate(languages, start=1):
    print(f"{number}. {language}")

# Enumerating a string yields one character at a time.
word = "code"
for position, character in enumerate(word, start=1):
    print(f"Character {position}: {character}")

# The index can be used to update a list when the item itself is not enough.
prices = [10, 25, 40]
for index, price in enumerate(prices):
    prices[index] = price * 2
print("Updated prices:", prices)

# Unpacking the two values makes the relationship between index and item
# explicit; no separate counter variable is required.
