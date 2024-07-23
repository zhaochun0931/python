import socket

node_name = 'hello-world-server-1'
ip_address = socket.gethostbyname(node_name)
print(f"IP address of {node_name} is {ip_address}")
