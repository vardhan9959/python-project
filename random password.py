import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password_length = 4
random_password = generate_password(password_length)
print("Generated Password:", random_password)

# import random
# import string
# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.jion(random.choice(characters) for _ in range(length))
#     return password
# password_length = 4
# random_password = generate_password(password_length)
# print("Generated password:", random_password)
