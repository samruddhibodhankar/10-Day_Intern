# Student Management System

import json
from pathlib import Path

file_path = Path(__file__).parent / "students.json"

def load_students():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Could not read the JSON file.")
        return []

def save_students(students):
    with open(file_path, "w") as file:
        json.dump(students, file, indent=4)

def add_student(students):
    print("\nAdd Student")

    try:
        student_id = int(input("Enter ID: "))

        for student in students:
            if student["id"] == student_id:
                print("This ID already exists.")
                return

        name = input("Enter name: ").strip()
        age = int(input("Enter age: "))
        city = input("Enter city: ").strip()
        course = input("Enter course: ").strip()
        marks = float(input("Enter marks: "))

        if not name or not city or not course:
            print("Name, city and course cannot be empty.")
            return

        if age < 5 or age > 100:
            print("Enter a valid age.")
            return

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "city": city,
            "course": course,
            "marks": marks
        }

        students.append(student)
        save_students(students)

        print("Student added successfully.")

    except ValueError:
        print("Please enter valid values.")


def update_student(students):
    print("\nUpdate Student")

    try:
        student_id = int(input("Enter ID to update: "))

        for student in students:
            if student["id"] == student_id:

                student["name"] = input("Enter new name: ").strip()
                student["age"] = int(input("Enter new age: "))
                student["city"] = input("Enter new city: ").strip()
                student["course"] = input("Enter new course: ").strip()
                student["marks"] = float(input("Enter new marks: "))

                if not student["name"] or not student["city"] or not student["course"]:
                    print("Fields cannot be empty.")
                    return

                if student["age"] < 5 or student["age"] > 100:
                    print("Enter a valid age.")
                    return

                if student["marks"] < 0 or student["marks"] > 100:
                    print("Marks should be between 0 and 100.")
                    return

                save_students(students)

                print("Student updated successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter valid values.")


def delete_student(students):
    print("\nDelete Student")

    try:
        student_id = int(input("Enter ID to delete: "))

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                save_students(students)

                print("Student deleted successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid ID.")


def search_student(students):
    print("\nSearch Student")

    search = input("Enter ID or name: ").strip().lower()

    found = False

    for student in students:
        if (
            str(student["id"]) == search
            or student["name"].lower() == search
        ):
            print(student)
            found = True

    if not found:
        print("Student not found.")


def filter_students(students):
    print("\nFilter Students")
    print("1. By course")
    print("2. By city")
    print("3. By minimum marks")

    choice = input("Enter choice: ")

    if choice == "1":
        course = input("Enter course: ").strip().lower()

        result = [
            student for student in students
            if student["course"].lower() == course
        ]

    elif choice == "2":
        city = input("Enter city: ").strip().lower()

        result = [
            student for student in students
            if student["city"].lower() == city
        ]

    elif choice == "3":
        try:
            marks = float(input("Enter minimum marks: "))

            result = [
                student for student in students
                if student["marks"] >= marks
            ]

        except ValueError:
            print("Please enter a valid number.")
            return

    else:
        print("Invalid choice.")
        return

    if result:
        for student in result:
            print(student)
    else:
        print("No students found.")


def sort_students(students):
    print("\nSort Students")
    print("1. By name")
    print("2. By marks")
    print("3. By age")

    choice = input("Enter choice: ")

    if choice == "1":
        result = sorted(
            students,
            key=lambda student: student["name"].lower()
        )

    elif choice == "2":
        result = sorted(
            students,
            key=lambda student: student["marks"],
            reverse=True
        )

    elif choice == "3":
        result = sorted(
            students,
            key=lambda student: student["age"]
        )

    else:
        print("Invalid choice.")
        return

    for student in result:
        print(student)


def show_statistics(students):
    print("\nStatistics")

    if not students:
        print("No student data available.")
        return

    marks = [student["marks"] for student in students]

    total = len(students)
    average = sum(marks) / total
    highest = max(marks)
    lowest = min(marks)

    passed = len([
        student for student in students
        if student["marks"] >= 40
    ])

    failed = total - passed

    print("Total students:", total)
    print("Average marks:", round(average, 2))
    print("Highest marks:", highest)
    print("Lowest marks:", lowest)
    print("Passed:", passed)
    print("Failed:", failed)

    print("\nCourse-wise statistics:")

    courses = {}

    for student in students:
        course = student["course"]

        if course not in courses:
            courses[course] = []

        courses[course].append(student["marks"])

    for course in courses:
        course_marks = courses[course]
        course_average = sum(course_marks) / len(course_marks)

        print(
            course,
            "- Students:", len(course_marks),
            "Average:", round(course_average, 2)
        )

def display_students(students):
    print("\nAll Students")

    if not students:
        print("No students available.")
        return

    for student in students:
        print(student)

def main():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Filter Students")
        print("6. Sort Students")
        print("7. Statistics")
        print("8. Display All Students")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            update_student(students)

        elif choice == "3":
            delete_student(students)

        elif choice == "4":
            search_student(students)

        elif choice == "5":
            filter_students(students)

        elif choice == "6":
            sort_students(students)

        elif choice == "7":
            show_statistics(students)

        elif choice == "8":
            display_students(students)

        elif choice == "9":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Please select 1-9.")

if __name__ == "__main__":
    main()