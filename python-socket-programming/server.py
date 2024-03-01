import socket
import time

xx = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# it will cause the remote server cannot connect to this host with the port 8080, or you can connect from the local host
# host = '127.0.0.1'

# listening on any interface
host = ''
# host = ''


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
