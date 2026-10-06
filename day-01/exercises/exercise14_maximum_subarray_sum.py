# Find the maximum subarray sum
# Take numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Start with the first number
current_sum = numbers[0]
maximum_sum = numbers[0]

# Find the maximum subarray sum
for number in numbers[1:]:
    current_sum = max(number, current_sum + number)
    maximum_sum = max(maximum_sum, current_sum)

# Display the result
print("Maximum subarray sum:", maximum_sum)