# Find common elements
# Take the first array from the user
array1 = list(map(int, input("Enter first array: ").split()))

# Take the second array from the user
array2 = list(map(int, input("Enter second array: ").split()))

# Find common elements
common_elements = []

for number in array1:
    if number in array2 and number not in common_elements:
        common_elements.append(number)

# Display the result
print("Common elements:", common_elements)