import socket

yy = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '10.0.0.4'
port = 8080

yy.connect((host,port))

mytime = yy.recv(1024)

yy.close()

print("The time got from the server is %s" %mytime.decode('ascii') )
