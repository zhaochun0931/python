import socket

yy = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9999

yy.connect((host,port))

mytime = yy.recv(1024)

yy.close()

print("The time got from the server is %s" %mytime.decode('ascii') )
