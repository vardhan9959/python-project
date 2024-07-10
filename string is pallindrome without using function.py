def is_palindrome(s):
  str1 = ''.join(s.split()).lower()
  length = len(str1)
  for i in range(length // 2):
    if str1[i] != str1[length - 1 - i]:
        return False
  return True
user_input = input("Enter a string: ")
if is_palindrome(user_input):
  print("Yes, it's a palindrome!")
else:
  print("No, it's not a palindrome.")