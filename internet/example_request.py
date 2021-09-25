from urllib import request, parse
from urllib.parse import urljoin

url = 'https://www.google.bg/search'

query_args = {'q': 'car', 'color': 'white'}

response = request.urlopen(url)
header = response.info()
print(response.geturl())
print(header)


encoded_args = parse.urlencode(query_args)

new_url = '?'.join([url, encoded_args])
print(new_url)