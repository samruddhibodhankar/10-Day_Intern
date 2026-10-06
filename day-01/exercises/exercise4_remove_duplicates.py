# Function to remove duplicate numbers
def remove_duplicates(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers

numbers = list(map(int, input("Enter numbers: ").split()))

result = remove_duplicates(numbers)

print("After removing duplicates:", result)