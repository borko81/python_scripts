import re
time = '12:20'

# matches = re.finditer('\d\d', time)
# matches = re.finditer('^\d\d', time)
# matches = re.finditer('(\d\d)$', time)
matches = re.finditer('(?P<first>^\d{2}):(?P<last>\d{2})$', time)

for match in matches:
    result = match.group()
    print("_".join(match.groups()))
    
print(re.sub(':', '-', time))