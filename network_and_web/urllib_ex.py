from urllib.request import urlopen
from pprint import pprint
import os


URL = 'https://unrealsoft.net'
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
output_file = desktop + '\web.html'

# with urlopen(URL) as response:
#     body = response.read()
    
#pprint(response.headers.items())

# print(response.headers.items())

# print(response.getheader('Server'))


response = None
try:
    response = urlopen(URL)
except Exception as ex:
    print(ex)
else:
    body = response.read()
    char = response.headers.get_content_charset()
    decoded_body = body.decode(char)
    with open(output_file, 'wb') as html_file:
        html_file.write(body)
finally:
    if response is not None:
        response.close()
        