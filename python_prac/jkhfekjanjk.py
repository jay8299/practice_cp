import json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ="http://py4e-data.dr-chuck.net/comments_368204.json"

uh = urllib.request.urlopen(url, context=ctx).read()
data = uh
print(data)
print('Retrieved', len(data), 'characters')
u=json.loads(uh)
c=0
for i in u['comments']:
    c+=i['count']
print(c)