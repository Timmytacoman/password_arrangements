import string
import random

CHARS = string.printable[:-6]
LENGTH = input("Enter password length: ")
password = ""
for i in range(int(LENGTH)):
    password += CHARS[random.randint(0, len(CHARS) - 1)]
print(password)
