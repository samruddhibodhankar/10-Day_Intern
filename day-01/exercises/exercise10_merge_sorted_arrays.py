# Merge the arrays
# Take the first sorted array
array1 = list(map(int, input("Enter first sorted array: ").split()))

# Take the second sorted array
array2 = list(map(int, input("Enter second sorted array: ").split()))

# Merge both arrays
merged_array = array1 + array2

# Sort the merged array
merged_array.sort()

# Display the result
print("Merged sorted array:", merged_array)