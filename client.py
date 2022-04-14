import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_port = ("143.47.184.219", 5378)
sock.connect(host_port)

sock.sendall(b"Hello World")

data = sock.recv(4096)

if not data:
    print("Socket is closed.")
else:
    print("Socket has data.")