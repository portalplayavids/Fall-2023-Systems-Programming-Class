#!/usr/bin/env python3

import socket
from subprocess import Popen, PIPE
import subprocess

# import your modules
import fileio
import command



def run_command(cmd: str) -> bytes:
    '''
        Use your Command module here and
        return the results.
    '''
    result = subprocess.run(cmd, shell=True, capture_output=True, check=True)
    return result.stdout
pass


def upload_file(filename='server_upload.txt') -> bytes:
    '''
        The server has received the "download_file" command.
        This means the client is trying to download a file from the server.
        The server will upload thie file.

        Use your FileIO module to read the file contents and return the contents
    '''

    # 1: call your read_file function
    # you can use the default filename above
    read_file = fileio.FileIO.read_file(filename)
    # 2: return results
    return read_file
pass


def download_file(data: bytes, filename='server_download.txt') -> None:
    '''
        The server has received the "upload_file" command.
        This means the server should download the file from the client

        Use your FileIO module to write the file contents
    '''

    # 1: call your write_file function here
    # you can use the default filename above
    fileio.FileIO.write_file(data, filename)

    pass


if __name__ == "__main__":
    # The server should listen for data from the client and should determine
    # what functions to run based on what the client requested

    s = socket.socket()          # Create a socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    HOST = '127.0.0.1'
    PORT = 8080                  # Reserve a port for your service.

    # TODO
    # write code for bind, listen
    s.bind((HOST, PORT))
    s.listen(5)

    # accepting clients
    conn, addr = s.accept()

    # Update the logic to handle the different cases.
    print(f"Connected to client: {addr}")
    while True:
        cmd = conn.recv(4096)
        print(cmd)
        # 1.) run_command
        if cmd == b'run_command':
            # Initial message to ask the command
            conn.sendall(b'What command would you like to run?')
            # The client should recv the message and server just waits
            # for the incomming message
            client_cmd = conn.recv(4096)

            # Decode the client_cmd bytes object into a string
            client_cmd = client_cmd.decode()

            # This gets sent to our run command function
            # make sure to fill it out
            result = run_command(client_cmd)

            # The run command results are sent back to the client
            conn.sendall(result)

        # 2.) upload_file
        elif cmd == b'upload_file':
            # The client wants to upload a file
            # Which means the server should download a file sent by the client

            # 1.) send acknowledgement to the client
            # example: s.sendall(b"Waiting for the file")
            conn.sendall(b'Waiting for the file')

            # 2.) Recv the data
            data = conn.recv(4096)

            # 3.) call the download_file function
            download_file(data)

        # 3.) download_file
        elif cmd == b'download_file':
            # The client wants to download a file
            # Which means the server should upload a file to send to the client
            conn.sendall(b'Sending the file')
            # 1.) Call upload function
            data = upload_file()
            # 2.) Send the results back to the client
            conn.sendall(data)

        # 4.) exit
        elif cmd == b'exit':
            # use `break` to exit loop
            break
        pass

        if not conn:
            break
    conn.close()
    s.close()
