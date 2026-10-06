# Find the missing number
# Take numbers from the user
numbers = list(map(int, input("Enter numbers: ").split()))

# Find the smallest and largest numbers
smallest = min(numbers)
largest = max(numbers)

# Store missing numbers
missing_numbers = []

# Check each number in the range
for number in range(smallest, largest + 1):
    if number not in numbers:
        missing_numbers.append(number)

# Display the missing numbers
print("Missing numbers:", missing_numbers)