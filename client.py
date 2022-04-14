import socket

IP = ("143.47.184.219")
PORT = 5378

my_username = input("username: ")
user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_socket.connect((IP, PORT))

username = my_username.encode("utf-8")

user_socket.send(username)

my_message = input("")
user_socket.send(my_message)

user_socket.close()
