import random

chars = ‘abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=+!@#$%^&*<>/~-:;?’
password = ”
number = input(“How many characters do you need: “)
int1 = int(number)

for c in range(int1):
password += random.choice(chars)
print(password)