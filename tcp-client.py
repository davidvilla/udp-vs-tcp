#!/usr/bin/env python3

import socket

sock = socket.socket()
sock.connect(('localhost', 2000))

for msg in "twenty tiny tigers".split():
	sock.send(msg.encode())
