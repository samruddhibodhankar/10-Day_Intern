# Display the character frequency
text = input("Enter a string: ")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print("Character frequency:", frequency)