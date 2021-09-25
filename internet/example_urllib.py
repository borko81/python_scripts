from urllib.parse import urlparse, urlsplit, urljoin

url = 'http://netloc/path;param?query=arg#frag'

u = urlparse((url))
print(u)
[print(i) for i in u]

print(urlsplit(url))
print(urljoin(url, '/test/index.html'))