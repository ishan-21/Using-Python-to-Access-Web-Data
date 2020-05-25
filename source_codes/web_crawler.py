import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup

url="https://www.youtube.com/"
info=urllib.request.urlopen(url) # notice no encoding
data=info.read()  # the data received is read in UTF-8 only, it's not decoded

x=BeautifulSoup(data,"html.parser") # extracts the page in html format

tags=x('a')  # makes a list of anchor tags in the html document
for tag in tags:
    print(tag.get("href",None)) # extracts the href attribute from each anchor tag

# as a result we get all the links available on a particular webpage

# web-crawler pretends to be a web-browser but it can extract information about the webpage unlike a browser, for example
# here it extracts all the links available on a webpage, search engines are web-crawlers for example google, and chrome,firefox
# are web-browsers
