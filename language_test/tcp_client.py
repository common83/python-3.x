#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 16:40
# @Author  : Kevindi
# @Site    : 
# @File    : tcp_client.py
# @Software: PyCharm Community Edition
# @Desc    :

from socket import socket,AF_INET,SOCK_STREAM

def send_data(port):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect(('localhost',port))
    print('connect port = ',port)
    i = 10
    while i:
        s.send(b'Hello,server')
        msg = s.recv(8192)
        print('response msg = ',msg)
        i -= 1
    s.close()

if __name__ == '__main__':
    send_data(20000)
    # send_data(20001)
    send_data(20002)
