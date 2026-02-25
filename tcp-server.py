#!/usr/bin/env python3

import socket

sock = socket.socket()
sock.bind(('', 2000))
sock.listen(5)
conn, addr = sock.accept()

for i in range(3):
	print(i+1, conn.recv(1024).decode())
