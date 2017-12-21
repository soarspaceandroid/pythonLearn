#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

server = socket.socket()
host = socket.gethostname()
port = 5555
server.bind((host , port))
server.listen(5)
while True:
    client = server.accept()
    client.send("this is first message")
    client.close()
  
