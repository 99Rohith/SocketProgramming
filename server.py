#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 00:26:27 2020

@author: rohith
"""

import socket

#create a socket
sfd = socket.socket()
#bind the socket to a IP and port
sfd.bind(('',12345))
#listen for client
sfd.listen(5)
print("LISTENING......")

c,addr = sfd.accept()
print("connected to client with address",addr)

sendMsg = ""
recvMsg = ""
while sendMsg!="Bye".encode():
    #accept client connection
    inp =  input("Server:")
    sendMsg = inp.encode();
    c.send(sendMsg)
    recvMsg = c.recv(1024);
    print("Client :",recvMsg.decode())
    if recvMsg == "Bye".encode():
        #close the connection with the client and open new connection
        c.close()
        c,addr = sfd.accept()
        print("connected to client with address",addr)
c.close()
