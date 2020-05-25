import urllib.request,urllib.parse,urllib.error  #imports urllib libraries

fhand=urllib.request.urlopen("http://data.pr4e.org/intro-short.txt\r\n\r\n")
# analogous to a GET request in socket, but this encodes as well and also opens a source/stream to the information, kind of
# like a file handle, we can't get header files in here by using HTTP/1.0 as opposed to socket method
# we don't have to manually decode the message anymore

counts=dict()

for line in fhand:
    line=line.decode() # we still have to decode information from UTF-8 to UNICODE
    print(line)
    line=line.split() # returns a list of words in the line
    for word in line:
        counts[word]=counts.get(word,0)+1
ls=list()
for (k,v) in counts.items():
    ls.append((v,k))
ls.sort(reverse=True)
for ((v,k)) in ls[:10]:
    print(k,v)
