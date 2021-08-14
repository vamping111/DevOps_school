#!/usr/bin/env python3

import socket
client       = input("Enter your domain: ")
tosend         = str.encode(client)
server   = ("127.0.0.1", 2204)
bufferSize          = 1024
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_socket.sendto(tosend, server)
msg_server = udp_socket.recvfrom(bufferSize)
msg = "Server: {}".format(msg_server[0])
print(msg)
