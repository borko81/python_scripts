import re
from fnmatch import fnmatch

pattern = re.compile(r'[,;\s]\s*')

line = 'asdf fjdk; afed, fjek,asdf, foo'
filename = 'https://google.bg'
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
lower_and_upper = 'UPPER PYTHON, lower python, Mixed Python'

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

result = pattern.split(line)

pattern_for_int = re.compile(r'\d+/\d+/\d+')

print(filename.startswith(('http', 'https')))
print(filename[-3:])
print(fnmatch(filename, 'https*'))
print([name for name in names if fnmatch(name, 'Dat*')])
print([a for a in addresses if fnmatch(a, '5[0-9][0-9][0-9]*ST')])
founded_date = pattern_for_int.findall(text)

for f in founded_date:
    print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\2.\1.\3', f))

print(re.findall('python', lower_and_upper, re.I))