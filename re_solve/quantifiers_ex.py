import re

s = """CPython, IronPython, and JPython 
       are major Python's implementation"""


matches = re.finditer('\w*Python', s)

[print(m) for m in matches]