# Removing items
student = {"name": "John", "age": 20, "grade": "A"}
student.pop("grade")       # Remove specific key
del student["age"]         # Delete key
print("After removal:", student)