def is_palindrome(number):
    # Convert the number to a string for easier comparison
    num_str = str(number)

    # Check if the reversed string is equal to the original string
    return num_str == num_str[::-1]

# Input a number
user_number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(user_number):
    print(f"{user_number} is a palindrome!")
else:
    print(f"{user_number} is not a palindrome.")