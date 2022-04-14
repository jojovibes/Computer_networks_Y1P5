import socket
import threading
import select

IP = ("143.47.184.219")
PORT = 5378

my_username = input("username: ")
hostport = ("143.47.184.219", 5378)
user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_socket.connect(hostport)

username = my_username.encode("utf-8")

# user_socket.send(username)

#my_message = input("")
# user_socket.send(my_message)


handshake = "HELLO-FROM ".encode("utf-8")
newline = " \n".encode("utf-8")

print(handshake + username + newline)

user_socket.sendall(handshake + username + newline)
print(user_socket.recv(4096))

data = user_socket.recv(4096)

if not data:
    print("Socket is closed.")
else:
    print("Socket has data.")

user_socket.close()
