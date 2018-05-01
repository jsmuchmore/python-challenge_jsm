file = open("resources\paragraph_1.txt")

import re

words = re.split(" ", file)

print(words)

