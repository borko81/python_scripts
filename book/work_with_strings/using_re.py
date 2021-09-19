import re

line = 'str1 str2; str3, str4  str5, str6'

result = re.split(r'[;,\s]\s*', line)

print(result)

text1 = '07/27/2017'
text2 = 'Today is 07/27/2017 next day is a 07/27/2017'

pattern = re.compile(r'\d+/\d+/\d+')
pattern_two = re.compile(r'\b(\d+)/(\d+)/(\d+)\b')


def search_in_text(text):
    data = pattern_two.findall(text2)
    if data:
        result = ''
        for line in data:
            result += f'{line[1]}.{line[0]}.{line[2]} '
        return result.strip()
    return "Not found"


print(pattern.match(text1).group(0))

print(search_in_text(text2))

# serach and replace
print(pattern_two.sub(r'\2.\1.\3', text1))