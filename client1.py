#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 00:22:34 2020

@author: rohith
"""

import socket

#create a socket
cfd = socket.socket()

#connect to host
cfd.connect(('127.0.0.1',12345))
sendMsg = ""
recvMsg = ""
while not (sendMsg=="Bye".encode() or recvMsg=="Bye".encode()):
    recvMsg = cfd.recv(1024)
    print("Server:",recvMsg.decode())
    inp = input("Client:")
    sendMsg = inp.encode()
    cfd.send(sendMsg)
cfd.close()
