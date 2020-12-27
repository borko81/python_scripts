import urllib.request
from bs4 import BeautifulSoup as bs
import time


t0 = time.time()

req = urllib.request.urlopen('https://unrealsoft.net')
t1 = time.time()
soup = bs(req.read(), "html.parser")
for l in soup.find_all('a'):
    print(l.get('href'))
print("Total time is %f" % (t1 - t0))
