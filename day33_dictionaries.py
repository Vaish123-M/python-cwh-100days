"""
# Day 33: Dictionaries

A dictionary stores key-value pairs.  Keys must be unique and hashable, and
values can be any type.  Access with `[]` raises KeyError for a missing key;
`get()` can return a default value instead.
"""

student = {
    "name": "Mina",
    "age": 20,
    "course": "Python",
}

print("Student:", student)
print("Name:", student["name"])
print("Course:", student.get("course"))
print("Email:", student.get("email", "not provided"))

# Keys and values provide views that can be iterated over.
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

for key, value in student.items():
    print(key, "=", value)

# A dictionary can contain nested dictionaries and lists.
profile = {
    "name": "Asha",
    "skills": ["Python", "SQL"],
    "contact": {"city": "Delhi"},
}
print("First skill:", profile["skills"][0])
print("City:", profile["contact"]["city"])

# Keys must be unique; a later assignment replaces the earlier value.
student["age"] = 21
print("Updated age:", student["age"])

# print(student["email"])  # KeyError: email
