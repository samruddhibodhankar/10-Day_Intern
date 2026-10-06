## Function to reverse the given string
def reverse_string(text):
    return text[::-1]


user_input = input("Enter a string: ")

result = reverse_string(user_input)

print("Reversed string:", result)