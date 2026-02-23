# Student Marks Analyzer

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


# Given list of student marks (example data)
students = {
    "Alice": [95, 85, 102, 78, -5],
    "Bob": [88, 92, 79, 85],
    "Charlie": [45, 55, 65, 75],
    "David": [100, 98, 105, 89]
}

results = {}

# Process each student
for name, marks in students.items():
    # Remove invalid marks
    valid_marks = [m for m in marks if 0 <= m <= 100]

    if len(valid_marks) == 0:
        average = 0
    else:
        average = sum(valid_marks) / len(valid_marks)

    grade = calculate_grade(average)

    results[name] = {
        "valid_marks": valid_marks,
        "average": average,
        "grade": grade
    }

# Find highest average
highest_avg = max(student["average"] for student in results.values())

# Find topper(s)
toppers = [name for name, data in results.items() if data["average"] == highest_avg]

# Display Results
print("----- Student Report -----")
for name, data in results.items():
    print(f"\nName: {name}")
    print(f"Valid Marks: {data['valid_marks']}")
    print(f"Average: {data['average']:.2f}")
    print(f"Grade: {data['grade']}")

print("\n----- Topper(s) -----")
print("Topper(s):", ", ".join(toppers))
print(f"Highest Average: {highest_avg:.2f}")