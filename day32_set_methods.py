"""
# Day 32: Set Methods

Set operations compare collections without relying on their order.
`union()` combines values, `intersection()` keeps shared values, and
`symmetric_difference()` keeps values found in exactly one set.
"""

python_students = {"Mina", "Asha", "Leo"}
math_students = {"Asha", "Leo", "Noah"}

print("All students:", python_students.union(math_students))
print("Students in both classes:", python_students.intersection(math_students))
print(
    "Only in one class:",
    python_students.symmetric_difference(math_students),
)

# update() adds values from another iterable in place.
attendees = {"Mina"}
attendees.update(["Asha", "Leo"])
print("Updated attendees:", attendees)

# add() inserts one value; remove() raises KeyError when it is absent.
attendees.add("Noah")
attendees.remove("Leo")
print("After add and remove:", attendees)

print("Classes are disjoint:", {"Art"}.isdisjoint(math_students))
print("Python class is a subset:", {"Mina"}.issubset(python_students))

# discard() is a safe alternative when absence is expected.
attendees.discard("Unknown")
print("After discarding an absent value:", attendees)
