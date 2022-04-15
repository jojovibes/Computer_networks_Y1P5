import socket

my_username = input("username: ")
username = my_username.encode("utf-8")
hostport = ("143.47.184.219", 5378)

user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_socket.connect(hostport)

handshake = "HELLO-FROM ".encode("utf-8")
newline = "\n".encode("utf-8")

test_hello = handshake + username + newline
print(test_hello)
user_socket.sendall(test_hello)


data = user_socket.recv(4096).decode("utf-8")
print("server: " + data)

while data == "IN-USE\n":
    user_socket.close()
    my_username = input("username: ")
    username = my_username.encode("utf-8")
    hostport = ("143.47.184.219", 5378)

    user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    user_socket.connect(hostport)

    handshake = "HELLO-FROM ".encode("utf-8")
    newline = "\n".encode("utf-8")

    test_hello = handshake + username + newline
    user_socket.sendall(test_hello)


    data = user_socket.recv(4096).decode("utf-8")
    print("server: " + data)


who = "WHO\n".encode("utf-8")
message_send = "SEND ".encode("utf-8")

while True:
    my_message = input("send: ")

    if(my_message == "!quit"):
        break

    elif(my_message == "!who"):
        user_socket.sendall(who)
        print("server:", user_socket.recv(4096).decode("utf-8"))

    elif(my_message[0] == "@"):

        my_message = my_message[1:]

        my_message = bytes(my_message, 'utf-8')
        send = message_send + my_message + newline
        user_socket.sendall(send)
        print("server:", user_socket.recv(4096).decode("utf-8"))
        socket.timeout(3) 
        print("server:", user_socket.recv(4096).decode("utf-8"))


user_socket.close()
