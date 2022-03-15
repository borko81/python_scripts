import re
s = 'Python 3.0 was released in 2020'
# matches = re.finditer('\d+', s)
# matches = re.finditer('\d\d\d\d', s)
# matches = re.finditer('\d{2}', s)
matches = re.finditer('\D+', s)

for match in matches:
    print(match.group().strip())
    
    
phone_no = re.sub('\D', '', '+359-(088)-772-333-111')
print('+' + phone_no[:3] + ' ' + phone_no[3:])