"""
This is a random password generator that gives you a secure password of a specified length.
---25-12-2025
"""

import random
import string

pass_len=int(input("Enter the length of the password: "))
characters=string.ascii_letters + string.digits + string.punctuation

password=''
for _ in range(pass_len):
    password+=random.choice(characters)

print("Your Random Password is:", password)


