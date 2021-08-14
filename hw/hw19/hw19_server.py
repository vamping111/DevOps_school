#!/usr/bin/env python3

import socket
server_dom    = "10.10.10.198"
send_dom      = str.encode(server_dom)
server_google = "216.58.209.206"
send_google   = str.encode(server_google)
server_def    = "127.0.0.1"
send_def      = str.encode(server_def)
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_socket.bind(('127.0.01', 2204))
while(True):
    msg_adr = udp_socket.recvfrom(1024)
    message = msg_adr[0]
    address = msg_adr[1]
    clientMsg = "Client:{}".format(message)
    print(clientMsg)
    if clientMsg   == 'Client:b\'domain.name\'':
        udp_socket.sendto(send_dom, address)
    elif clientMsg == 'Client:b\'google.com\'':
        udp_socket.sendto(send_google, address)
    else:
        udp_socket.sendto(send_def, address)
