import socket

host_port = ("143.47.184.219", 5378)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(host_port)

my_username = input("username: ")

username = my_username.encode("utf-8")

handshake = "HELLO-FROM ".encode("utf-8")
newline = " \n".encode("utf-8")

print(handshake + username + newline)

sock.sendall(handshake + username + newline)
print(sock.recv(4096))

data = sock.recv(4096).decode("utf-8")

if not data:
    print("Socket is closed.")
else:
    print("Socket has data.")
    if data == "IN-USE\n":
        new_name = input("new username: ")
        second_username = new_name.encode("utf-8")
        print((handshake + second_username + newline))
        sock.sendall(handshake + second_username + newline)
        print(sock.recv(4096))
        data = sock.recv(4096)
    else:
        sock.close()



