#QUEUE
# Create an empty queue
queue = []

# Take numbers from the user
numbers = input("Enter numbers separated by spaces: ").split()

# Add each number to the queue
for number in numbers:
    queue.append(number)

# Display the queue
print("Queue:", queue)

# Remove the first element from the queue
removed = queue.pop(0)

# Display the removed element
print("Removed element:", removed)

# Display the queue after removal
print("Queue after removal:", queue)