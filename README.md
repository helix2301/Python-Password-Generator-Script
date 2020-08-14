# Python-Password-Generator-Script
Python Password Generator Script
We all want to make the best and most secure passwords we can but sometimes you just need a strong password that’s really hard for a service account or an account we don’t use a lot.

The code is only a few lines. When the script is run it asks you how many characters you want the password. After you give it a number it spits out a random password that amount of characters.

import random

chars = ‘abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=+!@#$%^&*<>/~-:;?’
password = ”
number = input(“How many characters do you need: “)
int1 = int(number)

for c in range(int1):
password += random.choice(chars)
print(password)
