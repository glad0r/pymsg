#server

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50000))
s.listen(1)
conn, addr=s.accept()

data=conn.recv(1024)
print("verbindung von: ",addr)
print("nachricht: ",repr(data))
s.close()
