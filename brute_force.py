import string
import itertools
import time

START_TIME = time.time()
LENGTH = 3
CHARS = string.printable[:-6]
print(f"CHARS: {CHARS}")
print(f"CHARS length: {len(CHARS)}")

counter = 0
file = open("arrangements.txt", "w")

arrangements = list(map(''.join, itertools.product(CHARS, repeat=LENGTH)))
for i in arrangements:
    file.write(i + "\n")
    print(i)
    counter += 1
file.close()
print(len(arrangements))
END_TIME = time.time()
print(f"Elapsed time: {END_TIME - START_TIME}")
