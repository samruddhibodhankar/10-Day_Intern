# Lambda Functions

students = [
    {"name": "Aarav", "marks": 85},
    {"name": "Priya", "marks": 72},
    {"name": "Rahul", "marks": 91},
    {"name": "Sneha", "marks": 64}
]

# Sort students by marks
sorted_students = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True
)

print("Students sorted by marks:")

for student in sorted_students:
    print(student["name"], "-", student["marks"])