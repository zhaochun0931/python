import socket
import time

xx = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'

port = 9999

xx.bind((host,port))

xx.listen(5)

while True:
    print("the server is listening on the port %d" %port)
    clientconn, addr = xx.accept()
    print("Got a connection from %s" % str(addr))
    current_time = time.ctime(time.time())
    clientconn.send(current_time.encode('ascii'))
    clientconn.close()
