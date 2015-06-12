__author__ = 'tkessler'

from socket import socket, AF_INET, SOCK_STREAM

port = 50008
host = 'localhost'

def server():
    sock = socket() #AF_INET and SOCK_STREAM are defaults...
    sock.bind(("",port))
    sock.settimeout(1)
    sock.listen(5) #support 5 clients
    while True:
        (connObj, addr) = sock.accept()
        data = connObj.recv(1024) #save 1024 bytes of data...
        reply = 'Server received: %s' % data.decode()
        connObj.send(reply.encode())

def client(name):
    sock = socket()
    try:
        sock.connect((host,port)) #connect, if port is open...
    except:
        return 1
    sock.send(name.encode()) #send data to the server...
    reply = sock.recv(1024) #receive a response...
    sock.close() #close the connection
    print('Client receives response: %s' % reply.decode())

if __name__ == "__main__":
    from threading import Thread
    sthread = Thread(target=server)
    sthread.setDaemon(True)
    sthread.start() #start server thread, and open the socket
    for i in range(5):
        Thread(target=client, args=("%s" % i)).start()