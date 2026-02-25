#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 2000))

for i in range(3):
	print(i+1, sock.recvfrom(1024)[0].decode())
