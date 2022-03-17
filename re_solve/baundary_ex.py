import re
s = 'CPython is the implementation of Python in C'

# matches = re.finditer('Python', s)
matches = re.finditer(r'\bPython\b', s)

[print(match) for match in matches]