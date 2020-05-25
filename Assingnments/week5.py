import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl





# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




url="http://py4e-data.dr-chuck.net/comments_550959.xml"
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)
sum=0
results = tree.findall('comments/comment')
for items in results:
    x=int(items.find("count").text)
    sum=sum+x

print(sum)
