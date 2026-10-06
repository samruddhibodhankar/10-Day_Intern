#STACK
# Create an empty stack
stack = []

# Take numbers from the user
numbers = input("Enter numbers separated by spaces: ").split()

# Push each number into the stack
for number in numbers:
    stack.append(number)

# Display the stack
print("Stack:", stack)

# Remove the top element from the stack
removed = stack.pop()

# Display the removed element
print("Popped element:", removed)

# Display the stack after popping
print("Stack after pop:", stack)