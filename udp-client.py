#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for msg in "twenty tiny tigers".split():
	sock.sendto(msg.encode(), ('localhost', 2000))
