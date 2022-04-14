from cgi import test
import socket
import threading
import select


my_username = input("username: ")
username = my_username.encode("utf-8")
hostport = ("143.47.184.219", 5378)
user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_socket.connect(hostport)

handshake = "HELLO-FROM ".encode("utf-8")
newline = " \n".encode("utf-8")

test_hello = handshake + username + newline
user_socket.sendall(test_hello)
print ("server:", user_socket.recv(4096))

while True:
        my_message = input("send: ")
        message = my_message.encode("utf-8")

        if(message == "quit" or message == "Quit"):
            break

        user_socket.sendall(message)
        print ("server:", user_socket.recv(4096))
user_socket.close()
