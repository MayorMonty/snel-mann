# Generates a random 18k character array into a new file in the data folder

import random

""" Generates a single acceptable random character (ASCII range) """
def random_char(lower, upper):
    return chr(random.randint(lower, upper))

# Generates random file path
file_path = "".join([ random_char(97, 122) for x in range(18) ]) + ".txt"
print("Generating {}...".format(file_path))

file = open("data/" + file_path, "w+")

# Generates each character into an in string memorys
contents = ""
for i in range(18 * 1000):
    contents += random_char(32, 126)

# Write file
file.write(contents)

print("Done")