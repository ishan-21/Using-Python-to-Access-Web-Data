import socket

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #this creates the socket
soc.connect(("data.pr4e.org",80)) #connects the socket to port 80 of server "data.pr4e.org",note connect takes a single tupple para
cm= 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #get command, notice the encoding to UTF-8 from UNICODE
soc.send(cm) #sends the instruction from client to server

while True:
    line=soc.recv(1024).decode() #receives information in bits UTF-8 and decodes to UNICODE, 1024 characters at a time
    if len(line)<1:break #this is used to exit the loop when information received=0
    print(line,end="")
soc.close()         # closes the connection

# notice in line 5 if we don't write HTTP/1.0 the program will not return any header files as output
# also note that \r\n represents EOL so \r\n\r\n represents an EOL and then a blank line
