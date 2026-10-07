# Conditions and Loops 

students = [
    {"name": "Aarav", "marks": 85},
    {"name": "Priya", "marks": 72},
    {"name": "Rahul", "marks": 58},
    {"name": "Sneha", "marks": 91},
    {"name": "Vikram", "marks": 45}
]

# Conditions
print("Student Results:")
for student in students:
    marks = student["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if marks >= 40 else "Fail"

    print(
        student["name"],
        "- Marks:", marks,
        "- Grade:", grade,
        "- Status:", status
    )

# Find students who scored 75 or more
print("\nStudents scoring 75 or more:")

for student in students:
    if student["marks"] >= 75:
        print(student["name"])

# Calculate total and average
total = 0

for student in students:
    total += student["marks"]

average = total / len(students)

print("\nTotal Marks:", total)
print("Average Marks:", average)