'''
Write a set of Python classes that can simulate an Internet application in
which one party, Alice, is periodically creating a set of packets that she
wants to send to Bob. An Internet process is continually checking if Alice
has any packets to send, and if so, it delivers them to Bob’s computer, and
Bob is periodically checking if his computer has a packet from Alice, and,
if so, he reads and deletes it.
'''

import socket

class Client():
    def __init__(self,name,host,port):
        self.__name__ = name
        self.__host__ = host
        self.__port__ = port
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        print(self.__name__+':Connected to'+self.__host__+':'+str(self.__port__))
        while 1:
            toServer = input('[----From: '+self.__name__+']\nPlease input packet：')
            s.sendall(('----From: '+self.__name__+'['+toServer+']').encode())
            fromServer = s.recv(1024)
            print(fromServer.decode())
        conn.close()
Alice = Client('Alice','127.0.0.1',14174)
