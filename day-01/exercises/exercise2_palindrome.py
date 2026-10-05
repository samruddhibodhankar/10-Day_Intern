def check_palindrome(text):
    return text == text[::-1]


user_input = input("Enter a string: ")

if check_palindrome(user_input):
    print("Palindrome")
else:
    print("Not a palindrome")