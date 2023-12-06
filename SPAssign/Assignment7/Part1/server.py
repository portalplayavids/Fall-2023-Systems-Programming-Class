#Goal: Write a program consisting of a TCP client and server.
#      The server executes commands based on messages received from the client.
#      the server should: 
#      1. listen for a connection from the client
#      2. accept the connection
#      3. receive data from the client
#      4. respond with "world" when the client sends "hello"
#      5. the server should only exit when the client sends "exit"
#      6. respond with "exit" then close can cleanup (shutdown the server and close the socket) when the client sends "exit"
#      7. display the data received from the client

import socket

def main():

    server_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if server_fd == -1:
        print("socket")
        exit(-1)

    addr = ('', 8080)
    bind_result = server_fd.bind(addr)
    if bind_result == -1:
        print("bind")
        exit(-1)

    listen_result = server_fd.listen(1)
    if listen_result == -1:
        print("listen")
        exit(-1)

    print("Waiting for client to connect")
    client_fd, addr = server_fd.accept()
    if client_fd == -1:
        print("accept")
        exit(-1)
    print("connected to client")

    buf = client_fd.recv(1024).decode()
    print("Message recieved from client:", buf)
    client_fd.sendall(b"world")
    print("Responding with: 'world'")

    buf = client_fd.recv(1024).decode()
    print("Message recieved from client:", buf)
    client_fd.sendall(b"exit")
    print("Responding with:", buf)
    print("closing connection")

    server_fd.close()
    client_fd.close()

if __name__ == "__main__":
    main()
