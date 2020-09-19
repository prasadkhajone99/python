import socket

f=open("abc.jpg",'rb')

#l=f.read(12500)

fd=socket.socket()
print("socket created")

fd.bind(('192.168.0.113',2000))

fd.listen(5)
print("waiting for connection")

c,addr=fd.accept()
print("connected with ",addr)

c.send(abc.jpg)

c.close()



