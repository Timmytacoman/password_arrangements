import time
import string

START_TIME = time.time()
CHARS = string.printable[:-6]
LENGTH = 3

print(len(CHARS) ** LENGTH)

END_TIME = time.time()
print(f"Elapsed time: {END_TIME - START_TIME}")
