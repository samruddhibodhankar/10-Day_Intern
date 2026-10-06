# Find the largest and second-largest numbers from the input

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = numbers[0]
second_largest = numbers[1]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("Largest:", largest)
print("Second largest:", second_largest)