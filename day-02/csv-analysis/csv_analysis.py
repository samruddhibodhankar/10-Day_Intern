# CSV Analysis

import csv

file_name = "students.csv"

students = []

with open(file_name, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

print("Total Records:", len(students))

# Missing values

print("\nMissing Values:")

missing_values = {}

for column in students[0]:
    count = 0

    for student in students:
        if student[column].strip() == "":
            count += 1

    missing_values[column] = count
    print(column, ":", count)

# Duplicate student details

print("\nDuplicate Records:")

seen = set()
duplicates = 0

for student in students:
    record = (
        student["name"],
        student["course"],
        student["city"],
        student["marks"]
    )

    if record in seen:
        duplicates += 1
    else:
        seen.add(record)

print("Duplicates:", duplicates)

# Marks statistics

marks = []

for student in students:
    if student["marks"].strip() != "":
        marks.append(float(student["marks"]))

print("\nMarks Statistics:")
print("Average:", round(sum(marks) / len(marks), 2))
print("Minimum:", min(marks))
print("Maximum:", max(marks))

# Course-wise statistics

print("\nCourse-wise Statistics:")

courses = {}

for student in students:
    course = student["course"]

    if course not in courses:
        courses[course] = []

    if student["marks"].strip() != "":
        courses[course].append(float(student["marks"]))


for course in courses:
    course_marks = courses[course]

    average = sum(course_marks) / len(course_marks)

    print(
        course,
        "- Students:", len(course_marks),
        "Average:", round(average, 2),
        "Minimum:", min(course_marks),
        "Maximum:", max(course_marks)
    )