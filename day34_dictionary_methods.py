"""
# Day 34: Dictionary Methods

Dictionaries can be changed in place.  `update()` adds or replaces entries,
`pop()` removes a named entry, `popitem()` removes the last inserted pair,
and `clear()` removes everything.  `del` can remove a specific key or the
whole dictionary.
"""

student = {"name": "Mina", "age": 20}

student.update({"course": "Python", "age": 21})
print("After update:", student)

removed_course = student.pop("course")
print("Removed course:", removed_course)
print("After pop:", student)

student["city"] = "Delhi"
last_item = student.popitem()
print("Last item:", last_item)
print("After popitem:", student)

# pop() can use a default when a key may not exist.
missing = student.pop("email", "not provided")
print("Missing email:", missing)

student.clear()
print("After clear:", student)

# `del` removes a key, while deleting the dictionary name makes it unusable.
account = {"username": "mina", "active": True}
del account["active"]
print("After deleting active flag:", account)

del account
# print(account)  # NameError: account is no longer defined.
