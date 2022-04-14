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


data = user_socket.recv(4096).decode("utf-8")
print("server: " + data)

if data == "IN-USE\n":
    new_name = input("new username: ")
    second_username = new_name.encode("utf-8")
    print((handshake + second_username + newline))
    user_socket.sendall(handshake + second_username + newline)
    print(user_socket.recv(4096))
    data = user_socket.recv(4096) 

who = "WHO\n".encode("utf-8")
message_send = "SEND".encode("utf-8")

while True:
        my_message = input("send: ")
        print(my_message)

        if(my_message == "quit" or my_message == "Quit"):
            break

        if(my_message == "!who"):
            user_socket.sendall(who)

        if(my_message[0] == "@"):

            #message_username = my_message[0:empty]
            #message_content = my_message[empty:-1]
            #print(message_username)
            my_message = my_message[1:-1]
            send = message_send + my_message + newline
            user_socket.sendall(send)

        print("server:", user_socket.recv(4096))
user_socket.close()
