import socket

f1=open("data.jpg",'wb')

c=socket.socket()

c.connect(('localhost',2000))

f1.write(c.recv(10240))
