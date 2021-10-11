import requests

URL = 'https://unrealsoft.bg'


r = requests.get(URL)

encode = r.encoding

# Write to file
# with open('fromsite.txt', 'w', encoding='ISO-8859-1') as f:
#     f.write(r.text)

h = requests.head(URL)

print(h.headers)