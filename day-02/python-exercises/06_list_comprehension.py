# List Comprehensions

marks = [45, 72, 88, 35, 91, 64]

passed_marks = [mark for mark in marks if mark >= 40]

updated_marks = [mark + 5 for mark in passed_marks]

print("Original Marks:", marks)
print("Passed Marks:", passed_marks)
print("Updated Marks:", updated_marks)