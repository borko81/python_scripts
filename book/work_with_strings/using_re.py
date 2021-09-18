import re

line = 'str1 str2; str3, str4  str5, str6'

result = re.split(r'[;,\s]\s*', line)

print(result)