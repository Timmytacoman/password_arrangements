import string
import itertools

LENGTH = 2
CHARS = string.printable[:-6]
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
