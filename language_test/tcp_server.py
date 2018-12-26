#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 16:36
# @Author  : Kevindi
# @Site    : 
# @File    : tcp_server.py
# @Software: PyCharm Community Edition
# @Desc    :

from socketserver import BaseRequestHandler,TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('get connection from ',self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            else:
                print('get msg ',msg)
            self.request.send(b'Hello client')


from socketserver import StreamRequestHandler, TCPServer

# error 无法收到数据
class EchoHandler_s(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            print('got from client:',line)
            # self.wfile is a file-like object for writing
            self.wfile.write(line)
        print('send all.')


# socketserver 可以让我们很容易的创建简单的TCP服务器。 但是，你需要注意的是，
# 默认情况下这种服务器是单线程的，一次只能为一个客户端连接服务。 如果你想处理多个客户端，
# 可以初始化一个 ForkingTCPServer 或者是 ThreadingTCPServer 对象

from socketserver import ThreadingTCPServer
import threading

if __name__ == '__main__':
    serv1 = TCPServer(('',20000),EchoHandler)
    # serv2 = TCPServer(('', 20001), EchoHandler_s)
    t1 = threading.Thread(target=serv1.serve_forever)
    t1.start()
    # serv1.serve_forever()
    # t2 = threading.Thread(target=serv2.serve_forever)
    # t2.start()
    # t2.join()

    serv3 = ThreadingTCPServer(('', 20002), EchoHandler)
    serv3.serve_forever()
    t1.join()

