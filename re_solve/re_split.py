import re
import os
from fnmatch import fnmatch

line = 'str1, str2  str3: str4'

# one
print(re.split(r'[,:\s]\s*', line))

# two
print(re.split(r'(?:,|:|\s)\s*', line))


for root, dirname, filename in os.walk(os.path.join(os.getcwd(), 're_solve')):
    [print(os.path.join(root, file)) for file in filename if fnmatch(file, '*.py')]
        
