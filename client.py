#client

import socket

HOST = 'localhost'
PORT = 50000
MSG = b""

MSG = input("Nachricht: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(bytes(MSG, 'utf-8'))
s.close()
-
