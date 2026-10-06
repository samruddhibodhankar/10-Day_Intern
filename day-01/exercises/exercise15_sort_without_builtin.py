#Sorting without built-in sorting  
# Take numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Sort the numbers using Bubble Sort
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap the numbers
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Display the sorted numbers
print("Sorted numbers:", numbers)