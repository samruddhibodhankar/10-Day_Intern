# 05_functions.py
# Functions

def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(average):
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    return "F"


marks = [85, 72, 91]

average = calculate_average(marks)
grade = get_grade(average)

print("Marks:", marks)
print("Average:", round(average, 2))
print("Grade:", grade)