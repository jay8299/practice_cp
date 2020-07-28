"""
# Excel Sum
n=int(input())
k=n
g=''
while(k!=0):
    p=k%26
    if p==0:
        g +='Z'
        k = k//26 - 1
    else:
        g += str(chr(p + 64))
        k//=26
print(g[::-1])
"""
#merge the sublists with one or more common elements
"""
l=[[1,2],[1,3],[2,4],[3,5],[7,8]]
out=[]
while len(l)>0:
    first,*rest =l
    first=set(first)
    lf=-1
    while len(first)>lf:
        lf=len(first)
        rest2=[]
        for r in rest:
            if len(first.intersection(set(r)))>0:
                print('abc',first)
                first |=set(r)
                print(first)
            else:
                rest2.append(r)
        rest=rest2
    out.append(first)
    l=rest
print(out)
"""
"""
a=dict()

for i,j in enumerate(["abcd","b"]):
    a[i]=a.get(i,[0 for k in range(len(j))])
    a[i][0]+=1
print(a)

"""
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_368201.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
s=0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('comments', None))
    print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    s+=int(tag.contents[0])
print(s)

"""



# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ="http://py4e-data.dr-chuck.net/comments_368203.xml"

uh = urllib.request.urlopen(url, context=ctx).read()
data = uh
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('.//count')
s=0
for i in results:
    s+=int(i.text)
print(s)




"""
import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Florence.html"
count = 7
position = 18
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    print(s[position - 1])
    print(t[position - 1])
    url = s[position - 1]

"""














