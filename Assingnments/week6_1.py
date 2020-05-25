import json
import urllib.request, urllib.parse, urllib.error
import ssl
# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_550960.json"
data = urllib.request.urlopen(url, context=ctx).read()


info = json.loads(data)
sum=0
for item in info["comments"]:
    sum=sum+item["count"]
print(sum)
