## File Handling

file_name = "student.txt"

# Write data to the file
with open(file_name, "w") as file:
    file.write("Name: Samruddhi\n")
    file.write("Marks: 85\n")
    file.write("Status: Pass\n")

# Read data from the file
with open(file_name, "r") as file:
    content = file.read()

print("Student Details:")
print(content)