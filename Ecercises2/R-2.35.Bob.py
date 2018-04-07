'''
Write a set of Python classes that can simulate an Internet application in
which one party, Alice, is periodically creating a set of packets that she
wants to send to Bob. An Internet process is continually checking if Alice
has any packets to send, and if so, it delivers them to Bob’s computer, and
Bob is periodically checking if his computer has a packet from Alice, and,
if so, he reads and deletes it.
'''
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 14174              # The same port as used by the server

class Server():
    def __init__(self,name,host,port):
        self.__name__ = name
        self.__host__ = host
        self.__port__ = port
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((host,port))
        s.listen(1)
        print(self.__name__+' is listening from '+host+'\nPort is : '+str(self.__port__))
        while 1:
            conn,addr = s.accept()
            print('Connected by:',addr)
            while 1:
                clintData = conn.recv(1024)
                print(clintData.decode())
                if not clintData:break
                srReply ='From ['+ self.__name__+'], Packet read and deleted!.'
                conn.sendall(srReply.encode())
        conn.close()
Bob = Server('Bob','127.0.0.1',14174)
Lisa = Server('Lisa','127.0.0.1',14175)
