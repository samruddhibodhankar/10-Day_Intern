# Exception Handling

try:
    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

except ValueError as error:
    print("Invalid input:", error)

else:
    print("Valid marks:", marks)

finally:
    print("Marks validation completed.")