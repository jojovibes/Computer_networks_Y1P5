import socket
import threading

user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostport = ("143.47.184.219", 5378)
user_socket.connect(hostport)

my_username = input("username: ")
username = my_username.encode("utf-8")

handshake = "HELLO-FROM ".encode("utf-8")
newline = "\n".encode("utf-8")
who = "WHO\n".encode("utf-8")
message_send = "SEND ".encode("utf-8")

test_hello = handshake + username + newline
user_socket.sendall(test_hello)

data = user_socket.recv(4096).decode("utf-8")
print("server: " + data)

def send():
    while True:
        my_message = input()

        if(my_message == "!quit"):
            user_socket.close()
            return

        elif(my_message == "!who"):
            user_socket.sendall(who)
    
        elif(my_message[0] == "@"):

            my_message = my_message[1:]

            my_message = bytes(my_message, 'utf-8')
            send = message_send + my_message + newline
            user_socket.sendall(send)

       
        
def receive():
    global user_socket
    while True:
        data = user_socket.recv(1).decode("utf-8")
        while data[-1] != "\n":
            data += user_socket.recv(1).decode("utf-8")
       
        
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



t2 = threading.Thread(target=receive, args = (), daemon=True)

t2.start()

send()




