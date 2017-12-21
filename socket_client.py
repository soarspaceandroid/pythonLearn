#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket               # 导入 socket 模块
from test import log

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 5555                # 设置端口好

s.connect((host, port))
log(s.recv(500))
s.close()  
