# Goal: Write a program consisting of a TCP client and server.
#       The server executes commands based on messages received from the client.
# the Client should:
# 1. Prompt the user for a command to execute on the server
# 2. Send the command to the server
# 3. perform cleanup and close the connection to the server if "exit" is entered
# 4. Display the output from the server

# The output:
# $ python3 client.py
# Msg to send: <user enters command>
# Server responded with: <output from command>
# if the user enters "exit" the client should close the connection and exit
# Msg to send: exit
# Server responded with: exit
# closing connection
##########################################################################################

import socket
import sys

def client():

    server_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if server_fd == -1:
        sys.exit("socket")

    addr = ('127.0.0.1', 8080)
    print("Connecting to server")
    try:
        server_fd.connect(addr)
    except socket.error as e:
        sys.exit("connect")

    print("Sending 'hello' to server")
    server_fd.send(b"hello")
    buf = server_fd.recv(1024).decode()
    print("Received:", buf)

    print("Message to send to server: 'exit'")
    server_fd.send(b"exit")
    buf = server_fd.recv(1024).decode()
    print("Server responded with:", buf)
    print("closing connection")

    server_fd.close()

if __name__ == "__main__":
    client()
