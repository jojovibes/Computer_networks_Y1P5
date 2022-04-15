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
    user_socket.sendall(handshake + second_username + newline)
    print(user_socket.recv(4096))
    data = user_socket.recv(4096) 
    if data == "IN-USE\n":
        new_name = input("new username: ")
        second_username = new_name.encode("utf-8")
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

        elif(my_message == "!who"):
            user_socket.sendall(who)

        elif(my_message[0] == "@"):

            empty = my_message.index(' ')
            empty2 = empty + 1
            message_username = my_message[1:empty]
            message_content = my_message[empty2:-1]

            message_username = bytes(message_username, 'utf-8')
            message_content = bytes(message_content, 'utf-8')
            my_message = my_message[1:]
            
            my_message = bytes(my_message, 'utf-8')
            send = message_send + message_username + message_content + newline
            user_socket.sendall(send)
            

        print("server:", user_socket.recv(4096))
user_socket.close()
