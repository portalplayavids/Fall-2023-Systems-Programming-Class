## Programming Assignment 7

### Part 1: Python TCP/IP Programming (50 points)

#### Objective:
Write a Python program consisting of a TCP server and client. The server executes commands based on messages received from the client.

#### Tasks:

1. **Server (`server.py`):**
    - Create a TCP server using Python.
    - The server should:
        - Respond with "world" when it receives the message "hello".
        - Respond with "exit", then close and clean up (shut down the server and close socket file handles) when it receives the message "exit".

2. **Client (`client.py`):**
    - Create a TCP client using Python.
    - The client should:
        - Take input from the user and send it to the server.
        - Perform cleanup and close the connection if "exit" is entered.

#### Expected Output:
When running `client.py`:
```bash
    $ python3 client.py
    Msg to send: hello
    Server responded with: world

    Msg to send: exit
    Server responded with: exit
    closing connection
```

When running `server.py`:
```bash
    $ python3 server.py
    Msg received from client: hello
    Responding with: world

    Msg received from client: exit
    Responding with: exit
    closing connection
```

### Part 2: C TCP/IP Programming (50 points)

#### Objective:
Write a C program consisting of a TCP server and client. The server executes commands based on messages received from the client.

#### Tasks:

1. **Server (`server.c`):**
    - Create a TCP server using C.
    - The server should:
        - Respond with "world" when it receives the message "hello".
        - Respond with "exit", then close and clean up (shut down the server and close socket file handles) when it receives the message "exit".

2. **Client (`client.c`):**
    - Create a TCP client using C.
    - The client should:
        - Take input from the user and send it to the server.
        - Perform cleanup and close the connection if "exit" is entered.

#### Expected Output:
When running `client.c`:
```bash
    $ ./client
    Msg to send: hello
    Server responded with: world

    Msg to send: exit
    Server responded with: exit
    closing connection
```

When running `server.c`:
```bash
    $ ./server
    Msg received from client: hello
    Responding with: world

    Msg received from client: exit
    Responding with: exit
    closing connection
```
